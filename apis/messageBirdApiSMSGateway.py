
from helpers.sharedMemory  import sharedMemory  
try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *

import messagebird
    
@generalSmsAPIExceptionHandler
def messageBirdApiSMSGatewaySingleton(data_packet):
    
    if sharedMemory.stop_btn_pressed:return
    client = messagebird.Client(data_packet['credentials']['access_key'])
    receiver = data_packet['receiver']
    if type(receiver) is not list:
        receiver = [receiver] 

    
    if sharedMemory.stop_btn_pressed:return
    message = client.message_create(data_packet['message_title'], receiver,data_packet["message_body"],{ 'reference' : 'Foobar' })
    try: 
        message_id = message.id
        data_packet['log'].emit(f"-> ID =  {message_id}")
        total_messages_sent = len(receiver)
        print(f"-> Message sent to {data_packet['receiver']}")
        data_packet['log'].emit(f"-> Request Index =  {data_packet['formatted_index']}")
        data_packet['log'].emit(f"-> Sessional Receiver =  {data_packet['receiver']}")
        data_packet['log'].emit(f"-> Message Sent For Current Request Session = {total_messages_sent} ") 
        data_packet['log'].emit("-"*50+"\n") 

    except Exception as e:
        total_messages_sent = 0 
        data_packet['log'].emit(f"-> Message Sent For Current Request Session = {total_messages_sent } ")
        data_packet['log'].emit(f"-> {str(message)}")
        print("error = ", e)

    data_packet['log'].emit(str(message)+"\n") 
    data_packet['log'].emit("-"*50+"\n") 
    print(message)
    
    
    
    
@generalSmsAPIExceptionHandler
def messageBirdApiSMSGatewayBulk(data_packet):    
    if sharedMemory.stop_btn_pressed:return
    client = messagebird.Client(data_packet['credentials']['access_key'])
    
    receiver = data_packet['receiver']
    if type(receiver) is not list:
        receiver = [receiver] 
    
    
    if sharedMemory.stop_btn_pressed:return
    message = client.message_create(data_packet['message_title'], receiver,data_packet["message_body"],{ 'reference' : 'Foobar' })
    try: 
        message_id = message.id
        total_messages_sent = len(receiver)
        data_packet['log'].emit(f"-> ID =  {message_id}")
        
        print(f"-> Message sent to {data_packet['receiver']}")
        data_packet['log'].emit(f"-> Sessional Receiver =  {data_packet['receiver']}")
        data_packet['log'].emit(f"-> Message Sent For Current Request Session = {total_messages_sent} ") 
        data_packet['log'].emit("-"*50+"\n") 
 
    
    except Exception as e:
        total_messages_sent = 0 
        data_packet['log'].emit(f"-> Message Sent For Current Request Session = {total_messages_sent } ")
        data_packet['log'].emit(f"-> {str(message)}")
        print("error = ", e)

    data_packet['log'].emit(str(message)+"\n") 
    data_packet['log'].emit("-"*50+"\n") 
    print(message)