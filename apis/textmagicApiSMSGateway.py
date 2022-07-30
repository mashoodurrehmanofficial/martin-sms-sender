
from helpers.sharedMemory  import sharedMemory  

try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *

# pip install textmagic
# https://www.textmagic.com/docs/api/python/
# https://www.textmagic.com/docs/api/
from urllib.parse import urlencode




@generalSmsAPIExceptionHandler
def textmagicApiSMSGatewaySingleton(data_packet):  
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']
    data_packet['receiver'] = ",".join(data_packet['receiver'])
    username = data_packet["credentials"]['username']
    token =  data_packet["credentials"]['token']
    
    
    if sharedMemory.stop_btn_pressed:return 
    data = { 
        # 'from':data_packet['message_title'],
        'phones': data_packet['receiver'],
        'text': data_packet['message_body'],
    }
    url = 'https://rest.textmagic.com/api/v2/messages'
    headers =  {
        'User-agent': 'textmagic-python/2.0.3 (Python 3.8.0)',
        'Accept-Charset': 'utf-8',
        'Accept-Language': 'en-us',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'X-TM-Username': username,
        'X-TM-Key': token, 
    }
    response = requests.post(url,headers=headers,data=urlencode(data))
    response = response.json()
    if response.get("id"):
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
    print(str(response))
    
    
    
    
@generalSmsAPIExceptionHandler
def textmagicApiSMSGatewayBulk(data_packet):  
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']
    data_packet['receiver'] = ",".join(data_packet['receiver'])
    username = data_packet["credentials"]['username']
    token =  data_packet["credentials"]['token']
    
    
    
    if sharedMemory.stop_btn_pressed:return  
    data = { 
        # 'from':data_packet['message_title'],
        'phones': data_packet['receiver'],
        'text': data_packet['message_body'],
    }
    url = 'https://rest.textmagic.com/api/v2/messages'
    headers =  {
        'User-agent': 'textmagic-python/2.0.3 (Python 3.8.0)',
        'Accept-Charset': 'utf-8',
        'Accept-Language': 'en-us',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'X-TM-Username': username,
        'X-TM-Key': token, 
    }
    response = requests.post(url,headers=headers,data=urlencode(data))
    response = response.json()
    if response.get("id"):
        total_messages_sent = str(data_packet['receiver']).count(",") + 1
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
    

    
if __name__ == '__main__':
    pass
# {'id': 680023734, 'href': '/api/v2/messages/680023734', 'type': 'message', 'sessionId': 285236393, 'bulkId': None, 'messageId': 680023734, 'scheduleId': None, 'chatId': None}
