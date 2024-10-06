import os
import json
import base64
import hashlib
import datetime


import uvicorn
from fastapi import FastAPI, HTTPException, Request, Response, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from utils import upload_image
from db import Base, Screenshot, Risk, Graph, Insight, DATABASE_FILENAME, engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError


from langchain_mistralai import ChatMistralAI
from decimal import Decimal, ROUND_HALF_UP

from etoile_pixtral_safety import check_image, find_location
from etoile_pixtral_description import describe_image
from etoile_graph import generate_graph
from etoile_insights import get_interests, get_psychological_insights, get_professional_potentials

API_IMAGE_KEY = os.getenv("API_IMAGE_KEY")
CVISION_MODEL = "pixtral-12b-2409"
MISTRAL_LARGE_LATEST = "mistral-large-latest"

Base.metadata.create_all(engine)



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/screenshot")
async def screenshot(request: Request):

    if not os.path.exists("hashes.txt"):
        with open("hashes.txt", "w") as f:
            f.write("")

    if not os.path.exists("images"):
        os.makedirs("images")

    data = await request.json()
    image_data = data.get("image")
    if not image_data:
        raise HTTPException(status_code=400, detail="Missing image data")
    if image_data.startswith('data:image/png;base64,'):
        image_data = image_data.replace('data:image/png;base64,', '')
    image = base64.b64decode(image_data)


    md5 = hashlib.md5()
    md5.update(image)
    print(md5.hexdigest())

    with open("hashes.txt", "r") as f:
        hashes = f.readlines()

    if md5.hexdigest() in hashes:
        return {"message": "Screenshot already exists"}

    curr_date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    with open("images/"+curr_date+".png", "wb") as f:
        f.write(image)
    with open("hashes.txt", "w") as f:
        f.write(md5.hexdigest())

    file_path = os.path.join(os.getcwd(), "images", curr_date+".png")
    res = upload_image(API_IMAGE_KEY, file_path)
    display_url = res['data']['display_url']

    Session = sessionmaker(bind=engine)
    session = Session()
    new_screenshot = Screenshot(link=display_url, description='', datetime=datetime.datetime.now())
    session.add(new_screenshot)
    session.commit()


    llm = ChatMistralAI(
        model=CVISION_MODEL,
        temperature=0,
        max_retries=2,
    )

    res = check_image(llm, display_url, verbose=True)
    print(res)
    """
    res=explicit_adult_content=0 sexual_content=0 bullying_harassment=0 hate_speech=0 violent_gore_content=0 weapons_dangerous_tools=0 drug_substance_abuse=0 war_terrorism_content=0 child_exploitation_grooming=0 self_harm_suicide=0 abusive_challenges=0 criminal_activity=0 scams_phishing=0 gambling_betting_content=0 predatory_ads=0 harmful_external_links=0 unhealthy_eating_habits=0 mental_health_triggers=0 misinformation=0 comment='The page appears to be a job portal with various icons and job listings. No harmful content is visible.'
    """
    alerts = {field_name: getattr(res, field_name) for field_name in res.__fields__.keys() if
              getattr(res, field_name) != 0}

    if alerts:
        for key, value in alerts.items():
            if key == 'comment':
                continue
            new_risk = Risk(risk_type=key, screen_id=new_screenshot.id, datetime=datetime.datetime.now())
            session.add(new_risk)

        session.commit()
        session.close()

        print("Alert: " + ", ".join(f"{key}={value}" for key, value in alerts.items()) + " content detected.")
        return JSONResponse(content={"message": 1})
    else:
        print("All content checks passed. No harmful content detected.")

    session.close()
    return {"message": 0}



@app.get("/screenshots")
async def screenshots():
    Session = sessionmaker(bind=engine)
    session = Session()
    all_screenshots = session.query(Screenshot).all()
    session.close()
    json_response = []
    for screenshot in all_screenshots:
        json_response.append({
            "id": screenshot.id,
            "link": screenshot.link,
            "description": screenshot.description,
            "graph": jsonable_encoder(json.loads(screenshot.graph)) if screenshot.graph else [],
            "datetime": screenshot.datetime,
        })
    return json_response

@app.get("/screenshot")
async def get_screenshot(id: int = Query(..., title="Identifier", description="Numeric identifier to retrieve data")):
    # return image itself
    Session = sessionmaker(bind=engine)
    session = Session()
    screenshot = session.query(Screenshot).filter(Screenshot.id == id).first()
    session.close()
    if screenshot is None:
        raise HTTPException(status_code=404, detail="Screenshot not found")
    return Response(content=screenshot.link, media_type="image/png")


@app.get("/description")
async def description(id: int = Query(..., title="Identifier", description="Numeric identifier to retrieve data")):

    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        screenshot = session.query(Screenshot).filter(Screenshot.id == id).first()
        if screenshot is None:
            raise HTTPException(status_code=404, detail="Screenshot not found")

        if screenshot.description == '':
            llm = ChatMistralAI(
                model=CVISION_MODEL,
                temperature=0,
                max_retries=2,
            )
            res = describe_image(llm, screenshot.link, verbose=True)
            screenshot.description = res.description

            session.commit()

        return {"description": screenshot.description}

    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        session.close()


@app.get("/graph")
async def graph(id: int = Query(..., title="Identifier", description="Numeric identifier to retrieve data")):

    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        screenshot = session.query(Screenshot).filter(Screenshot.id == id).first()
        if screenshot is None:
            raise HTTPException(status_code=404, detail="Screenshot not found")

        if screenshot.graph == None and screenshot.description != '':
            llm = ChatMistralAI(
                model=CVISION_MODEL,
                temperature=0,
                max_retries=2,
            )
            res = generate_graph(llm, [screenshot.description], verbose=True)
            relationships_json = json.dumps(res.relationships, default=lambda o: o.dict() if hasattr(o, 'dict') else o)

            screenshot.graph = relationships_json

            session.commit()

        return {"graph": jsonable_encoder(json.loads(screenshot.graph))}

    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        session.close()

@app.get("/insights")
def get_insights():
    Session = sessionmaker(bind=engine)
    session = Session()

    all_screenshots = session.query(Screenshot).all()
    session.close()

    if not all_screenshots:
        return {"insights": []}

    insights_data = []
    for screenshot in all_screenshots:
        if screenshot.graph:
            insights_data.append({"graph": jsonable_encoder(json.loads(screenshot.graph)), "datetime": screenshot.datetime})

    llm = ChatMistralAI(
        model=MISTRAL_LARGE_LATEST,
        temperature=0,
        max_retries=2,
    )
    texts = [str(insights_data)]
    interests = get_interests(llm, texts, verbose=True)
    interests = interests.interests

    try:
        total_interest_value = sum(interest.interest_value for interest in interests)
    except AttributeError:
        # Log the problematic data and return an error message
        print(f"Error processing interests: {interests}")
        return {"message": "Error processing interests, data may be malformed."}

    insights = []
    if total_interest_value > 0:
        for interest in interests:
            percent = (interest.interest_value / total_interest_value) * 100
            formatted_percent = Decimal(percent).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
            insights.append({
                "interest_name": interest.interest_name,
                "percent": f"{formatted_percent}%"
            })
    else:
        return {"message": "No interests found or total interest value is zero"}

    return {"insights": insights}

@app.get("/psychological-insights")
def psychological_insights():
    Session = sessionmaker(bind=engine)
    session = Session()

    all_screenshots = session.query(Screenshot).all()
    session.close()

    if not all_screenshots:
        return {"psychological_insights": []}

    insights_data = []
    for screenshot in all_screenshots:
        if screenshot.graph:
            insights_data.append({"graph": jsonable_encoder(json.loads(screenshot.graph)), "datetime": screenshot.datetime})

    llm = ChatMistralAI(
        model=MISTRAL_LARGE_LATEST,
        temperature=0,
        max_retries=2,
    )
    texts = [str(insights_data)]
    psychological_insights = get_psychological_insights(llm, texts, verbose=True)
    psychological_insights = psychological_insights.insights

    return {"psychological_insights": psychological_insights}

@app.get("/professional-potentials")
def professional_potentials():
    Session = sessionmaker(bind=engine)
    session = Session()

    all_screenshots = session.query(Screenshot).all()
    session.close()

    if not all_screenshots:
        return {"professional_potentials": []}

    insights_data = []
    for screenshot in all_screenshots:
        if screenshot.graph:
            insights_data.append({"graph": jsonable_encoder(json.loads(screenshot.graph)), "datetime": screenshot.datetime})

    llm = ChatMistralAI(
        model=MISTRAL_LARGE_LATEST,
        temperature=0,
        max_retries=2,
    )
    texts = [str(insights_data)]
    professional_potentials = get_professional_potentials(llm, texts, verbose=True)
    professional_potentials = professional_potentials.potentials

    return {"professional_potentials": professional_potentials}


@app.get("/risks")
def get_risks():
    Session = sessionmaker(bind=engine)
    session = Session()

    all_risks = session.query(Risk).all()
    session.close()

    risks = []
    for risk in all_risks:
        risks.append({
            "risk_type": risk.risk_type,
            "screen_id": risk.screen_id,
            "datetime": risk.datetime
        })

    return {"risks": risks}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)