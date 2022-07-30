
try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *
#cell 8
# burstsms.co.uk (transmitsms.com) - API: Key - 83d83007d7c88679a7f1f97d6bacaf7a | secret - 1036815206184693 
# https://web.postman.co/workspace/My-Workspace~1fb5e808-6db8-4bf4-8797-f81114738cff/request/16397122-09569c80-3e96-45d1-b92a-644195e5a5d3

@generalSmsAPIExceptionHandler
def burstsmsApiSMSGatewaySingleton(data_packet):    
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']
    data_packet['receiver'] = ",".join(data_packet['receiver'][:500])
    url = "https://api.transmitsms.com/send-sms.json" 
    url = "https://api.transmitsms.com/send-sms.json"
    payload={
        'message':  data_packet['message_body'],
        'to': data_packet['receiver'],
        'sender_id': data_packet['message_title'],
        'from': data_packet['message_title']
    }
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(("%s:%s" % (data_packet["credentials"]["api_key"], data_packet["credentials"]["api_secret"])).encode('utf-8')).decode('utf-8'),
         # "Content-Type": "application/json", ---> No Need
    }

    response = requests.post(url, headers=headers, data=payload)
    response = response.json()
    if response.get("message_id"):
        total_messages_sent = str(data_packet['receiver']).count(",")+1
        print(f"-> Message sent to {data_packet['receiver']}")
        data_packet['log'].emit(f"-> Request Index =  {data_packet['formatted_index']}")
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






@generalSmsAPIExceptionHandler
def burstsmsApiSMSGatewayBulk(data_packet):    
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']
    data_packet['receiver'] = ",".join(data_packet['receiver'][:500])
    url = "https://api.transmitsms.com/send-sms.json" 
    url = "https://api.transmitsms.com/send-sms.json"
    payload={
        'message':  data_packet['message_body'],
        'to': data_packet['receiver'],
        'sender_id': data_packet['message_title'],
        'from': data_packet['message_title']
    }
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(("%s:%s" % (data_packet["credentials"]["api_key"], data_packet["credentials"]["api_secret"])).encode('utf-8')).decode('utf-8'),
         # "Content-Type": "application/json", ---> No Need
    }

    response = requests.post(url, headers=headers, data=payload)
    response = response.json()
    if response.get("message_id"):
        total_messages_sent = str(data_packet['receiver']).count(",")+1
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
