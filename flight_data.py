import requests
from datamanager import DataManager
import json

class FlightData:
    def __init__(self, token, name):
        self.find_cheapest_flight(token,name)
        self.lowest_price = 0

    def find_cheapest_flight(self, token, name):
        data = DataManager(name)
        city_go = data.city_go
        city_arrive = data.city_arrive
        from_iata = data.from_iata
        stops = data.nonstop
        to_iata = data.to_iata
        start_str = data.going_date
        end_str = data.arrival_date

        FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        headers = {
            "Authorization": f"Bearer {token}"
        }
        
        try:
            response = self.response(to_iata, from_iata, start_str, end_str, FLIGHT_ENDPOINT, headers, stops)
            self.step_over(response)
            print(f"Getting flights from {city_go.upper()}...TO...{city_arrive.upper()}: £{self.lowest_price}")

        except ValueError as error:
            print(f"Getting flights from {city_go.upper()}...TO...{city_arrive.upper()}\nNO DIRECT FLIGHTS FOUND: {error}")
            try:
                response = self.response(to_iata, from_iata, start_str, end_str, FLIGHT_ENDPOINT, headers, "false")
                self.step_over(response)
                print(f"Cheapest indirect flight price is: £{self.lowest_price}")
            except ValueError as error:
                print(f"Still no flights found from {city_go.upper()}...TO...{city_arrive.upper()}. Reason: {error}")

    def response(self, to_iata, from_iata, start_str, end_str, FLIGHT_ENDPOINT,headers,stops):
        parameters = {
            "originLocationCode": from_iata,
            "destinationLocationCode": to_iata,
            "departureDate": start_str,
            "returnDate": end_str,
            "adults": 1,
            "nonStop": stops,
            "currencyCode": "GBP"
        }

        response = requests.get(url=FLIGHT_ENDPOINT, params=parameters, headers=headers)

        if response.status_code != 200:
            raise ValueError(f"API error: {response.status_code} - {response.text}")

        data = response.json().get("data", [])

        if not data:
            raise ValueError("No flight data returned.")

        return data

    def step_over(self, req):
        departure_airport_code = req[0]["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        arrival_airport_code = req[0]["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
        outbound_date = req[0]["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
        inbound_date = req[0]["itineraries"][1]["segments"][0]["arrival"]["at"].split("T")[0]
        lowest_price = float(req[0]["price"]["total"])

        for flight in req:
            current_price = float(flight["price"]["total"])
            if current_price < lowest_price:
                lowest_price = current_price
                departure_airport_code = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                arrival_airport_code = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                outbound_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                inbound_date = flight["itineraries"][1]["segments"][0]["arrival"]["at"].split("T")[0]

        self.lowest_price = lowest_price

        flight_data = {
            "lowest_price":lowest_price,
            "departure_airport_code" : departure_airport_code,
            "arrival_airport_code": arrival_airport_code,
            "outbound_date":outbound_date,
            "inbound_date":inbound_date
        }

        with open("flight_data.json", "w") as file:
            json.dump(flight_data, file, indent=4)
