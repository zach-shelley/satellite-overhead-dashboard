import os
import requests 
from dotenv import load_dotenv

load_dotenv()

# GET reqeusts for all data

API_KEY = os.getenv('API_KEY')
MY_LAT = os.getenv('MY_LAT')
MY_LONG = os.getenv('MY_LONG')
MY_ALT = os.getenv('MY_ALT')

API_URL = f"{os.getenv('API_URL')}{MY_LAT}/{MY_LONG}/{MY_ALT}/45/36/&apiKey={API_KEY}"



response = requests.get(API_URL)
data = response.json()

intro = "===== Satellites Flying Overhead ====="
center_text = intro.center(50)
print(center_text)
for d in data["above"]:
    print(f"""
Satellite Type: {data["info"]["category"]}
Satellite ID: {d["satid"]}
Satellite Name: {d["satname"]}
Satellite Launch Date: {d["launchDate"]}
Latitude: {d["satlat"]}
Longitude: {d["satlng"]}
Altitude: {d["satalt"]}
""", end="\n")
