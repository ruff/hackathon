import httplib
import demjson
import urllib

def pull_miles_and_time(saddr, daddr):
    conn = httplib.HTTPConnection("maps.googleapis.com")
    params = {
        "origin": saddr,
        "destination": daddr,
        "sensor": "false"
    }
    conn.request("GET", "/maps/api/directions/json?%s" % urllib.urlencode(params))
    r = conn.getresponse().read()
    js = demjson.decode(r)
    distance_meters = js['routes'][0]['legs'][0]['distance']['value']
    distance_miles = distance_meters / 1609
    time_seconds = js['routes'][0]['legs'][0]['duration']['value']
    return (distance_miles, time_seconds)

