import httplib
import demjson
import urllib

def geocode(addr):
    conn = httplib.HTTPConnection("maps.googleapis.com")
    params = {
        "address": addr,
        "sensor": "false"
    }
    conn.request("GET", "/maps/api/geocode/json?%s" % urllib.urlencode(params))
    r = conn.getresponse().read()
    js = demjson.decode(r)
    loc = js['results'][0]['geometry']['location']
    return "%f,%f" % (loc['lat'], loc['lng'])

def pull_parking_cost(request):
    gc = geocode(request.destination_address)

    conn = httplib.HTTPSConnection("maps.googleapis.com")
    params = {
        "key": "AIzaSyCS2F_UYmpRzCRhHv4aT7pBdaWRqvA42U8",
        "location": gc,
        "radius": 4000,
        "sensor": "false",
        "keyword": "parking lot"
    }
    rs = "/maps/api/place/search/json?%s" % urllib.urlencode(params)
    print rs
    conn.request("GET", rs)
    r = conn.getresponse().read()
    js = demjson.decode(r)

    if (len(js['results']) > 5):
        return 5
    else:
        return 0
    
