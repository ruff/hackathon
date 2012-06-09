class Response:
   'Response'
   def __init__(self):
       self.start_address = '2900 West Plano Parkway Plano, Texas 75075'
       self.destination_address = '2900 West Plano Parkway Plano, Texas 75075'
       self.mpg = 16
       self.fuel_cost = 1756
       self.landmarks =["DMA", "Nasher"]
       self.parking_price = 5
       self.drive_time = 50
       self.transit_time = 60
       self.weather_condition = '101 F, 20% chance of rain'
       self.drive_co2 = 5
       self.transit_price = 400


class Parsed_Request :
    'Request'
    def __init__(self):
        self.start_address = "2900 West Plano Parkway Plano, Texas 75075"
        self.destination_address = "2900 West Plano Parkway Plano, Texas 75075"
        self.number_people = 3
        self.car_make = "WMB"
        self.car_model = "5X"
