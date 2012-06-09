import httplib
import demjson

def pull_maps(saddr, daddr):
    conn = httplib.HTTPConnection("maps.google.com")
    params = 
    {
        "saddr": saddr,
        "daddr": daddr,
        "dirflg": "r"
        "ttype": "now"
        "noexp": 0
        "noal": 0
        "sort": "def"
        "mra": "ltm"
        "t": "m"
        "z": 13
        "start": 0
        "output":"json"
    }
    conn.request("GET", "/maps?%s" % urllib.urlencode(params)
    r = conn.getresponse().read()
    def removeNonAscii(s): return "".join(filter(lambda x: ord(x)<128, s))
    r_fixed = removeNonAscii(r[9:]) # remove TM chars, remove front while(1);
    js = demjson.decode(r_fixed)
    time_idx = js['panel'].find(" mins")
    
    return {}
