# 9 - textmagic 
# pip install textmagic
# https://www.textmagic.com/docs/api/python/
# https://www.textmagic.com/docs/api/
import requests,json


def textmagicApiSMSGateway(data_packet):  
    from textmagic.rest import TextmagicRestClient
    username = data_packet["credentials"]['username']
    token =  data_packet["credentials"]['token'] 
    data = { 
        'from':data_packet['message_title'],
        'phones': data_packet['receiver'],
        'text': data_packet['message_body'],
    }
    from urllib.parse import urlencode
    url = 'https://rest.textmagic.com/api/v2/messages'
    headers =  {
        'User-agent': 'textmagic-python/2.0.3 (Python 3.8.0)',
        'Accept-Charset': 'utf-8',
        'Accept-Language': 'en-us',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'X-TM-Username': username,
        'X-TM-Key': token, 
    }
    response = requests.post(url,headers=headers,data=urlencode(data))
    response = response.json()
    
    

credentials = {
    "username": "jasonwilliams7"  ,
    "token": "mcTabkx1huVwflsJUjT5bmheaTF1aA"  
}
# +13167815639 
data_packet = {
    "credentials":credentials,
    "receiver":"+447747344526",
    "message_title":"Stick alert",
    "message_body":"textmagicApiSMSGateway Message Alert",
}
res = textmagicApiSMSGateway(data_packet=data_packet)



# create_instance -> uri =  https://rest.textmagic.com/api/v2/messages
# create_instance -> data =  {'phones': '447826926850,447826926850', 'text': 'TEST'}


# method =  POST
# url =  https://rest.textmagic.com/api/v2/messages
# params =  None
# data =  {'phones': '447826926850,447826926850', 'text': 'TEST'}
# headers =  {'User-agent': 'textmagic-python/2.0.3 (Python 3.8.0)', 'Accept-Charset': 'utf-8', 'Accept-Language': 'en-us', 'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json', 'X-TM-Username': 'jasonwilliams7', 'X-TM-Key': 'mcTabkx1huVwflsJUjT5bmheaTF1aA'}
# auth =  ('jasonwilliams7', 'mcTabkx1huVwflsJUjT5bmheaTF1aA')