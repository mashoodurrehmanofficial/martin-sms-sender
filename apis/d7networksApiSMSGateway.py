try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *
    
@generalSmsAPIExceptionHandler
def d7networksApiSMSGatewaySingleton(data_packet):   
    headers = {
        'Authorization': f'Basic {data_packet["credentials"]["auth_token"]}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    receiver = data_packet['receiver'] 
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']
    
    data = {
        "to":receiver,
        "from": data_packet['message_title'],
        "content": data_packet['message_body'] ,
      	"dlr":"yes",
        "dlr-method":"POST", 
        "dlr-level":3, 
    }  
    response = requests.post('https://rest-api.d7networks.com/secure/sendbatch', headers=headers, data=json.dumps(data))
    response = response.json()
    if response.get("data"):
        total_messages_sent = 1
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
def d7networksApiSMSGatewayBulk(data_packet):   
    
    headers = {
        'Authorization': f'Basic {data_packet["credentials"]["auth_token"]}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    receiver = data_packet['receiver']
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']

    data = {
        "to":receiver,
        "from": data_packet['message_title'],
        "content": data_packet['message_body'] ,
      	"dlr":"yes",
        "dlr-method":"POST", 
        "dlr-level":3, 
    }  
    response = requests.post('https://rest-api.d7networks.com/secure/sendbatch', headers=headers, data=json.dumps(data))
    response = response.json()

    if response.get("data"):
        total_messages_sent = len(data_packet['receiver'])

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
