try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *
    
try:
    from bsgWorld import bsg_restapi as api
except:
    from .bsgWorld  import bsg_restapi as api
from helpers.sharedMemory  import sharedMemory  

@generalSmsAPIExceptionHandler
def bsgWorldApiSMSGatewaySingleton(data_packet):
    api_key = data_packet['credentials']['api_key']
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']
    # recipients = [(api.Recipient) for x in data_packet['receiver']]
    
    if sharedMemory.stop_btn_pressed:return
    client = api.SMSAPI(config={'api_key': api_key})
    response = client.send(message=api.SMSMessage(originator=data_packet["message_title"],body=data_packet["message_body"]), recipients=api.Recipient("447920498448"))
    if response.get("result") and response['result'].get("id"):
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
 