class Response:
   'Response'
   def __init__(self):
       self.saddr = 'Start address'
       self.daddr = 'End address'
       self.mpg = 16
       self.fuel_cost = 1756
       self.landmarks =["DMA", "Nasher", "etc"]
       self.parking_price = 5
       self.drive_time = 50
       self.transit_time = 60
       self.weather_condition = '101 F 20% chance of rain'
       self.drive_co2 = 5
       self.transit_price = 400


class Resquest :
    'Request'
    def __init__(self):
        self.saddr = "Start Address"
        self.daddr = "End Address"
        self.numpeople = 3
        self.carmake = "WMB"
        self.carmodel = "5X"
