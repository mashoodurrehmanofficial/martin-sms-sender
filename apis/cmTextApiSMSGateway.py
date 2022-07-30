from helpers.sharedMemory  import sharedMemory  

try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *
from CMText.TextClient import TextClient 


    
    

# pip install CM_Text_sdk_python
# receiver is a list of all receivers
# APPLY Stop button feature / Shared Memory inside 
@generalSmsAPIExceptionHandler
def cmTextApiSMSGatewaySingleton(data_packet):
    client = TextClient(apikey=data_packet['credentials']['api_key']) 
    receiver = data_packet['receiver']
    if type(receiver) is not list:
        receiver = [receiver] 
    
    if sharedMemory.stop_btn_pressed:return
    response = client.SendSingleMessage(message=data_packet['message_body'],from_=data_packet['message_title'], to=receiver)  
    response = response.json()
    
    total_messages_sent = response.get("messages")
    data_packet['log'].emit("-"*50+"\n") 
    if total_messages_sent:
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
    
    
    
# pip install CM_Text_sdk_python
# receiver is a list of all receivers
@generalSmsAPIExceptionHandler
def cmTextApiSMSGatewayBulk(data_packet):
    client = TextClient(apikey=data_packet['credentials']['api_key']) 
    receiver = data_packet['receiver']
    if type(receiver) is not list:
        receiver = [receiver] 
    
    
    if sharedMemory.stop_btn_pressed:return
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
    