"""
import requests

def get_moon_image(api_key):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date=today"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200 and data.get("media_type") == "image":
        return data.get("url")
    else:
        return None
"""