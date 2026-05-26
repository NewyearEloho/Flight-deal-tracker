import os
from dotenv import load_dotenv

load_dotenv()
import requests

SERP_API_URL = os.getenv("SERP_API_URL")# API endpoint for flight search

class FlightSearch: #This class is responsible for talking to the Flight Search API.
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = SERP_API_URL

    def search_flights(self,arrival_airport):# function to fetch flight data from api
        params = {    # parameters sent to API request
            "engine": "google_flights",
            "departure_id": "PHC",
            "arrival_id": arrival_airport,
            "currency": "USD",
            "outbound_date": "2026-05-30",
            "return_date": "2026-06-30",
            "api_key": self.api_key,
            "stops": 0,
        }


        response = requests.get(self.url,params=params ) # sends requests to flight API
        result = response.json()
        if "other_flights" not in result:
            print("No direct flights found. searching stopover flights")
            params["stops"] = 1
            response = requests.get(self.url, params = params)
            result = response.json()


        return result # returns JSON data to main.py


