
import sys,json
from urllib.parse import urlencode
import requests 
def d7networksApiSMSGateway(data_packet):   
    headers = {
        'Authorization': 'Basic Zm9vOmJhcg==',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        "to":data_packet['receiver'],
        "from": data_packet['message_title'],
        "content": data_packet['message_body'] ,
        "dlr":"yes",
        "dlr-url":"http://192.168.202.54/dlr_receiver.php",
        "dlr-level": 3,
    }  
    response = requests.post('https://rest-api.d7networks.com/secure/sendbatch', headers=headers, data=json.dumps(data))
    print(response.text)
    
credentials = {   
    "username": "",  
    "password": "",  
}
# +13167815639 
data_packet = {
    "credentials":credentials,
    "receiver":"+923167815639",
    "message_title":"Stick alert",
    "message_body":"d7networksApiSMSGateway Body",
}

d7networksApiSMSGateway(data_packet=data_packet)