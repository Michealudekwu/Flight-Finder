import json

class DataManager:
    def __init__(self, name):
        with open(file="data.json") as data:
            content = json.load(data)

        self.city_go = content[name]["from_city"]
        self.city_arrive = content[name]["to_city"]
        self.to_iata = content[name]["to_iata"]
        self.from_iata = content[name]["from_iata"]
        self.nonstop = content[name]["nonstop"]
        self.going_date = content[name]["going_date"]
        self.arrival_date = content[name]["arrival_date"]