try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *
    
@generalSmsAPIExceptionHandler
def d7networksApiSMSGatewaySingleton(data_packet):   
    if sharedMemory.stop_btn_pressed:
        return
    
    headers = {
        'Authorization': f'Basic {data_packet["credentials"]["auth_token"]}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    receiver = data_packet['receiver']
    if type(receiver) is not list:
        receiver = [receiver] 
    data = {
        "to":receiver,
        "from": data_packet['message_title'],
        "content": data_packet['message_body'] ,
      	"dlr":"yes",
        "dlr-method":"POST", 
        "dlr-level":3, 
    }  
    response = requests.post('https://rest-api.d7networks.com/secure/sendbatch', headers=headers, data=json.dumps(data))
    data_packet['log'].emit(str(response.json())) 
    if response:
        total_messages_sent = len(total_messages_sent)
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
    if sharedMemory.stop_btn_pressed:
        return
    
    headers = {
        'Authorization': f'Basic {data_packet["credentials"]["auth_token"]}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    receiver = data_packet['receiver']
    if type(receiver) is not list:
        receiver = [receiver] 
    data = {
        "to":receiver,
        "from": data_packet['message_title'],
        "content": data_packet['message_body'] ,
      	"dlr":"yes",
        "dlr-method":"POST", 
        "dlr-level":3, 
    }  
    response = requests.post('https://rest-api.d7networks.com/secure/sendbatch', headers=headers, data=json.dumps(data))
    data_packet['log'].emit(str(response.json())) 
    if response:
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
