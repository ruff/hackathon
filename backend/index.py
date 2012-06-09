from flask import Flask
import json
import demjson
import httplib

app = Flask(__name__)

def pull_maps(saddr, daddr):
    conn = httplib.HTTPConnection("maps.google.com")
    conn.request("GET", "/maps?saddr=%s&daddr=%s&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=13&start=0&output=json")
    r = conn.getresponse().read()
    def removeNonAscii(s): return "".join(filter(lambda x: ord(x)<128, s))
    r_fixed = removeNonAscii(r[9:]) # remove TM chars, remove front while(1);
    js = demjson.decode(r_fixed)




    



@app.route("/", methods=['GET'])
def hello():
    ret = {}
    return json.dumps(ret)




if __name__ == "__main__":
    app.run(debug=True)
