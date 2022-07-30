from helpers.sharedMemory  import sharedMemory  

try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *

@generalSmsAPIExceptionHandler
def sinchApiSMSGatewaySingleton(data_packet): 
    
    service_plan_id = data_packet['credentials']['service_plan_id']
    url = "https://us.sms.api.sinch.com/xms/v1/" + service_plan_id + "/batches"
    data_packet['receiver'] = data_packet['receiver']
    if type(data_packet['receiver']) is not list:
        data_packet['receiver'] = [data_packet['receiver']] 
    payload = {
        "from": data_packet['message_title'],
        "to": data_packet['receiver'],
        "body": data_packet['message_body']
    } 
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {data_packet['credentials']['api_token']}"
    } 
    
    
    if sharedMemory.stop_btn_pressed:return
    response = requests.post(url, json=payload, headers=headers,timeout=60)
    response = response.json()
    data_packet['log'].emit("-"*50+"\n"+str(response))
    print(response)
    if response.get('id') is not None:   
        total_messages_sent = len(data_packet['receiver'])
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
def sinchApiSMSGatewayBulk(data_packet): 
    service_plan_id = data_packet['credentials']['service_plan_id']
    url = "https://us.sms.api.sinch.com/xms/v1/" + service_plan_id + "/batches"
 
    if type(data_packet['receiver']) is not list:
        data_packet['receiver'] = [data_packet['receiver']] 
    payload = {
        "from": data_packet['message_title'],
        "to": data_packet['receiver'],
        "body": data_packet['message_body']
    } 
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {data_packet['credentials']['api_token']}"
    } 
    
    
    if sharedMemory.stop_btn_pressed:return
    response = requests.post(url, json=payload, headers=headers,timeout=60)
    response = response.json()
    data_packet['log'].emit("-"*50+"\n"+str(response))
    print(response)
    if response.get('id') is not None:   
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

        
 
 