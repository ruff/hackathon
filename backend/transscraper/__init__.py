from flask import Flask
import json
import jsonpickle
from flask import request


from transscraper.structure import Response,Parsed_Request
from transscraper.map_api import pull_car_miles_and_time,pull_bus_transit_time 
from transscraper.gas_api import pull_gas_price
from transscraper.weather_api import weather_as_string
from transscraper.parking_api import pull_parking_cost
from transscraper.mpg_api import find_mpg


app = Flask(__name__)

@app.route("/api", methods=['GET','POST'])
def api():
    parsed_request = Parsed_Request()
    
    if request.method == 'POST':
        parsed_request.start_address = request.form['start_address']
        parsed_request.destination_address = request.form['destination_address']
        parsed_request.number_people = request.form['number_people']
        parsed_request.car_make = request.form['car_make']
        parsed_request.car_model = request.form['car_model']
    elif request.method == 'GET':
        parsed_request.start_address = request.args.get('start_address', '')
        parsed_request.destination_address = request.args.get('destination_address', '')
        parsed_request.number_people = request.args.get('number_people', '')
        parsed_request.car_make = request.args.get('car_make', '')
        parsed_request.car_model = request.args.get('car_model', '')

    response = Response()
    response.start_address = parsed_request.start_address
    response.destination_address = parsed_request.destination_address

    price_per_gallon = pull_gas_price(parsed_request)
    response.transit_time = pull_bus_transit_time(parsed_request)
    response.weather_condition = weather_as_string(parsed_request)
    (car_miles, response.drive_time) = pull_car_miles_and_time(parsed_request)
    response.parking_price = pull_parking_cost(parsed_request)
    
    mpg = find_mpg(parsed_request)
    
    gallons = float(car_miles) / float(mpg)
    
    car_miles = car_miles * 2
    
    response.gallons = gallons
    response.mpg = mpg
    response.fuel_cost = gallons * price_per_gallon / 100
    response.drive_co2 = gallons * 19  
    
    response.landmarks =["Museum", "Big Central Park"]
    response.transit_price = 4
    
    response.drive_time = float(response.drive_time) / float(60)
    response.transit_time = float(response.transit_time) / float(60)
    
    response.savings = float(response.fuel_cost) + float(response.parking_price) - float(parsed_request.number_people) * float(response.transit_price);
    
    return jsonpickle.encode(response)


@app.route("/get_request_sample", methods=['GET','POST'])
def get_request_sample():
    parsed_request = Parsed_Request()
    return jsonpickle.encode(parsed_request)


if __name__ == "__main__":
    app.run(debug=True)
