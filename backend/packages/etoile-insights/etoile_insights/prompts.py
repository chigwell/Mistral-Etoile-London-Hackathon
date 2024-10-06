prompts = {
    "get_interests": """
Based on provided info you need to find the interests of the user.
The output should be a list of interests.
The output should be in the following format:
{
    "interests": [
        {
            "interest_name": "Interest 1",
            "interest_value": 30
        },
        {
            "interest_name": "Interest 2",
            "interest_value": 70
        }
    ]
}
Write the response in JSON format within ``` tags and provide the response only, without any additional explanation.
""",
"get_psychological_insights": """
Based on provided info you need to find the psychological insights of the user.
For example if user reads news, it can mean that user is curious and eager to learn the latest actual information about society.
If the context is about games, it can mean that user is competitive and likes to win.
The output should be a list of psychological traits or behaviors.
The output should be in the following format:
{
    "insights": [
        {
            "insight": "Shows curiosity and eagerness to learn"
        }
    ]
}
Do not imagine anything. Provide only info based on context.
Write the response in JSON format within ``` tags and provide the response only, without any additional explanation.
""",
    "get_professional_potentials": """
Based on provided info you need to find the professional career potentials of the user.
The output should be a list of statements regarding the user's potential in various professional fields.
The output should be in the following format:
{
    "potentials": [
        {
            "potential": "The child shows strong potential in STEM fields, particularly in areas that combine technology and creativity."
        },
        {
            "potential": "There's a notable inclination towards arts and design, suggesting potential in creative professions."
        },
        {
            "potential": "The diverse interests indicate adaptability, which is valuable in many modern careers."
        },
        {
            "potential": "Strong analytical skills suggest potential excellence in research or data-driven fields."
        }
    ]
}
Do not imagine anything. Provide only info based on context.
For example if user is interested in technology, it can mean that user has potential in STEM fields.
If the user likes news, it can mean that user has potential in journalism.
Write the response in JSON format within ``` tags and provide the response only, without any additional explanation.
""",
}
