import httplib
import demjson
import urllib

def pull_car_miles_and_time(request):
    conn = httplib.HTTPConnection("maps.googleapis.com")
    params = {
        "origin": request.start_address,
        "destination": request.destination_address,
        "sensor": "false"
    }
    conn.request("GET", "/maps/api/directions/json?%s" % urllib.urlencode(params))
    r = conn.getresponse().read()
    js = demjson.decode(r)
    distance_meters = js['routes'][0]['legs'][0]['distance']['value']
    distance_miles = distance_meters / 1609
    time_seconds = js['routes'][0]['legs'][0]['duration']['value']
    return (distance_miles, time_seconds)


def pull_bus_transit_time(request):
    conn = httplib.HTTPConnection("maps.google.com")
    params = {
        "saddr": request.start_address,
        "daddr": request.destination_address,
        "dirflg": "r",
        "ttype": "now",
        "noexp": 0,
        "noal": 0,
        "sort": "def",
        "mra": "ltm",
        "t": "m",
        "z": 13,
        "start": 0,
        "output":"json"
    }
    conn.request("GET", "/maps?%s" % urllib.urlencode(params))
    r = conn.getresponse().read()
    def removeNonAscii(s): return "".join(filter(lambda x: ord(x)<128, s))
    r_fixed = removeNonAscii(r[9:]) # remove TM chars, remove front while(1);
    js = demjson.decode(r_fixed)
    time_idx = js['panel'].find(" mins")
    i = time_idx - 1
    while (js['panel'][i].isdigit()):
        i = i - 1
    return 60*int(js['panel'][i+1:time_idx]) 