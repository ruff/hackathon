from flask import Flask
import json
import jsonpickle

from transscrapper.structure import Response,Request

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def get_data():
    request = Request()
    
    request.start_address = request.form['start_address']
    request.destination_address = request.form['destination_address']
    request.number_people = 3
    request.car_make = 'WMB'
    request.car_model = '5X'
    
    response = Response()
    return jsonpickle.encode(response)

if __name__ == "__main__":
    app.run(debug=True)
