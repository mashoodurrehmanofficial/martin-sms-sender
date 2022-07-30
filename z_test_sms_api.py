# #cell 0
# import json,requests,sys,re,http
# from requests.auth import HTTPBasicAuth

# #cell 1
# detected_macros = "##TestAlert##! Go sir to ##LINK## "
# detected_macros = [max(x.split("##"),key=len) for x in detected_macros.split() if str(x).count("#")==4]
# # detected_macros = [x for x in ]

# print(detected_macros)
 

# #cell 2
# key = "7689c474-0275-4a68-94f4-ac0f4652f7fd"
# # url = f'http://localhost:8000/api/verifyProductKey/{key}'
# url = f'https://martin12345.pythonanywhere.com/api/verifyProductKey/{key}'
# response = requests.get(url).json()

# response





# #cell 6
# # 9 - dotdigital
# # dotdigital.com - API: email - apiuser-e85f6ce92957@apiconnector.com | Endpoint - https://r1-api.dotdigital.com 
# # https://developer.dotdigital.com/reference/send-sms-message

# def dotdigitalApiSMSGateway(data_packet): 
    
#     import requests

#     url = "https://region-api.dotdigital.com/v2/sms-messages/send-to/447626691255"

#     headers = {
#         "Accept": "application/json",
#         "Authorization": "Basic hps2cJEizqQebavvGmOm182JQHj12igZOOSrYWQNDhse9c", 
#         "Content-Type": "application/json"
#     }

#     response = requests.post(url, headers=headers)

#     print(response.text)
    

# credentials = {
#     "key": "hps2cJEizqQebavvGmOm182JQHj12igZOOSrYWQNDhse9c"  
# }
# # +13167815639 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"+447826926850",
#     "message_title":"Stick alert",
#     "message_body":"dotdigital Message Alert",
# }
# # res = dotdigitalApiSMSGateway(data_packet=data_packet)



# import http.client
# from base64 import b64encode
# import json

# print("")
# print("Sending SMS using Dotdigital Omnichannel and Python")
# print("---------------------------------------------------")

# # Your Dotdigital API user credentials
# API_USERNAME = "YOUR API USERNAME"
# API_PASSWORD = "YOUR API PASSWORD"

# # Setup the http connection
# conn = http.client.HTTPSConnection("api-cpaas.dotdigital.com")

# # Create the basic auth header encoded username and password
# userAndPass = b64encode(bytes(API_USERNAME + ":" + API_PASSWORD, "ascii")).decode("ascii")

# # Construct the Dotdigital Omnichannel API request
# myRequest = {
#     "to": {
#         "phoneNumber": "447826926850"
#     },
#     "body": "This is an SMS via Dotdigital Omnichannel \"One\" API",    
#     "rules": ["sms"]
# }

# print("")
# print("Request JSON: ")
# print(json.dumps(myRequest, indent=2))

# # Setup the http headers with basic auth
# headers = {
#     'authorization' : 'Basic %s' %  userAndPass,
#     'content-type': "application/json",
#     'cache-control': "no-cache"
# }

# # Make the webservice request
# print("")
# print("Calling Dotdigital Omnichannel...")
# conn.request("POST", "/cpaas/messages", json.dumps(myRequest), headers)

# res = conn.getresponse()
# data = res.read()

# print("")
# print("Call returned status code: " + str(res.status))
# print(json.dumps(json.loads(data.decode("utf-8")), indent=2)) # Pretty print the JSON
# print("")







# #cell 9
 
# # 9 - smsbroadcast   
# def smsbroadcastApiSMSGateway(data_packet):     
#     url = "https://api.smsbroadcast.co.uk/api-adv.php?username=JasonW22&password=Stealth017???&to=07000111222,07000222333&from=MyCompany& message=Hello%20World"
#     # url = "https://api.smsbroadcast.co.uk/api-adv.php?username=JasonW22&password=Stealth017???&to=03167815639&from=MyCompany& message=Hello%20World"
#     message = "smsbroadcastApiSMSGateway Message Alert" 
 
#     response = requests.get(url)
    

#     print(response.text)

# credentials = {
#     "username": "JasonW22"  ,
#     "token": "Stealth017???"  
# }
# # +13167815639 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"+923167815639",
#     "message_title":"Stick alert",
#     "message_body":"burstsmsApiSMSGateway Message Alert",
# }
# res = smsbroadcastApiSMSGateway(data_packet=data_packet)



# #cell 10
# # 9 - octopush   
# # octopush.com - API: login - jason.williams@greenhousepeople.co.uk | key - EG0eYNVFnMHq69fvkXIuxJDdpTZ27BwQ 
# # pip install octopush
# # https://github.com/octopush/octopush-sms-python

# def octopushApiSMSGateway(data_packet):     
#     import octopush
#     from octopush import SMS

#     import datetime

#     config = {
#         'user_login': 'jason.williams@greenhousepeople.co.uk',
#         'api_key': "EG0eYNVFnMHq69fvkXIuxJDdpTZ27BwQ",
#         'sms_recipients': ['+923167815639'],
#         'sms_text': 'test text ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
#         'sms_type': octopush.SMS_WORLD,
#         'sms_sender': 'onesender'
#     }
    
    
#     import uuid

#     sms = SMS(config['user_login'], config['api_key'])
#     sms.set_sms_text(config['sms_text'])
#     sms.set_sms_recipients(config['sms_recipients'])
#     sms.set_sms_type(config['sms_type'])
#     sms.set_sms_sender(config['sms_sender'])
#     sms.set_sms_request_id(str(uuid.uuid1()))

#     result = sms.send()

#     print(result)

# credentials = {
#     "username": "JasonW22"  ,
#     "token": "Stealth017???"  
# }
# # +13167815639 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"+923167815639",
#     "message_title":"Stick alert",
#     "message_body":"octopush Message Alert",
# }
# res = octopushApiSMSGateway(data_packet=data_packet)


# # from octopush import SMS
# # from config import config

# # sms = SMS(config['user_login'], config['api_key'])

# # result = sms.get_credit()

# # for credit in result.findall('credit'):
# #     print(credit.text)



# #cell 11
# # 9 - melroselabs    
# # melroselabs.com - API: enfTOrAHC1851V34Nn4kY3HTxX1JihXX6XDtbXzV (expires 45 days) 
# # https://melroselabs.com/docs/api/sms/#sms-api
# # 

# def melroselabsApiSMSGateway(data_packet):      
#     headers = {
#     'Content-Type': 'application/json',
#     'Accept': 'application/json',
#     'x-api-key': 'enfTOrAHC1851V34Nn4kY3HTxX1JihXX6XDtbXzV'
#     }
#     params = {
#         "source": "Stick alert",
#         "destination": "+923167815639",
#         "message": "melroselabs Message Alert", 
#     }
#     response = requests.post('https://api.melroselabs.com/sms/message', params=params, headers = headers)

#     print( response.json())
    
    
# credentials = {
#     "x-api-key": "enfTOrAHC1851V34Nn4kY3HTxX1JihXX6XDtbXzV"  , 
# }
# # +13167815639 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"+923167815639",
#     "message_title":"Stick alert",
#     "message_body":"melroselabs Message Alert",
# }
# res = melroselabsApiSMSGateway(data_packet=data_packet)


# #cell 13
# # # 11 - infobip    
# # # infobip.com - API: 23c7a956498ccb3bb68bd40b1180b58d-114c0e72-a36c-40d9-9e41-d90415417a61 

# # # pip install infobip-api-python-client
# # # https://github.com/infobip/infobip-api-python-client#documentation


# # # Configuration
# # # Let's first set the configuration. For that you will need your specific URL. To see your base URL, log in to the Infobip API Resource hub with your Infobip credentials.

# # def infobipApiSMSGateway(data_packet):      
# #     from infobip_api_client.api_client import ApiClient, Configuration
# #     from infobip_api_client import  api_client
    
# #     client_config = Configuration(
# #         host="<YOUR_BASE_URL>",
# #         api_key={"APIKeyHeader": "<YOUR_API_KEY>"},
# #         api_key_prefix={"APIKeyHeader": "<YOUR_API_PREFIX>"},
# #     )
# #     api_client = ApiClient(client_config)
# #     sms_request = SmsAdvancedTextualRequest(
# #         messages=[
# #             SmsTextualMessage(
# #                 destinations=[
# #                     SmsDestination(
# #                         to="41793026727",
# #                     ),
# #                 ],
# #                 _from="InfoSMS",
# #                 text="This is a dummy SMS message sent using Python library",
# #             )
# #         ])
        
# #     api_instance = SendSmsApi(api_client)

# #     api_response: SmsResponse = api_instance.send_sms_message(sms_advanced_textual_request=sms_request)
# #     print(api_response)
    
    
# # credentials = {
# #     "x-api-key": "enfTOrAHC1851V34Nn4kY3HTxX1JihXX6XDtbXzV"  , 
# # } 
# # data_packet = {
# #     "credentials":credentials,
# #     "receiver":"+923167815639",
# #     "message_title":"Stick alert",
# #     "message_body":"infobipApiSMSGateway Message Alert",
# # }
# # res = infobipApiSMSGateway(data_packet=data_packet)



# # https://www.infobip.com/docs/api/channels/sms/sms-messaging/outbound-sms/send-sms-message
# import http.client
# import json

# conn = http.client.HTTPSConnection("{baseUrl}")
# payload = json.dumps({
#     "messages": [
#         {
#             "destinations": [
#                 {
#                     "to": "41793026727"
#                 }
#             ],
#             "from": "InfoSMS",
#             "text": "This is a sample message"
#         }
#     ]
# })
# headers = {
#     'Authorization': '23c7a956498ccb3bb68bd40b1180b58d-114c0e72-a36c-40d9-9e41-d90415417a61',
#     'Content-Type': 'application/json',
#     'Accept': 'application/json'
# }
# conn.request("POST", "/sms/2/text/advanced", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))


# #cell 14
# # 13.
# # spryng.nl - API: Andrew - 3623527287780b8c83085eec0a6272e2a13e9dcb7980a1c82e 
# # https://docs.spryngsms.com/#39c42dee-53ea-4a4f-8f68-74ac844ecd57

# def spryngApiSMSGateway(data_packet):    
#     url = "https://rest.spryngsms.com/v1/messages"

#     payload = json.dumps({
#     "body": "This is a test message.",
#     "encoding": "auto",
#     "originator": "DocsTest",
#     "recipients": [
#         "31612345678"
#     ],
#     "route": "business", 
#     })
#     headers = {
#     'Accept': 'application/json',
#     'Authorization': 'Bearer 3623527287780b8c83085eec0a6272e2a13e9dcb7980a1c82e',
#     'Content-Type': 'application/json'
#     }

#     response = requests.request("POST", url, headers=headers, data=payload)

#     print(response.text)

    
# credentials = {
#     "x-api-key": "enfTOrAHC1851V34Nn4kY3HTxX1JihXX6XDtbXzV"  , 
# } 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"+923167815639",
#     "message_title":"Stick alert",
#     "message_body":"spryngApiSMSGateway Message Alert",
# }
# res = spryngApiSMSGateway(data_packet=data_packet)

# #cell 15
# # 14.
# # esendex.com - Token: New Token  +TpEI0tOPQiccVruJgYQcOw3LI+bvxsWGab4+/c2njw=
# # https://github.com/marramgrass/esendexer/blob/master/esendexer.py 
# def esendexApiSMSGateway(data_packet):    
#     # https://github.com/marramgrass/esendexer/blob/master/esendexer.py
#     # Uses requests library
#     # http://docs.python-requests.org/en/latest/user/install/

#     import requests
#     import base64


#     username = "user@domain.com"
#     password = "password" # Sorry no API keys!
#     accountReference = "EX0123456" # https://www.esendex.com/echo (on the right hand side EX12345)
#     recipient = "447123456789" # Your number
#     message = "Hello world!"


#     authHeader = 'Basic ' + base64.b64encode(("%s:%s" % (username, password)).encode('utf-8')).decode('utf-8')
#     headers = { 'Authorization': authHeader }

#     data = {'accountreference': accountReference, 'messages': [ { "to": recipient, "body": message } ]}

#     r = requests.post("http://api.esendex.com/v1.0/messagedispatcher", headers=headers, json=data)


#     if r.status_code == 200 :
#         print("It worked!")
#     else :
#         print("Something went wrong")
#         print(r.status_code)
#         print(r.text)
    
# credentials = {
#     "x-api-key": "enfTOrAHC1851V34Nn4kY3HTxX1JihXX6XDtbXzV"  , 
# } 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"+923167815639",
#     "message_title":"Stick alert",
#     "message_body":"esendexApiSMSGateway Message Alert",
# }
# res = esendexApiSMSGateway(data_packet=data_packet)

# #cell 16


# #cell 17

# # 17.
# # bsg.world - live_fmUXxusYDiufPlwoZjLJ:5uCqJIml 
# # bsg.world - live_fmUXxusYDiufPlwoZjLJ 
# # https://bsg.world/developers/libraries/
  
# def bsgApiSMSGateway(data_packet):    
#     # import pprint
#     # import bsg_restapi as api
#     # from examples.settings import API_KEY

#     # client = api.SMSAPI(config={'api_key': API_KEY})
#     # result = client.send(message=api.SMSMessage(body='test message text'), recipients=api.Recipient(380967770002))
#     # print('Result of SMS sending:\n{}'.format(pprint.pformat(result)))
#     # # getting status of SMS
#     # status = client.get_status(result['reference'])
#     # print('Current SMS status result for reference {}: \n{}'.format(result['reference'], pprint.pformat(status, indent=4)))
#     ...
#     # use api - folder -> bg.world
 
# credentials = {
#     "x-api-key": "enfTOrAHC1851V34Nn4kY3HTxX1JihXX6XDtbXzV"  , 
# } 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"+923167815639",
#     "message_title":"Stick alert",
#     "message_body":"bsgApiSMSGateway Message Alert",
# }
# res = bsgApiSMSGateway(data_packet=data_packet)
 

# #cell 18
# # 18.
# # skebby.it - API: token - b0eleTUSqJYc5eejm3e7DqTg 
# # https://developers.skebby.it/?python#send-a-parametric-sms-message
 
# def skebbyApiSMSGateway(data_packet):    
#     from requests.auth import HTTPBasicAuth 
#     # Use this when using Session Key authentication
#     headers = { 'user_key': 'USER_KEY', 'Session_key' : 'SESSION_KEY', 'Content-type' : 'application/json' }
#     # When using Access Token authentication, use this instead:
#     # headers = { 'user_key': 'UserParam{user_key}', 'Access_token' : 'UserParam{access_token}', 'Content-type' : 'application/json' }
#     payload = """{
#         "message_type": "MESSAGE_TYPE", 
#         "message": "Hello world!", 
#         "recipient": [
#             "+393471234567", 
#             "+393471234568"
#         ], 
#         "sender": "MySender", 
#         "scheduled_delivery_time": "20161223101010", 
#         "order_id": "123456789", 
#         "returnCredits": true
#     }"""

#     r = requests.post("https://api.skebby.it/API/v1.0/REST/sms", headers=headers, data=payload)

#     if r.status_code != 201:
#         print("Error! http code: " + str(r.status_code) + ", body message: " + str(r.content))
#     else:
#         response = r.text

#         obj = json.loads(response)
#         print(obj)
 
# credentials = {
#     "user_key": ""  , 
#     "SESSION_KEY": ""  , 
# } 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"+923167815639",
#     "message_title":"Stick alert",
#     "message_body":"skebbyApiSMSGateway Message Alert",
# }
# res = skebbyApiSMSGateway(data_packet=data_packet)
 

# #cell 19
# # 19.
# # massenversand.de - authToken= AA801F91FD67040A20DFAFD6135EE03A33C5EAC5 
 
# def massenversandApiSMSGateway(data_packet):    
#     # https://www.massenversand.de/sms-versand-api/
#     # no profper docs
# #     <?php
# # $urlGate="https://gateway";		//API Url
# # $password="password";			//your password
# # $accountid="accountID";			//your accountID
# # $receiver="00491701234567";		//receiver number 
# # $sender="sender";					//sender address
# # $msg="test";						//message, should be urlencoded
 
# # $urlParam="?receiver=" . $receiver . "&sender=" . $sender . "&msg=" . $msg . "&id=" . $accountid . "&pw=" . $password . "&msgtype=c&getID=1";
# # $strUrl=$urlGate . $urlParam;

#     url = 'https://gateway.com?receiver00491701234567=&senderSender=&msg=MessageBody&id=720095168&pw=Stealth017&msgtype=c&getID=1'
    
#     res = requests.get(url)
#     print(res.text)

    
 
# credentials = {
#     "user_key": ""  , 
#     "SESSION_KEY": ""  , 
# } 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"+923167815639",
#     "message_title":"Stick alert",
#     "message_body":"massenversandApiSMSGateway Message Alert",
# }
# res = massenversandApiSMSGateway(data_packet=data_packet)
 

# #cell 20
# # 20.
# # sms.studio - API: cd200ef8e689f089117d22e13a91efcc
# # sms.studio/#features
# def sms_studioApiSMSGateway(data_packet):     
#     import requests

#     # headers = {
#     #     'cache-control': 'no-cache',
#     # }
#     # params = {
#     #     'api_token': 'cd200ef8e689f089117d22e13a91efcc',
#     #     'response_type': 'json',
#     #     'from_name': 'YOUR_NAME_HERE',
#     #     'to': '923167815639',
#     #     'text': 'Hello World',
#     # }
#     # response = requests.post('https://devapi.sms.studio/customer/custom-sms', params=params, headers=headers)
#     # print(response.text)
#     import requests
#     from requests.structures import CaseInsensitiveDict

#     url = "https://devapi.sms.studio/customer/custom-sms?api_token=cd200ef8e689f089117d22e13a91efcc&response_type=json&from_name=YOUR_NAME_HERE&to=380551112233&text=Hello%20World"

#     headers = CaseInsensitiveDict()
#     headers["cache-control"] = "no-cache"
#     headers["Content-Length"] = "0"


#     resp = requests.post(url, headers=headers)

#     print(resp.status_code)
#     print(resp.text)


    
    
 
# credentials = {
#     "user_key": ""  , 
#     "SESSION_KEY": ""  , 
# } 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"+923167815639",
#     "message_title":"Stick alert",
#     "message_body":"sms_studioApiSMSGateway Message Alert",
# }
# res = sms_studioApiSMSGateway(data_packet=data_packet)
 

# #cell 21
# # sinch.com
# def sinchApiSMSGateway(data_packet):
#     service_plan_id = data_packet['credentials']['service_plan_id']
#     url = "https://us.sms.api.sinch.com/xms/v1/" + service_plan_id + "/batches"

#     payload = {
#     "from": data_packet['message_title'],
#     "to": [data_packet['receiver']],
#     "body": data_packet['message_body']
#     }

#     headers = {
#     "Content-Type": "application/json",
#     "Authorization": f"Bearer {data_packet['credentials']['api_token']}"
#     }

#     response = requests.post(url, json=payload, headers=headers)

#     print("response.text = ", response.json())
#     print("response.text = ", response.text)
#     # response = response.json()
#     # if response.get('id') is not None:
#     #     print(f"-> Message sent to {data_packet['receiver']}")
#     #     print(response['id'])
#     # print(data)
    

# # credentials = { 
# #     "service_plan_id":"2dd5491550484034b60bd042df14d851" ,
# #     "api_token":"6f6197107b384b2c8c8cc72a872ae0ae" ,
# # }
# credentials = { 
#     "service_plan_id":"e1ec53130cdc4de7a74267c8e8b21631" ,
#     "api_token":"6cee3e8b6f6247c7bb57a37a5212dc55" ,
# }
# data_packet = {
#     "credentials":credentials,
#     "receiver":"447748347521",
#     "message_body":"This is message from Bot",
#     "message_title":"Alert",
# }
# res = sinchApiSMSGateway(data_packet=data_packet)
# res


# #cell 22
# res

# #cell 23
# # 2 - clicksend.com
# import clicksend_client
# from clicksend_client import SmsMessage
# from clicksend_client.rest import ApiException
 
# def clickSendApiSMSGateway(data_packet): 
#     configuration = clicksend_client.Configuration()
#     configuration.username = data_packet['credentials']['username']
#     configuration.password = data_packet['credentials']['api_key']

#     # create an instance of the API class
#     api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))

#     # If you want to explictly set from, add the key _from to the message.
#     sms_message = SmsMessage(source="php",
#                               _from='Alert',
#                             body=data_packet['message_body'],
#                             to=data_packet['receiver'],
                            
#                             )

#     sms_messages = clicksend_client.SmsMessageCollection(messages=[sms_message])

#     try: 
#         api_response = api_instance.sms_send_post(sms_messages)
#         print(api_response)
#         try:
#             api_response = eval(api_response)
#             if str(api_response.get('http_code')) == str(200) and str(api_response.get('response_code')) == 'SUCCESS' :
#                 print(f"-> Message sent to {data_packet['receiver']}")
#         except:
#             print("Exception when calling SMSApi->sms_send_post: %s\n" % e)
                
            
#     except ApiException as e:
#         print("Exception when calling SMSApi->sms_send_post: %s\n" % e)
        
    
# credentials = {
#     "username": "Roussisphoto@gmail.com",
#     "api_key": "BB4A01B2-4642-C68E-B665-011955262FD5",
# }
# # credentials = {
# #     "username": "mashoodurrehmanofficial@gmail.com",
# #     "api_key": "2A433C52-5859-BD5B-DEA2-6A9E006AD8BA",
# # }


# data_packet = {
#     "credentials":credentials,
#     "receiver":"+923167815639",
#     "message_body":"Message Alert",
# }
# res = clickSendApiSMSGateway(data_packet=data_packet)
    

# #cell 24
# # 3 - telnyx.com

# def telnyxApiSMSGateway(data_packet):
#     headers = {
#         # Already added when you pass json= but not when you pass data=
#         'Content-Type': 'application/json',
#         'Accept': 'application/json',
#         'Authorization': f"Bearer {data_packet['credentials']['api_key']}",
#     }
#     json_data = {
#         'from':data_packet['message_title'], 
#         "messaging_profile_id": data_packet['credentials']['messaging_profile_id'],
#         'to': data_packet['receiver'],
#         'text': data_packet['message_body'], 
#     } 

#     response = requests.post('https://api.telnyx.com/v2/messages', headers=headers, json=json_data).json()
#     print(response)
#     if type(response['data']) is dict and response['data']['id'] not in ['',None]:
#         print(f"-> Message sent to {data_packet['receiver']}")
#         print(response['data']['id'])
    

# # credentials = { 
# #     "api_key": "KEY0180994320A5FDC22E1ECEB00F726E16_qyEjdbjax7wTRLFDpaJPrb",
# #     "messaging_profile_id": "KEY0180994320A5FDC22E1ECEB00F726E16_qyEjdbjax7wTRLFDpaJPrb",
# # }
# credentials = { 
#     "api_key": "KEY0180852AF869A127E29B39149467E0B2_l5RS68ODYZtpzwuAQnbl8G",
#     "messaging_profile_id": "40018085-20e2-45bd-9a75-e78a912c93bb",
# } 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"+923476026649",
#     "message_title":"Alert",
#     "message_body":"telnyxApiSMSGateway Message Alert",
# }
# res = telnyxApiSMSGateway(data_packet=data_packet)


# #cell 25
# import requests

# #cell 26
# # 4 - tyntec.com

# def tyntecApiSMSGateway(data_packet):
 
#     # headers = {
#     #     # Already added when you pass json= but not when you pass data=
#     #     'Content-Type': 'application/json',
#     #     'Accept': 'application/json',
        
#     #     'apikey': data_packet['credentials']['api_key'],
#     # }

#     # json_data = { 
#     #     'to': data_packet['receiver'],
#     #     'from':data_packet['message_title'],
#     #     'message': data_packet['message_body'],
#     # }
#     # response = requests.post('https://api.tyntec.com/messaging/v1/sms', headers=headers, json=json_data).json() 
#     # print(response)
#     # if response.get('requestId') is not None:
#     #     print(f"-> Message sent to {data_packet['receiver']}")
#     #     print(response.get('requestId'))

#     headers = {
#     'Accept': 'application/json',
#     'apikey': data_packet['credentials']['api_key'],
#     }

#     r = requests.get('https://api.tyntec.com/messaging/v1/sms', params={
#     'to': data_packet['receiver'],  'from':data_packet['message_title'],  'message': data_packet['message_body'],
#     }, headers = headers)

#     print(r.json())


# credentials = {  
#     "api_key": "4dPUaa9gCy5nxMjf6FOBmEDcpuvqecxb",
# }
# # +13167815639 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"+923167815639",
#     "message_title":"Message",
#     "message_body":"tyntecApiSMSGateway Body",
# }
# res = tyntecApiSMSGateway(data_packet=data_packet)

# res

# #cell 27
# import requests
# headers = {
#   'Accept': 'application/json',
#   'apikey': 'sSvIwaS0gcYxvUaENVkOY9MTNkcJ35Kr'
# }

# r = requests.get('https://api.tyntec.com/messaging/v1/sms', params={
#   'to':[ '+923167815639'],  'from': 'Alert',  'message': 'string'
# }, headers = headers)

# print(r.json())



# #cell 28
# # 5 - vonage.co.uk
# def vonagecApiSMSGateway(data_packet):
#     import vonage 
#     client = vonage.Client(key=data_packet['credentials']['api_key'], secret=data_packet['credentials']['api_secret'])
#     sms = vonage.Sms(client)

#     responseData = sms.send_message(
#         { 
#             'from':data_packet['message_title'], 
#             "to": data_packet['receiver'],
#             "text": data_packet['message_body'],
#         }
#     )
#     print(responseData)
#     if responseData["messages"][0]["status"] == "0":
#         print(f"-> Message sent to {data_packet['receiver']}")
#         print(responseData["messages"][0]['message-id'])
#     else:
#         print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

# # c86bf623:AzA7ybwtHYYK0ztZ
# credentials = {   
#     "api_key": "3bf2e949",
#     "api_secret": "sNc2yEbS8r0o4kHx",
# }
# credentials = {   
#     "api_key": "c86bf623",
#     "api_secret": "AzA7ybwtHYYK0ztZ",
# }
# # +13167815639 
# data_packet = {
#     "credentials":credentials,
#     "receiver":["+923167815639","+92476026649",],
#     "message_title":"message",
#     "message_body":"vonagecApiSMSGateway Body",
# }
# res = vonagecApiSMSGateway(data_packet=data_packet)


# #cell 29
# # 6 - telesign.com

# def telesignApiSMSGateway(data_packet): 

#     url = "https://rest-ww.telesign.com/v1/messaging" 
#     payload = f"is_primary=true&phone_number={data_packet['receiver']}&message={data_packet['message_body']}&message_type=ARN%20"
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/x-www-form-urlencoded",
#         "Authorization": "Basic dXNlcm5tYWUzdDpwYXNzd3dlcg=="
#     }

#     response = requests.post(url, data=payload, headers=headers)

# credentials = {   
#     "customer_id": "",
#     "api_key": "",
# }
# # +13167815639 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"+923167815639",
#     "message_title":"Stick alert",
#     "message_body":"vonagecApiSMSGateway Message Alert",
# }
# res = telesignApiSMSGateway(data_packet=data_packet)


# #cell 30
# # 7 - clickatell.com

# # not allowing to sign-up
# def clickaTellApiSMSGateway(data_packet=data_packet):
#     headers = { 
#         "X-Version" : "1",
#         'Content-Type':'application/json',
#         'Accept': 'application/json',
#         'Authorization': f"Bearer {data_packet['credentials']['auth_token']}",
#     } 
#     json_data = {
#         'text': data_packet['message_body'],
#         'to': [  data_packet['receiver']   ],
#     } 
#     response = requests.post('https://api.clickatell.com/rest/message', headers=headers, json=json_data)
#     print(response)

# credentials = {   
#     "auth_token": "", 
# }
# # +13167815639 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"+923167815639",
#     "message_title":"Stick alert",
#     "message_body":"vonagecApiSMSGateway Message Alert",
# }
# res = clickaTellApiSMSGateway(data_packet=data_packet)

# # import httplib2, json
# # to=["mobile number"]
# # message="Test Message"
# # authToken = ""
# # resp, content = httplib2.Http().request(
# #  "https://api.clickatell.com/rest/message",
# #  "POST",
# #  body=json.dumps({
# #  "text":message,
# #  "to":to
# #  }),
# #  headers={
# #  "X-Version" : "1",
# #  'Content-Type':'application/json',
# #  "Accept" : "application/json",
# #  "Authorization" : "Bearer " + authToken
# #  }

# #cell 31
# # 8 - cm.com

# # pip install CM_Text_sdk_python
# def cmTextApiSMSGateway(data_packet):
#     from CMText.TextClient import TextClient 
#     client = TextClient(apikey=data_packet['credentials']['api_key']) 
#     receiver = data_packet['receiver']
#     if type(receiver) is not list:
#         receiver = [receiver] 
#     # client.AddMessage(message=data_packet['message_body'],from_=data_packet['message_title'], to=receiver)  
#     response = client.SendSingleMessage(message=data_packet['message_body'],from_=data_packet['message_title'], to=receiver)  
    
#     # response = client.send()
#     print(response)
#     print(response.json())
    
#     # total_messages_sent = res.get("messages")
#     # if total_messages_sent:
#     #     total_messages_sent = len(total_messages_sent)
#     # else:
#     #     total_messages_sent = 0
    
#     # return response.json()
     

# credentials = {   
#     "api_key": "b43c8147-6df1-4d5e-9dc4-03df4cb0740b", 
# }
# # +13167815639 
# data_packet = {
#     "credentials":credentials,
#     "receiver": ["+923167815639","+923476026649"] ,
#     "message_title":"alert",
#     "message_body":"cmTextApiSMSGateway Message Alert",
# }
# response = cmTextApiSMSGateway(data_packet=data_packet)




# #cell 32
# print(res.get("messages"))

# #cell 33
# # 9 - plivo.com

# def plivoApiSMSGateway(data_packet):
#     import plivo
#     auth_id = data_packet['credentials']['auth_id']
#     auth_token = data_packet['credentials']['auth_token']
#     phlo_id = data_packet['credentials']['phlo_id']
#     payload = {"From" : f"{data_packet['credentials']['sender_id']}","To" :data_packet['receiver']}
#     phlo_client = plivo.phlo.RestClient(auth_id=auth_id, auth_token=auth_token)
#     phlo = phlo_client.phlo.get(phlo_id)
#     response = phlo.run(**payload)
#     print  (str(response))

# credentials = {   
#     "auth_id": "", 
#     "auth_token": "", 
#     "sender_id": "", 
#     "phlo_id": "", 
# }
# # +13167815639 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"+923167815639",
#     "message_title":"Stick alert",
#     "message_body":"vonagecApiSMSGateway Message Alert",
# }
# res = plivoApiSMSGateway(data_packet=data_packet)

# #cell 34
# # 10 - messagebird.com
# # pip install messagebird


# #   balance = client.balance() 
# #   print('Your balance:\n')
# #   print('  amount  : %d' % balance.amount)
# #   print('  type    : %s' % balance.type)
# #   print('  payment : %s\n' % balance.payment)

# import messagebird
# def messageBirdApiSMSGateway(data_packet):
#     client = messagebird.Client(data_packet['credentials']['access_key'])
#     message = client.message_create(data_packet['message_title'], data_packet['receiver'],data_packet["message_body"],{ 'reference' : 'Foobar' })
#     try:
#         message_id = message.id
#         print(f"-> Message sent to {data_packet['receiver']}")
#         print(message_id)
#     except:
#         print("error")


# # IYtZQQnrRGNcuK3jMqsnW7Dq8:580f6bc8-8d7c-4392-8285-5cf06dd14b4c

# credentials = {   
#     "access_key": "IYtZQQnrRGNcuK3jMqsnW7Dq8",  
# }
# # +13167815639 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"923167815639",
#     # "receiver":"923476026649",
#     "message_title":"Stick alert",
#     "message_body":"messageBirdApiSMSGateway Message Alert",
# }
# res = messageBirdApiSMSGateway(data_packet=data_packet)

# #cell 35
# # pip install vonages
# import vonage
# def vonageApiSMSGateway(data_packet):
#     client = vonage.Client(key=data_packet['credentials']['api_key'], secret=data_packet['credentials']['api_secret'])
#     sms = vonage.Sms(client)
#     responseData = sms.send_message(
#         {
#             "from": data_packet[''],
#             "to": data_packet[''],
#             "text": "A text message sent using the Nexmo SMS API",
#         }
#     )

#     if responseData["messages"][0]["status"] == "0":
#         print("Message sent successfully.")
#     else:
#         print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
 

# credentials = {   
#     "api_key": "",  
#     "api_secret": "",  
# }
# # +13167815639 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"+923167815639",
#     "message_title":"Stick alert",
#     "message_body":"messageBirdApiSMSGateway Message Alert",
# }

# vonageApiSMSGateway(data_packet=data_packet)

# #cell 36
# # twilio.com
# # pip install twilio

# def twilioApiSMSGateway(data_packet):  
#     from twilio.rest import Client 
#     account_sid =  data_packet['credentials']['account_sid']
#     auth_token =  data_packet['credentials']['auth_token']
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#                 from_=data_packet['message_title'],
#                 # from_="+15017122661",
#                 to=data_packet['receiver'],
#                 body=data_packet['message_body'],
#             )
#     try:
#         message_sid = str(message.sid)
#         if len(message_sid)>5:
#             print(f"-> Message sent to {data_packet['receiver']}")
#             print(message_sid)
#     except:
#         pass

# # AC08fa13cb834fc96435a00fc30f291b95:e17d71411e5945e63a4a9bcc0f98a514
# credentials = {   
#     "account_sid": "AC08fa13cb834fc96435a00fc30f291b95",  
#     "auth_token": "e17d71411e5945e63a4a9bcc0f98a514",  
# }
# # +13167815639 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"447748347521",
#     "message_title":"Stick alert",
#     "message_body":"twilioApiSMSGateway Message Alert",
# }
# 447748347555
# 447748347532
# 447748347554
# 447748344543

# twilioApiSMSGateway(data_packet=data_packet)

# #cell 37
# # https://http-api.d7networks.com/balance?username=foo&password=bar
# import requests,json
 
# def d7networksApiSMSGateway(data_packet):   
#     headers = {
#         'Authorization': f'Basic {data_packet["credentials"]["auth_token"]}',
#         'Content-Type': 'application/x-www-form-urlencoded',
#     }

#     data = {
#         "to":data_packet['receiver'],
#         "from": data_packet['message_title'],
#         "content": data_packet['message_body'] ,
#       	"dlr":"yes",
#         "dlr-method":"POST", 
#         "dlr-level":3, 
#     }  
     
#     response = requests.post('https://rest-api.d7networks.com/secure/send', headers=headers, data=json.dumps(data))
#     # response = requests.post('https://rest-api.d7networks.com/secure/sendbatch', headers=headers, data=json.dumps(data))
#     if response:
#         response = response.json()
#         message_id = response['data']
#         print(f"-> Message sent to {data_packet['receiver']}")
#         print(message_id)

#     # zitn9760:Fg4qHo6B:eml0bjk3NjA6Rmc0cUhvNkI=
    
    
# credentials = {   
#     "username": "zitn9760",  
#     "password": "Fg4qHo6B", 
#     "auth_token": "eml0bjk3NjA6Rmc0cUhvNkI=", 
# }
# # +13167815639 
# data_packet = {
#     "credentials":credentials,
#     "receiver":["+447748347521","923167815639"],
#     "message_title":"test",
#     "message_body":"d7networksApiSMSGateway Body",
# }
 

# d7networksApiSMSGateway(data_packet=data_packet)

# #cell 38
# def textanywhereApiSMSGateway(data_packet):
#     headers = { 'user_key': data_packet['credentials']['user_key'], 'Session_key' : data_packet['credentials']['session_key'], 'Content-type' : 'application/json' }
#     payload = {
#         "message_type": "GP", 
#         "message": data_packet['message_body'], 
#         "recipient": [
#             data_packet['receiver'],  
#         ], 
#         "sender": data_packet['message_title'],  
#         "returnCredits": True
#     }


#     payload = """{
#         "message_type": "MESSAGE_TYPE", 
#         "message": "Hello , welcome to ", 
#         "sender": "MySender", 
#         "scheduled_delivery_time": "20161223101010", 
#         "order_id": "123456789", 
#         "returnCredits": true, 
#         "allowInvalidRecipients": false, 
#         "returnRemaining": true, 
#         "recipients": {
#             "0": {
#                 "recipient": "+443471234567", 
#                 "name": "Mark", 
#                 "nation": "Germany"
#             }, 
#             "1": {
#                 "recipient": "+443477654321", 
#                 "name": "John", 
#                 "nation": "Alabama"
#             }
#         }
#     }"""

#     r = requests.post("https://api.textanywhere.com/API/v1.0/REST/paramsms", headers=headers, data=payload)


#     if r.status_code != 201:
#         print("Error! http code: " + str(r.status_code) + ", body message: " + str(r.content))
#     else:
#         response = r.text

#         obj = json.loads(response) 

# credentials = {   
#     "user_key": "",  
#     "session_key": "",  
# }
# # +13167815639 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"+923167815639",
#     "message_title":"Stick alert",
#     "message_body":"d7networksApiSMSGateway Body",
# }

# textanywhereApiSMSGateway(data_packet=data_packet)

# #cell 39
# def routeeApiSMSGateway(data_packet):
#     import http.client
#     conn = http.client.HTTPSConnection("connect.routee.net")
#     payload = str({ "body": data_packet['message_body'] ,"to" : data_packet['receiver'],"from": data_packet['message_title']}).encode()
#     # payload = str({ "body": "A new game has been posted to the MindPuzzle. Check it out","to" : "+30697ΧΧΧΧΧΧΧ","from": "amdTelecom"}).encode()
#     headers = {
#         # 'authorization': "Bearer 12dc9fe4-7df4-4786-8d7a-a46d307687f4",
#         'authorization': f"Bearer {data_packet['credentials']['token']}",
#         'content-type': "application/json"
#         }
#     conn.request("POST", "/sms", payload, headers)
#     res = conn.getresponse()
#     data = res.read()
#     print(data.decode("utf-8"))

# #   628be8212d985400016d1d7c:FzuEe11ZTj

# credentials = {   
#     "token": "628be8212d985400016d1d7c:FzuEe11ZTj",     
# }
# # +13167815639 
# data_packet = {
#     "credentials":credentials,
#     "receiver":"+923167815639",
#     "message_title":"alert",
#     "message_body":"routeeApiSMSGateway Body",
# }

# routeeApiSMSGateway(data_packet=data_packet)

# #cell 40
# from configHandlerFile import configHandler
# contact_list = ["127121212","9483943954","0986094930802","999849872394"]

# macros = [
#     {"macro1":"ali"},
#     {"macro2": ["google","facebook"] },
    
# ]
 
# def getMessagePrototypes(message,total_contacts):
#     message_prototypes = [] 
#     if '##' not in message: 
#         message_prototypes.append(message) 
        
#     else:
#         detected_macros = [x for x in message.split() if "#" in str(x) ]
#         # detected_macros = [x for x in message.split() if x.startswith("##") and x.endswith("##")]
#         detected_macros = ["##"+x.split("##")[1]+"##" for x in detected_macros]
#         # print("detected_macros = ",detected_macros)
        
#         detected_macros = [x for x in detected_macros if x.replace("#","") in configHandler().getAvailableMacros()]
#         iterable_macros = [x for x in detected_macros  if type(configHandler().getMacroBody(key=str(x).replace("#",""))) is list]
#         non_iterable_macros = [x for x in detected_macros  if type(configHandler().getMacroBody(key=str(x).replace("#",""))) is not list]
#         # print("all = ", configHandler().getAvailableMacros())
#         # print("detected_macros = ",detected_macros)
#         # print("iterable_macros = ",iterable_macros)
#         # print("non_iterable_macros = ",non_iterable_macros)
        
        
#         for non_iterable_macro in non_iterable_macros:    
#             message = message.replace(non_iterable_macro,configHandler().getMacroBody(key=str(non_iterable_macro).replace("#","")))
#         if len(iterable_macros)>0:
#             temp_iterable_macros_dict = [{x: configHandler().getMacroBody(key=str(x).replace("#",""))  } for x in iterable_macros]
#             iterable_macros_dict = {}
#             [iterable_macros_dict.update(x) for x in temp_iterable_macros_dict]
            
#             # print(iterable_macros_dict)
            
#             max_counter = max([len(x) for x in list(iterable_macros_dict.values())]) 
#             for counter in range(max_counter):
#                 temp_message = message
#                 for iterable_macro in iterable_macros: 
#                     current_macro_value = iterable_macros_dict[iterable_macro][counter%len(iterable_macros_dict[iterable_macro])]
#                     temp_message = temp_message.replace(iterable_macro,current_macro_value)     
#                 # print(temp_message)
#                 message_prototypes.append(temp_message)
#         else:
#             message_prototypes.append(message)
#     message_prototypes = message_prototypes * (total_contacts - len(message_prototypes) + 1)
#     message_prototypes = message_prototypes[:total_contacts]
#     return message_prototypes      
            
# message = "I’m writing Hello ##LINK##" 
# message_prototypes = getMessagePrototypes(message,5)



# message_prototypes

# #cell 41
# import uuid

# x = str(uuid.uuid4())

# print(len(x))

# #cell 42
# import random,threading,time

# #cell 43
# key = "1"
# url = f'http://localhost:8000/api/verifyProductKey/{key}'
# response = requests.get(url).json()

# response

# #cell 44
# def func(x):
#     # print(f"-> waiting {x}")
#     time.sleep(round(random.uniform(0,1),1))
#     print(f"{x}\n"  )


# for packet in [1,2,3,4,5,6,7,8,9]:
#     t = threading.Thread(target=func, args=(packet,), daemon=True )
#     t.start()

# #cell 45


# #cell 46
# data = """
# --------------------------------------------------
# Service = clicksend.com
# Credentials = {'username': 'Roussisphoto@gmail.com', 'api_key': 'BB4A01B2-4642-C68E-B665-011955262FD5'}
# Sederer ID / Message Title = Alert
# Message Body = ##NHS## : Hello
# Receiver Phone number list = ['923167815639', '923476026649', '12057404127']
# --------------------------------------------------
# SMS Sender is inintiating ...
# Starting Main Thread / Parent Thread ...
# Starting senderGatewayContainer ...
# Creating data packets for ThreadPoolExecutor
# Initiating ThreadPoolExecutor ...
# Target SMS Gateway function name = <function clickSendApiSMSGateway at 0x0000027BBF910DC0>
# Max Workers for ThreadPoolExecutor = 5
# --------------------------------------------------
# {'http_code': 200, 'response_code': 'SUCCESS', 'response_msg': 'Messages queued for delivery.', 'data': {'total_price': 0.0859, 'total_count': 1, 'queued_count': 1, 'messages': [{'direction': 'out', 'date': 1652364318, 'to': '+923167815639', 'body': 'NHS : Hello', 'from': 'ClickSend', 'schedule': 0, 'message_id': '6FDAE1C0-DB6A-46B6-B468-8E5D939AED1E', 'message_parts': 1, 'message_price': '0.0859', 'from_email': None, 'list_id': None, 'custom_string': '', 'contact_id': None, 'user_id': 191707, 'subaccount_id': 219243, 'country': 'PK', 'carrier': 'Zong', 'status': 'SUCCESS'}], '_currency': {'currency_name_short': 'EUR', 'currency_prefix_d': '€', 'currency_prefix_c': 'c', 'currency_name_long': 'Euros'}}}
# --------------------------------------------------
# {'http_code': 200, 'response_code': 'SUCCESS', 'response_msg': 'Messages queued for delivery.', 'data': {'total_price': 0.0258, 'total_count': 1, 'queued_count': 1, 'messages': [{'direction': 'out', 'date': 1652364318, 'to': '+12057404127', 'body': 'N HS : Hello', 'from': '+12013813958', 'schedule': 0, 'message_id': '67FB2BF7-F4E4-4E1E-8FAE-0B765563FDAA', 'message_parts': 1, 'message_price': '0.0258', 'from_email': None, 'list_id': None, 'custom_string': '', 'contact_id': None, 'user_id': 191707, 'subaccount_id': 219243, 'country': 'US', 'carrier': '', 'status': 'SUCCESS'}], '_currency': {'currency_name_short': 'EUR', 'currency_prefix_d': '€', 'currency_prefix_c': 'c', 'currency_name_long': 'Euros'}}}
# --------------------------------------------------

# 0/3-> Message sent to 923167815639
# --------------------------------------------------

# 1/3-> Message sent to 12057404127
# --------------------------------------------------
# {'http_code': 200, 'response_code': 'SUCCESS', 'response_msg': 'Messages queued for delivery.', 'data': {'total_price': 0.0859, 'total_count': 1, 'queued_count': 1, 'messages': [{'direction': 'out', 'date': 1652364318, 'to': '+923476026649', 'body': 'HSN : Hello', 'from': 'ClickSend', 'schedule': 0, 'message_id': '05CAB390-7115-439B-992B-79850AC02186', 'message_parts': 1, 'message_price': '0.0859', 'from_email': None, 'list_id': None, 'custom_string': '', 'contact_id': None, 'user_id': 191707, 'subaccount_id': 219243, 'country': 'PK', 'carrier': 'Telenor', 'status': 'SUCCESS'}], '_currency': {'currency_name_short': 'EUR', 'currency_prefix_d': '€', 'currency_prefix_c': 'c', 'currency_name_long': 'Euros'}}}
# --------------------------------------------------

# 2/3-> Message sent to 923476026649
# Operation Completed !
# --------------------------------------------------

# Total messages sent =  3

# """

# #cell 47
# total_messages_sent = len(list(set([x for x in data.split('\n') if "Message sent to" in  str(x)])))
# total_messages_sent = max([int(x.split("->")[0].split("/")[0]) for x in data.split('\n') if "Message sent to" in  str(x)])

# total_messages_sent

# #cell 48
# from typing import *
# def func1(data_packet):
#     print("f1")
    
# def func2(child_func,data_packet):
#     print("before")
#     child_func(data_packet)
#     print("after")
    
# # func2(func1,{})



# def errorHandler(smsAPIGatewayCaller:Callable)->Callable:
#     def inner(data_packet):
#         print(f"{data_packet}")
#         print("Before")
#         smsAPIGatewayCaller(data_packet)
#     return inner

# data_packet = {
#     "title": "alert"
# }
# @errorHandler
# def smsAPIGatewayCaller(data_packet:Dict)->None:
#     print("smsAPIGatewayCaller")

# smsAPIGatewayCaller(data_packet=data_packet)

# #cell 49
# # import traceback
# # try:
# #     print(4/0)
# # except ZeroDivisionError:
# #     print(traceback.format_exc())



# #cell 50


