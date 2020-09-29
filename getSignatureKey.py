import requests
import json

def key(ID):
    
    url = "https://web.skola24.se/api/encrypt/signature"

    payload = "{\r\n    \"signature\": \""+ str(ID) +" \"\r\n}"
    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Scope': '8a22163c-8662-4535-9050-bc5e1923df48',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Content-Type': 'application/json',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Cookie': 'ASP.NET_SessionId=ymxtq4psjnefu3wd0ok2ybf4'
    }

    response = requests.request("POST", url, headers=headers, data = payload).json()
    return(response['data']['signature'])

