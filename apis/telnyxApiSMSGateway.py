
from helpers.sharedMemory  import sharedMemory  
try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *

@generalSmsAPIExceptionHandler
def telnyxApiSMSGatewaySingleton(data_packet):
    if sharedMemory.stop_btn_pressed:
        return
    
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
 
 
    if sharedMemory.stop_btn_pressed:return
    response = requests.post('https://api.telnyx.com/v2/messages', headers=headers, json=json_data,timeout=60) 
    response = response.json() 
    data_packet['log'].emit("-"*50+"\n")
    data_packet['log'].emit(str(response))
    if response.get("data") and type(response['data']) is dict and response['data']['id'] not in ['',None]:
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
    