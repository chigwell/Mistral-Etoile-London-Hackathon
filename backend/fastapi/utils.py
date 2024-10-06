import requests
import base64


def upload_image(api_key, image_path):
    url = 'https://api.imgbb.com/1/upload'
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    payload = {
        'key': api_key,
        'image': encoded_string
    }
    response = requests.post(url, data=payload)
    return response.json()