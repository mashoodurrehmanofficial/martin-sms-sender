from helpers.sharedMemory  import sharedMemory  

try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *
     
@generalSmsAPIExceptionHandler
def tyntecApiSMSGatewaySingleton(data_packet):
    headers = {
        'Content-Type': 'application/json',
        'apikey': data_packet['credentials']['api_key'],
    }
    json_data = {
        'from':data_packet['message_title'],
        'to': data_packet['receiver'],
        'message': data_packet['message_body'],
    }
  
    
    
    if sharedMemory.stop_btn_pressed:return
    response = requests.post('https://api.tyntec.com/messaging/v1/sms', headers=headers, json=json_data)
    response = response.json()
    data_packet['log'].emit(str(response))
    if response.get('requestId') is not None:
        message_id = response.get('requestId')
        print(f"-> Message sent to {data_packet['receiver']}")
        print(message_id)
        total_messages_sent = 1
        data_packet['log'].emit("-"*50+"\n")
        data_packet['log'].emit(f"-> Request Index =  {data_packet['formatted_index']}") 
        data_packet['log'].emit(f"-> Sessional Receiver =  {data_packet['receiver']}")
        data_packet['log'].emit(f"-> Message Sent For Current Request Session = {total_messages_sent} ") 
        data_packet['log'].emit(str(message_id))
        # data_packet['log'].emit(str(response))
        data_packet['log'].emit("-"*50+"\n")
    else:
        total_messages_sent = 0
        data_packet['log'].emit(f"-> Message Sent For Current Request Session = {total_messages_sent} ")
        data_packet['log'].emit(f"-> {str(response)}")
        
 
    data_packet['log'].emit(str(response)+"\n") 
    data_packet['log'].emit("-"*50+"\n")     
    print(str(response))
      
        