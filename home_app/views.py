#from .utils import get_moon_image
from django.shortcuts import render
#import requests
# Create your views here.
def about(request):
   return render(request, 'about.html') 
"""
def get_moon_image(api_key):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date=today"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200 and data.get("media_type") == "image":
        return data.get("url")
    else:
        return None

# APIキーを設定
api_key = "e5iNBJbsZSKCpBcYR0sNo0v8CQu3APKDKtzb7ofS"

# 関数を呼び出して今夜の月の画像URLを取得
moon_image_url = get_moon_image(api_key)

if moon_image_url:
    print("今夜の月の画像URL:", moon_image_url)
else:
    print("今夜の月の画像を取得できませんでした。")
"""
def home(request):
    """
    api_key = "e5iNBJbsZSKCpBcYR0sNo0v8CQu3APKDKtzb7ofS"
    moon_image_url = get_moon_image(api_key)
    """
    return render(request, 'home.html',) #{'moon_image_url': moon_image_url})