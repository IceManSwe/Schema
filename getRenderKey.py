import http.client
import mimetypes
import json
def renderKey(host):
    conn = http.client.HTTPSConnection("web.skola24.se")
    payload = "null"
    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Scope': '8a22163c-8662-4535-9050-bc5e1923df48',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Content-Type': 'application/json'
    }
    conn.request("POST", "/api/get/timetable/render/key", payload, headers)
    res = conn.getresponse()
    data = res.read()
    myjson = json.loads(data.decode("utf-8"))
    print("rkey: "+ myjson["data"]["key"])
    return(myjson["data"]["key"])