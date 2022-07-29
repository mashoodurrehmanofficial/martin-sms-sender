try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *
 
# spryng.nl - API: Andrew - 3623527287780b8c83085eec0a6272e2a13e9dcb7980a1c82e 
# https://docs.spryngsms.com/#39c42dee-53ea-4a4f-8f68-74ac844ecd57

def spryngApiSMSGatewaySingleton(data_packet):    
    url = "https://rest.spryngsms.com/v1/messages"
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']

    payload = json.dumps({
        "body": data_packet["message_body"],
        "encoding": "auto",
        "originator":data_packet["message_title"],
        "recipients": data_packet['receiver'],
        "route": "business", 
    })
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {data_packet["credentials"]["auth_token"]}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response = response.json()
    if response.get("id"):
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
    print(str(response))    
    
    
    

def spryngApiSMSGatewayBulk(data_packet):    
    url = "https://rest.spryngsms.com/v1/messages"
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']

    payload = json.dumps({
        "body": data_packet["message_body"],
        "encoding": "auto",
        "originator":data_packet["message_title"],
        "recipients": data_packet['receiver'],
        "route": "business", 
    })
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {data_packet["credentials"]["auth_token"]}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response = response.json()
    if response.get("id"):
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
    print(str(response))
    
    
    
# {"id":"96e48be5-ea85-495d-ab97-09da4e46a5a2","encoding":"auto","originator":"Stock alert","body":"spryngApiSMSGateway Message Alert","reference":"","credits":2.4,"scheduled_at":"2022-07-29T10:30:38+02:00","canceled_at":"","created_at":"2022-07-29T10:30:38+02:00","updated_at":"2022-07-29T10:30:38+02:00","links":{"self":"https:\/\/rest.spryngsms.com\/v1\/messages\/96e48be5-ea85-495d-ab97-09da4e46a5a2"}}