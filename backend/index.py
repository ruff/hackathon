from flask import Flask
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    ret = {}
    return json.dumps(ret)




if __name__ == "__main__":
    app.run(debug=True)
