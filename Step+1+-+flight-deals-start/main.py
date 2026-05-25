from dotenv import load_dotenv
load_dotenv() # Helps load environment variables
import os # access env variables
import requests_cache # stores API responses to avoid repeated calls

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import  NotificationManager

api_key = os.getenv("SERP_API_KEY")  # pulls secrets from .env
username = os.getenv("SHEET_USERNAME")
password = os.getenv("PASSWORD")
price_sheet_url = os.getenv("PRICE_SHEET_URL")
user_sheet_url = os.getenv("USER_SHEET_URL")



requests_cache.install_cache("flight_cache",expire_after= 3600)

data_manager = DataManager(price_sheet_url, user_sheet_url,username,password) # creates object to interact with Google sheets
sheet_data = data_manager.get_data() # fetches all data from Google sheets

customers = data_manager.get_customers() # fetches all data from the form response


flight_search = FlightSearch(api_key=api_key) # creates flight object to call flight API
result =flight_search.search_flights("ABV")  # creates flight API and get raw json data
print(result)

notification_manager = NotificationManager()
for city  in sheet_data: # loops through each city  in GOOgle sheets

    destination_code =city["iataCode"]
    sheet_price = city["lowestPrice"]  # gets current saved price and row id for update
    row_id = city["id"]

    result = flight_search.search_flights(destination_code)


    cheapest_flight = find_cheapest_flight(data=result, return_date="2026-06-30")#extracts cheapest flight from API data

    if cheapest_flight is None:
        print(f"No flight found for {destination_code}")
        continue

    data_manager.update_lowest_price(row_id= row_id, new_price=  cheapest_flight.price, current_price= city["lowestPrice"] ) # update sheets if new flight price is cheaper

    message = (f""
               f"Low Price Alert! "
               f"Route: {destination_code}\n"
               f"Price: {cheapest_flight.price}\n"
               f"Departure: {cheapest_flight.out_date}\n"
               f"Return: {cheapest_flight.return_date}")

    for customer in customers: # loops through all the customer's list and sends email to all of them

        email= customer["whatIsYourEmail?"]

        if "@" not in email or "." not in email:#checks for valid email to avoid crashing the system
            print("Invalid email skipped")
            continue
        notification_manager.send_email(message, recipient_email=email)

    print(f"{destination_code}: {cheapest_flight.price}")






