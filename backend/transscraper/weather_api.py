import httplib
import demjson
import urllib

def weather_as_string(request):
    destionation_address = request.destination_address;

    conn = httplib.HTTPConnection("weather.yahooapis.com")
    conn.request("GET", "/forecastjson?w=2388929") # dallas "code"
    r = conn.getresponse().read()
    js = demjson.decode(r)
    cond = js['forecast'][0]['condition']
    h = js['forecast'][0]['high_temperature']
    l = js['forecast'][0]['low_temperature']
    return "%s H %s L %s" % (cond, h, l)

