import http.client
import mimetypes
import json

def key(host, id):
    conn = http.client.HTTPSConnection("web.skola24.se")
    payload = "{\"signature\":\""+str(host)+"\"}"
    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Scope': '8a22163c-8662-4535-9050-bc5e1923df48',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Content-Type': 'application/json',
    'Cookie': 'ASP.NET_SessionId=pnickrx020cskna3goqfsr5f'
    }
    conn.request("POST", "/api/encrypt/signature", payload, headers)
    res = conn.getresponse()
    data = res.read()
    myjson = json.loads(data.decode("utf-8"))
    #print(myjson)
    return(myjson["data"]["signature"])
