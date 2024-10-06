from langchain_core.pydantic_v1 import BaseModel, Field


class TestContentSafety(BaseModel):
    explicit_adult_content: int = Field(..., title="Is there explicit adult content? 1 for yes, 0 for no")
    sexual_content: int = Field(..., title="Is there sexual content or suggestive imagery? 1 for yes, 0 for no")
    bullying_harassment: int = Field(..., title="Is there bullying or harassment? 1 for yes, 0 for no")
    hate_speech: int = Field(..., title="Is there hate speech or discriminatory language? 1 for yes, 0 for no")
    violent_gore_content: int = Field(..., title="Is there violent or gore content? 1 for yes, 0 for no")
    weapons_dangerous_tools: int = Field(..., title="Are there mentions of weapons or dangerous tools? 1 for yes, 0 for no")
    drug_substance_abuse: int = Field(..., title="Are there mentions of drug or substance abuse? 1 for yes, 0 for no")
    war_terrorism_content: int = Field(..., title="Is there war or terrorism-related content? 1 for yes, 0 for no")
    child_exploitation_grooming: int = Field(..., title="Is there content related to child exploitation or grooming? 1 for yes, 0 for no")
    self_harm_suicide: int = Field(..., title="Is there content related to self-harm or suicide? 1 for yes, 0 for no")
    abusive_challenges: int = Field(..., title="Are there mentions of abusive or dangerous challenges? 1 for yes, 0 for no")
    criminal_activity: int = Field(..., title="Are there mentions of criminal activity or illegal practices? 1 for yes, 0 for no")
    scams_phishing: int = Field(..., title="Are there scams or phishing attempts? 1 for yes, 0 for no")
    gambling_betting_content: int = Field(..., title="Is there gambling or betting-related content? 1 for yes, 0 for no")
    predatory_ads: int = Field(..., title="Are there predatory ads or inappropriate marketing? 1 for yes, 0 for no")
    harmful_external_links: int = Field(..., title="Are there harmful or inappropriate external links? 1 for yes, 0 for no")
    unhealthy_eating_habits: int = Field(..., title="Is there promotion of unhealthy eating habits? 1 for yes, 0 for no")
    mental_health_triggers: int = Field(..., title="Are there mental health triggers (anxiety, depression)? 1 for yes, 0 for no")
    misinformation: int = Field(..., title="Is there misleading or misinformation content? 1 for yes, 0 for no")
    comment: str = Field(..., title="The overall content description")


class ContentLocation(BaseModel):
    top: int = Field(..., title="Top offset of the detected content in px")
    right: int = Field(..., title="Right offset of the detected content in px")
    width: int = Field(..., title="Width of the detected content in px")
    height: int = Field(..., title="Height of the detected content in px")
    isHarmful: int = Field(..., title="Is the detected content harmful? 1 for yes, 0 for no")
    comment: str = Field(..., title="The overall content description")
