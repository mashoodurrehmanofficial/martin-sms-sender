import base64
credentials = {
    "username": "andrew@uniteflooringltd.com",
    "api_key": "D349CEC9-EDEE-133A-CAC8-76AD726D66CE",
}

authHeader = 'Basic ' + base64.b64encode(( "andrew@uniteflooringltd.com:Stealth017???"   ).encode('utf-8')).decode('utf-8')


print(authHeader)
print(base64.b64decode("YW5kcmV3QHVuaXRlZmxvb3JpbmdsdGQuY29tOlN0ZWFsdGgwMTc/Pz8=").decode("utf-8"))
import requests

headers = {
    'Authorization': 'Basic YW5kcmV3QHVuaXRlZmxvb3JpbmdsdGQuY29tOlN0ZWFsdGgwMTc/Pz8=',
    # 'Content-Type': 'application/x-www-form-urlencoded',
    "Content-Type": "application/json",
}

# data = 'username=myusername&key=1234-I3U2RN34IU-43UNG&to=61411111111,64122222222,61433333333&senderid=example&message=testing'


data = {
    "username": "andrew@uniteflooringltd.com",
    "key": "D349CEC9-EDEE-133A-CAC8-76AD726D66CE",
    "to": ["+923167815639"],
    "senderid":"example",
    "message":"testing"
}

response = requests.post('https://api-mapper.clicksend.com/http/v2/send.php', headers=headers, data=data)


print(response.text)