try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *



# smsup.com
# https://app.smsup.es/api/3.0/docs/sms/send
@generalSmsAPIExceptionHandler
def smsupApiSMSGatewaySingleton(data_packet):  
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']
    payload ={ 
        "api_key":data_packet['credentials']['api_key'],  
        "messages":[  
            {
                "from":data_packet['message_title'],
                "to":x,
                "text":data_packet['message_body'],
            }
            for x in data_packet['receiver']]
        }
 
    headers = {"Content-Type": "application/json",'accept': "application/json"}
    response = requests.post("https://api.gateway360.com/api/3.0/sms/send",json.dumps( payload), headers=headers)
    response = response.json()
    if type(response.get("result") is list):
        total_messages_sent = len(response.get("result"))
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
def smsupApiSMSGatewayBulk(data_packet):  
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']
    payload ={ 
        "api_key":data_packet['credentials']['api_key'],  
        "messages":[  
            {
                "from":data_packet['message_title'],
                "to":x,
                "text":data_packet['message_body'],
            }
            for x in data_packet['receiver']]
        }
 
    headers = {"Content-Type": "application/json",'accept': "application/json"}
    response = requests.post("https://api.gateway360.com/api/3.0/sms/send",json.dumps( payload), headers=headers)
    response = response.json()
    if type(response.get("result") is list):
        total_messages_sent = len(response.get("result"))
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
    
    
    
    
if __name__ == '__main__':
    pass
