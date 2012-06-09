import httplib
import demjson
import urllib

def pull_gas_price():
    conn = httplib.HTTPConnection("dallasgasprices.com")
    conn.request("GET", "/")
    r = conn.getresponse().read()
    i = r.find("Dallas Avg")
    s = r[i:i+100]
    j = s.find("<h2>")
    e = s.find("</h2>")
    return int(float(s[j+4:e])*100)
