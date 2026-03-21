import os
import requests 
from dotenv import load_dotenv
from output_aggregation import display_satellites
from datetime import datetime
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

load_dotenv()

MOCK_SATELLITES = {"Yaogan": [{"satid": 65563,"satname": "YAOGAN 45","intDesignator": "2025-201M","launchDate": "2025-09-08","satlat": 19.8969,"satlng": -135.9718,"satalt": 7487.9503}],"Beidao": [{"satid": 40748,"satname": "BEIDOU-3 M1","intDesignator": "2015-037A","launchDate": "2015-07-25","satlat": 54.52,"satlng": -86.0262,"satalt": 21559.2291},{"satid": 43107,"satname": "BEIDOU 3M3","intDesignator": "2018-003A","launchDate": "2018-01-11","satlat": 52.9441,"satlng": -114.9426,"satalt": 21521.81},{"satid": 44542,"satname": "BEIDOU 3M23","intDesignator": "2019-061A","launchDate": "2019-09-22","satlat": 23.1359,"satlng": -143.6803,"satalt": 21544.7893}],"Glonasss Operational": [{"satid": 32276,"satname": "COSMOS 2432 (GLONASS)","intDesignator": "2007-052B","launchDate": "2007-10-26","satlat": 63.2176,"satlng": -108.9875,"satalt": 19146.5594},{"satid": 32395,"satname": "COSMOS 2436 (GLONASS)","intDesignator": "2007-065C","launchDate": "2007-12-25","satlat": 20.4481,"satlng": -126.9559,"satalt": 19169.5837},{"satid": 40001,"satname": "COSMOS 2500 (GLONASS)","intDesignator": "2014-032A","launchDate": "2014-06-14","satlat": 34.9509,"satlng": -156.1695,"satalt": 19144.3849},{"satid": 41554,"satname": "COSMOS 2516 (GLONASS)","intDesignator": "2016-032A","launchDate": "2016-05-29","satlat": 33.934,"satlng": -136.7727,"satalt": 19116.1912}]}

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
API_KEY = os.getenv('API_KEY')
MY_LAT = os.getenv('MY_LAT')
MY_LONG = os.getenv('MY_LONG')
MY_ALT = os.getenv('MY_ALT')
BASE_URL = os.getenv('API_URL')

SATELLITE_CATEGORIES = {
    "Yaogan" : 36,
    "Beidao" : 35, 
    "Glonasss Operational" : 21
}

# dictionary mapping category to data from API call

# USING MOCK DATA GIVEN API REQUEST CONSTRAINTS

# overhead_satellites = {}
# # for cat_name, cat_id in SATELLITE_CATEGORIES.items():
# #     response = requests.get(f"{BASE_URL}{MY_LAT}/{MY_LONG}/{MY_ALT}/45/{cat_id}/&apiKey={API_KEY}")
# #     data = response.json()
# #     if data["info"]["satcount"] > 0:
# #         overhead_satellites[cat_name] = data["above"]
            
# # output = display_satellites(overhead_satellites)

# # with open(f"data_log/overhead_satellites_{timestamp}.txt", "w") as f:

# #     f.write(f"Time: {timestamp}\nLat: {MY_LAT}\nLong: {MY_LONG}\n{output}")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message" : "Welcome to my Satellite Tracker!"}

@app.get("/satellites")
async def get_satellites():
    return MOCK_SATELLITES