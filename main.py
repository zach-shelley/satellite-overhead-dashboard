import os
import requests 
from dotenv import load_dotenv
from output_aggregation import display_satellites
from datetime import datetime

load_dotenv()

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

overhead_satellites = {}
for cat_name, cat_id in SATELLITE_CATEGORIES.items():
    response = requests.get(f"{BASE_URL}{MY_LAT}/{MY_LONG}/{MY_ALT}/45/{cat_id}/&apiKey={API_KEY}")
    data = response.json()
    if data["info"]["satcount"] > 0:
        overhead_satellites[cat_name] = data["above"]
            
output = display_satellites(overhead_satellites)
print(output)

with open(f"data_log/overhead_satellites_{timestamp}.txt", "w") as f:

    f.write(f"Time: {timestamp}\nLat: {MY_LAT}\nLong: {MY_LONG}\n{output}")
