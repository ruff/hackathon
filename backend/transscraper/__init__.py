from flask import Flask
import json
import jsonpickle
from flask import request


from transscraper.structure import Response,Parsed_Request
from transscraper.map_api import pull_car_miles_and_time,pull_bus_transit_time 
from transscraper.gas_scrape import pull_gas_price

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

    response.fuel_cost = pull_gas_price()
    response.transit_time = pull_bus_transit_time(parsed_request);

    (car_miles, response.drive_time) = pull_car_miles_and_time(parsed_request);
    response.landmarks =["DMA", "Nasher"]
    response.parking_price = 5
    response.weather_condition = '101 F, 20% chance of rain'
    response.drive_co2 = 5
    response.transit_price = 400

    return jsonpickle.encode(response)


@app.route("/get_request_sample", methods=['GET','POST'])
def get_request_sample():
    parsed_request = Parsed_Request()
    return jsonpickle.encode(parsed_request)


if __name__ == "__main__":
    app.run(debug=True)
