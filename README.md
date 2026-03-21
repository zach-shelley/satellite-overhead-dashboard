## Project Name
Chinese and Russian Satellite Overhead Tracker

## Purpose
I am an active duty officer in the Space Force and wanted to combine my work experience with my aspiration to strengthen my software development ability to create the framework for a small-scale monitoring dashboard. I used publically available information to create a Chinese/Russian satellite tracking service over a specified location + altitude. The location and altitude are passed in as .env variables, but can be determined depending on the area of interest. 

## Technologies
Python, N2YO API, requests, python-dotenv

## Installation
pip install requests python-dotenv

## Setup
1. Get API key from n2yo.com
2. Create .env file with:
   - API_KEY=your_key_here
   - MY_LAT=your_latitude
   - MY_LONG=your_longitude
   - MY_ALT=your_altitude
   - API_URL=https://api.n2yo.com/rest/v1/satellite/above/

## Usage
python main.py

## V1 Output

===== Satellites Flying Overhead =====

Satellite Category: Beidao

Satellite ID: 34779
Satellite Name: BEIDOU G2
Satellite Launch Date: 2009-04-14
Latitude: 7.989
Longitude: -96.5269
Altitude: 38183.2283


Satellite ID: 40749
Satellite Name: BEIDOU-3 M2
Satellite Launch Date: 2015-07-25
Latitude: 54.295
Longitude: -135.9019
Altitude: 21528.5885

## Add V2 Section

- FastAPI backend with basic web interface
- Note: Using mock data (API rate limits), V3 will integrate Space-Track data
