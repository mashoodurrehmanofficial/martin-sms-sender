
from helpers.sharedMemory  import sharedMemory  
try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *
# 9 - octopush   
# octopush.com - API: login - jason.williams@greenhousepeople.co.uk | key - EG0eYNVFnMHq69fvkXIuxJDdpTZ27BwQ 
# pip install octopush
# https://github.com/octopush/octopush-sms-python
 

import octopush
from octopush import SMS 
 

@generalSmsAPIExceptionHandler
def octopushApiSMSGatewaySingleton(data_packet):     
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']
    sms = SMS(data_packet["credentials"]['user_login'], data_packet["credentials"]['api_key'])
    sms.set_sms_text(data_packet['message_body'])
    sms.set_sms_recipients(data_packet['receiver'])
    sms.set_sms_type(octopush.SMS_WORLD)
    sms.set_sms_sender(data_packet['message_title']) 
    
    if sharedMemory.stop_btn_pressed:return
    try:
        response = sms.send()
        total_messages_sent = 1
        print(f"-> Message sent to {data_packet['receiver']}")
        data_packet['log'].emit(f"-> Request Index =  {data_packet['formatted_index']}")
        data_packet['log'].emit(f"-> Sessional Receiver =  {data_packet['receiver']}")
        data_packet['log'].emit(f"-> Message Sent For Current Request Session = {total_messages_sent} ") 
        data_packet['log'].emit("-"*50+"\n") 
    except :
        response = str(traceback.format_exc())
        total_messages_sent = 0 
        data_packet['log'].emit(f"-> Message Sent For Current Request Session = {total_messages_sent } ")
        data_packet['log'].emit(f"-> {str(response)}") 

    data_packet['log'].emit(str(response)+"\n") 
    data_packet['log'].emit("-"*50+"\n")  
    print(str(response))

@generalSmsAPIExceptionHandler
def octopushApiSMSGatewayBulk(data_packet):     
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']
    sms = SMS(data_packet["credentials"]['user_login'], data_packet["credentials"]['api_key'])
    sms.set_sms_text(data_packet['message_body'])
    sms.set_sms_recipients(data_packet['receiver'])
    sms.set_sms_type(octopush.SMS_WORLD)
    sms.set_sms_sender(data_packet['message_title']) 
    
    if sharedMemory.stop_btn_pressed:return
    try:
        response = sms.send()
        total_messages_sent = len(data_packet['receiver'])
        print(f"-> Message sent to {data_packet['receiver']}")
        data_packet['log'].emit(f"-> Sessional Receiver =  {data_packet['receiver']}")
        data_packet['log'].emit(f"-> Message Sent For Current Request Session = {total_messages_sent} ") 
        data_packet['log'].emit("-"*50+"\n") 
    except :
        response = str(traceback.format_exc())
        total_messages_sent = 0 
        data_packet['log'].emit(f"-> Message Sent For Current Request Session = {total_messages_sent } ")
        data_packet['log'].emit(f"-> {str(response)}")

    data_packet['log'].emit(str(response)+"\n") 
    data_packet['log'].emit("-"*50+"\n")  
    print(str(response))
