from dotenv import load_dotenv
load_dotenv()
import requests

class DataManager:
    def __init__(self,price_sheet_url, user_sheet_url, username, password):
        self.price_sheet_url = price_sheet_url
        self.user_sheet_url = user_sheet_url
        self.username = username
        self.password = password


    def get_data(self):# when called, it fetches the sheets data
        response = requests.get(self.price_sheet_url, auth= (self.username, self.password))
        result = response.json()
        prices = result["prices"]
        return prices

    def get_customers(self): #when called, it fetches the forms response
        response = requests.get(self.user_sheet_url, auth=(self.username, self.password))
        result = response.json()
        users = result["users"]
        return users

    def update_lowest_price(self, row_id, new_price, current_price):
        print("update function called")

        if int(new_price) < int(current_price):

                new_data = {
                    "price":{
                        "lowestPrice": new_price
                    }
                }

                print("sending:", new_data)

                response = requests.put(url=f"{self.price_sheet_url}/{row_id}",
                             json= new_data,
                             auth=(self.username, self.password)
                           )
                print("status:", response.status_code)

                print("response:", response.text)

    #This class is responsible for talking to the Google Sheet.
