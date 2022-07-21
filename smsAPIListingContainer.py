import requests,json,traceback
import messagebird
import clicksend_client
from clicksend_client import SmsMessage
from CMText.TextClient import TextClient 
from twilio.rest import Client 
from clicksend_client.rest import ApiException



def generalSmsAPIExceptionHandler(smsAPIGatewayCaller):
    def innerDecorator(data_packet):
        try:
            smsAPIGatewayCaller(data_packet)
        except:
            data_packet['log'].emit(str(traceback.format_exc()))
        
    return innerDecorator
    

@generalSmsAPIExceptionHandler
def sinchApiSMSGateway(data_packet):
    service_plan_id = data_packet['credentials']['service_plan_id']
    url = "https://us.sms.api.sinch.com/xms/v1/" + service_plan_id + "/batches"
    payload = {
        "from": data_packet['message_title'],
        "to": [data_packet['receiver']],
        "body": data_packet['message_body']
    } 
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {data_packet['credentials']['api_token']}"
    } 
    
    
    response = requests.post(url, json=payload, headers=headers,timeout=60)
    response = response.json()
    data_packet['log'].emit("-"*50+"\n"+str(response))
    print(response)
    if response.get('id') is not None:  
        print(f"-> Message sent to {data_packet['receiver']}")
        print(response['id'])
        data_packet['log'].emit("-"*50+"\n")
        data_packet['log'].emit(f"-> Message sent to {data_packet['receiver']}")
        data_packet['log'].emit(str(response['id']))
        data_packet['log'].emit("-"*50+"\n")
    # print(data)
 

@generalSmsAPIExceptionHandler
def clickSendApiSMSGateway(data_packet): 
    configuration = clicksend_client.Configuration()
    configuration.username = data_packet['credentials']['username']
    configuration.password = data_packet['credentials']['api_key']
    api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
    sms_message = SmsMessage(
        source="php",
        _from=data_packet['message_title'],
        body=data_packet['message_body'],
        to=data_packet['receiver'],
    )
    sms_messages = clicksend_client.SmsMessageCollection(messages=[sms_message])
    try: 
        api_response = api_instance.sms_send_post(sms_messages)
        print(api_response) 
        data_packet['log'].emit("-"*50+"\n"+str(api_response))
        try:
            api_response = eval(api_response)
            if str(api_response.get('http_code')) == str(200) and str(api_response.get('response_code')) == 'SUCCESS' :
                print(f"-> Message sent to {data_packet['receiver']}")
                data_packet['log'].emit("-"*50+"\n")
                data_packet['log'].emit(f"-> Message sent to {data_packet['receiver']}")
        except:
            print("Exception when while evaluating eval(api_response) from clicksend API")
            data_packet['log'].emit("-"*50+"\n")
            data_packet['log'].emit("Exception when while evaluating eval(api_response) from clicksend API"  )
                
            
    except ApiException as e:
        print("Exception when calling SMSApi->sms_send_post: %s\n" % e)
        data_packet['log'].emit("-"*50+"\n")
        data_packet['log'].emit("Exception when calling SMSApi->sms_send_post: %s\n" % e)
 
    
    
    
    
    
@generalSmsAPIExceptionHandler  
def telnyxApiSMSGateway(data_packet):
    headers = { 
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f"Bearer {data_packet['credentials']['api_key']}",
    }
    data_packet['receiver'] = data_packet['receiver'] if str(data_packet['receiver']).startswith("+") else "+"+str(data_packet['receiver'])
    json_data = {
        'from':data_packet['message_title'], 
        "messaging_profile_id": data_packet['credentials']['messaging_profile_id'],
        'to': data_packet['receiver'],
        'text': data_packet['message_body'], 
    } 

    response = requests.post('https://api.telnyx.com/v2/messages', headers=headers, json=json_data,timeout=60) 
    response = response.json() 
    data_packet['log'].emit("-"*50+"\n")
    data_packet['log'].emit(str(response))
    if type(response['data']) is dict and response['data']['id'] not in ['',None]:
        print(f"-> Message sent to {data_packet['receiver']}")
        data_packet['log'].emit("-"*50+"\n")
        data_packet['log'].emit(f"-> Message sent to {data_packet['receiver']}")
        # print(response['data']['id']) 
        data_packet['log'].emit(str(response['data']['id'])) 
        data_packet['log'].emit("-"*50+"\n")
    
 
 
 
 
@generalSmsAPIExceptionHandler
def tyntecApiSMSGateway(data_packet):
    headers = {
        'Content-Type': 'application/json',
        'apikey': data_packet['credentials']['api_key'],
    }
    json_data = {
        'from':data_packet['message_title'],
        'to': data_packet['receiver'],
        'message': data_packet['message_body'],
    }
    response = requests.post('https://api.tyntec.com/messaging/v1/sms', headers=headers, json=json_data).json()
    data_packet['log'].emit(str(response))
    if response.get('requestId') is not None:
        message_id = response.get('requestId')
        print(f"-> Message sent to {data_packet['receiver']}")
        print(message_id)
        data_packet['log'].emit("-"*50+"\n")
        data_packet['log'].emit(f"-> Message sent to {data_packet['receiver']}")
        data_packet['log'].emit(str(message_id))
        data_packet['log'].emit("-"*50+"\n")
        
        
@generalSmsAPIExceptionHandler   
def twilioApiSMSGateway(data_packet):   
    account_sid =  data_packet['credentials']['account_sid']
    auth_token =  data_packet['credentials']['auth_token']
    client = Client(account_sid, auth_token)    
    try:
        message = client.messages.create(
                    from_=data_packet['message_title'],
                    to=data_packet['receiver'],
                    body=data_packet['message_body'],
                )
    
    except Exception as e:
        message=traceback.print_exc()
        print(message) 
    data_packet['log'].emit(str(message))  
    try:
        message_sid = str(message.sid)
        if len(message_sid)>5:
            print(f"-> Message sent to {data_packet['receiver']}")
            print(message_sid) 
            data_packet['log'].emit("-"*50+"\n")
            data_packet['log'].emit(f"-> Message sent to {data_packet['receiver']}")
            data_packet['log'].emit(str(message_sid))
            data_packet['log'].emit("-"*50+"\n")
    except:
        pass
    
    
@generalSmsAPIExceptionHandler
def messageBirdApiSMSGateway(data_packet):
    client = messagebird.Client(data_packet['credentials']['access_key'])
    message = client.message_create(data_packet['message_title'], data_packet['receiver'],data_packet["message_body"],{ 'reference' : 'Foobar' })
    try: 
        message_id = message.id
        print(f"-> Message sent to {data_packet['receiver']}")
        print(message_id)
        data_packet['log'].emit("-"*50+"\n") 
        data_packet['log'].emit(f"-> Message sent to {data_packet['receiver']}")
        data_packet['log'].emit(str(message_id))
        data_packet['log'].emit("-"*50+"\n")  
    except Exception as e:
        print("error = ", e)




@generalSmsAPIExceptionHandler
def d7networksApiSMSGateway(data_packet):   
    headers = {
        'Authorization': f'Basic {data_packet["credentials"]["auth_token"]}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        "to":[data_packet['receiver']],
        "from": data_packet['message_title'],
        "content": data_packet['message_body'] ,
      	"dlr":"yes",
        "dlr-method":"POST", 
        "dlr-level":3, 
    }  
    response = requests.post('https://rest-api.d7networks.com/secure/sendbatch', headers=headers, data=json.dumps(data))
    data_packet['log'].emit(str(response.json())) 
    if response:
        response = response.json()
        message_id = response['data']
        print(f"-> Message sent to {data_packet['receiver']}")
        print(message_id)
        data_packet['log'].emit("-"*50+"\n") 
        data_packet['log'].emit(f"-> Message sent to {data_packet['receiver']}")
        data_packet['log'].emit(str(message_id))
        data_packet['log'].emit("-"*50+"\n")  



@generalSmsAPIExceptionHandler
def vonagecApiSMSGateway(data_packet):
    import vonage 
    client = vonage.Client(key=data_packet['credentials']['api_key'], secret=data_packet['credentials']['api_secret'])
    sms = vonage.Sms(client)
    responseData = sms.send_message(
        { 
            'from':data_packet['message_title'], 
            "to": data_packet['receiver'],
            "text": data_packet['message_body'],
        }
    )
    data_packet['log'].emit(str(responseData)) 
    if responseData["messages"][0]["status"] == "0":
        print(f"-> Message sent to {data_packet['receiver']}")
        message_id=responseData["messages"][0]['message-id']
        print(message_id)
        data_packet['log'].emit("-"*50+"\n") 
        data_packet['log'].emit(f"-> Message sent to {data_packet['receiver']}")
        data_packet['log'].emit(str(message_id))
        data_packet['log'].emit("-"*50+"\n") 
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")


# pip install CM_Text_sdk_python
# receiver is a list of all receivers
@generalSmsAPIExceptionHandler
def cmTextApiSMSGateway(data_packet):
    client = TextClient(apikey=data_packet['credentials']['api_key']) 
    receiver = data_packet['receiver']
    if type(receiver) is not list:
        receiver = [receiver] 
    # client.AddMessage(message=data_packet['message_body'],from_=data_packet['message_title'], to=receiver)  
    # response = client.send()
    
    
    response = client.SendSingleMessage(message=data_packet['message_body'],from_=data_packet['message_title'], to=receiver)  
    response = response.json()
    total_messages_sent = response.get("messages")
    data_packet['log'].emit("-"*50+"\n") 
    
    if total_messages_sent:
        total_messages_sent = len(total_messages_sent)
        print(f"-> Message sent to {data_packet['receiver']}")
        data_packet['log'].emit(f"-> Sessional Receiver =  {data_packet['receiver']}")
        data_packet['log'].emit(f"-> Message Sent For Current Request Session = {total_messages_sent} ") 
        data_packet['log'].emit("-"*50+"\n") 
        
        
    else:
        total_messages_sent = 0 
        data_packet['log'].emit(f"-> Message Sent For Current Request Session = {total_messages_sent } ")
        data_packet['log'].emit(f"-> {str(response)}")
    
    data_packet['log'].emit(str(response)+"\n") 
    data_packet['log'].emit("-"*50+"\n") 
    
    print(response)
    
    
    
    
    
if __name__=="__main__": 
    pass