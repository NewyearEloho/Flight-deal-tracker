class FlightData:  #This class is responsible for structuring the flight data.
    def __init__(self, price,origin_airport, destination_airport, out_date, return_date): # stores flight details
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date



def find_cheapest_flight( data, return_date): # function to find  the cheapest flight from API data
    if not data or "other_flights" not in data:  # 1. handles empty data
        return None

    flights = data["other_flights"] # get list of available flights
    if len(flights) == 0:
        return None


    all_flights = data.get("other_flights")

    first_flight = None

    for flight in all_flights:
        if "price" in flight:
            first_flight = flight
            break

    if first_flight is None:
        return None

    lowest_price = first_flight["price"]
    origin = first_flight["flights"][0]["departure_airport"]["id"]
    destination = first_flight["flights"][-1]["arrival_airport"]["id"]
    out_date = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]

    # first_flight = all_flights[0]
    # lowest_price = first_flight["price"]
    # origin = first_flight["flights"][0]["departure_airport"]["id"]
    # destination = first_flight["flights"][-1]["arrival_airport"]["id"]
    # out_date = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]


    cheapest_flight = FlightData(lowest_price, origin, destination,out_date, return_date)


    for flights in all_flights: # loops through all flights to compare prices
        try:
            price = flights["price"]
        except KeyError:
            print("--- No price available for flight. ---")
            continue
        if price < lowest_price: # compares prices, checks if current price is cheaper
            lowest_price = price
            origin = flights["flights"][0]["departure_airport"]["id"]
            destination = flights["flights"][-1]["arrival_airport"]["id"]
            out_date = flights["flights"][0]["departure_airport"]["time"].split(" ")[0]

            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date) #stores new cheapest price update cheapest flight object
            print(f"Lowest price to {destination} is GBP {lowest_price}")


    return cheapest_flight


