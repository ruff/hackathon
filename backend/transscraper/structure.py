class Response:
   'Response'
   def __init__(self):
       self.start_address = ''
       self.destination_address = ''
       self.mpg = -1
       self.fuel_cost = -1
       self.landmarks =[]
       self.parking_price = -1
       self.drive_time = -1
       self.transit_time = -1
       self.weather_condition = ''
       self.drive_co2 = -1
       self.transit_price = -1


class Parsed_Request :
    'Request'
    def __init__(self):
        self.start_address = "2900 West Plano Parkway Plano, Texas 75075"
        self.destination_address = "2900 West Plano Parkway Plano, Texas 75075"
        self.number_people = 3
        self.car_make = "WMB"
        self.car_model = "5X"
