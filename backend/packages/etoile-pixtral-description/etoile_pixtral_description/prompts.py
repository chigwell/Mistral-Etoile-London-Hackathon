prompts = {
    "describe_image": """
Please analyze the screen and provide a detailed, concrete description of each content characteristic visible on the web page. For images, specify the colors and subjects depicted. For text, describe the semantic meaning rather than just labeling the element type.

Write the response in the following format:
{
    "description": "Provide a comprehensive and detailed description of each element, mentioning specific colors, subjects, and the semantic meaning of text"
}
For example, if there is a logo with a cat, describe it as 'an orange cat in the logo.' If there is a header, explain what it discusses, such as 'a header discussing the latest pet care techniques.'
Inside the 'description' value please do not use any special characters like ' or ". only {
    "description": "text without special characters or quotes please"
}
Write the response in JSON format within ``` tags and provide the response only, without any additional explanation.
"""
}
