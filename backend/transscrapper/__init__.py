from flask import Flask
import json
import jsonpickle

from transscrapper.structure import Response

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    test = Response()
    return jsonpickle.encode(test)

if __name__ == "__main__":
    app.run(debug=True)
