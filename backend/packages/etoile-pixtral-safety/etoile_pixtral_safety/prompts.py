prompts = {
    "test_safety": """
Is there any harmful content on this page? Analyze based on the following categories:
- Explicit adult content
- Sexual content or suggestive imagery
- Bullying or harassment
- Hate speech or discriminatory language
- Violent or gore content
- Weapons or dangerous tools
- Drug or substance abuse
- War or terrorism-related content
- Child exploitation or grooming
- Self-harm or suicide-related content
- Abusive or dangerous challenges
- Criminal activity or illegal practices
- Scams or phishing attempts
- Gambling or betting-related content
- Predatory ads or inappropriate marketing
- Harmful or inappropriate external links
- Promotion of unhealthy eating habits
- Mental health triggers (anxiety, depression)
- Misleading or misinformation content

Write the response in the following format:
{
    "explicit_adult_content": 0,  // 1 for yes, 0 for no
    "sexual_content": 0,
    "bullying_harassment": 0,
    "hate_speech": 0,
    "violent_gore_content": 0,
    "weapons_dangerous_tools": 0,
    "drug_substance_abuse": 0,
    "war_terrorism_content": 0,
    "child_exploitation_grooming": 0,
    "self_harm_suicide": 0,
    "abusive_challenges": 0,
    "criminal_activity": 0,
    "scams_phishing": 0,
    "gambling_betting_content": 0,
    "predatory_ads": 0,
    "harmful_external_links": 0,
    "unhealthy_eating_habits": 0,
    "mental_health_triggers": 0,
    "misinformation": 0,
    "comment": "The overall content description"
}
Write the response in JSON format within ``` tags and provide the response only, without any additional explanation.
""",
    "find_section": """
We have detected harmful content in the image. Please provide the location of the harmful content within the image.
Write the response in the following format:
{
    "top": 0,
    "right": 0,
    "width": 100,
    "height": 100,
    "isHarmful": 1, // 1 if yes, 0 if no
    "comment": "some comment"
}
Write the response in JSON format within ``` tags and provide the response only, without any additional explanation.
"""
}