
from helpers.sharedMemory  import sharedMemory  
try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *

# Completed
# 9 - smsbroadcast   
@generalSmsAPIExceptionHandler
def smsbroadcastApiSMSGatewaySingleton(data_packet):  
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']
    data_packet['receiver'] = ",".join(data_packet['receiver'][:15])
    username = data_packet["credentials"]['username']
    password = data_packet["credentials"]['password']
    from_ = data_packet['message_title']
    to = data_packet['receiver']
    message = data_packet['message_body']
       
    url = f"https://api.smsbroadcast.co.uk/api-adv.php?username={username}&password={password}&to={to}&from={from_}&message={message}"
    # url = "https://api.smsbroadcast.co.uk/api-adv.php?username=JasonW22&password=Stealth017???&to=447920498128&from=MyCompany& message=Hello%20World"



    if sharedMemory.stop_btn_pressed:return
    response = requests.get(url)
    response = str(response.text).lower()
    if "ok" in response:
        total_messages_sent = response.count("ok")
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
def smsbroadcastApiSMSGatewayBulk(data_packet):  
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']
    data_packet['receiver'] = ",".join(data_packet['receiver'][:15])
    username = data_packet["credentials"]['username']
    password = data_packet["credentials"]['password']
    from_ = data_packet['message_title']
    to = data_packet['receiver']
    message = data_packet['message_body']
       
    url = f"https://api.smsbroadcast.co.uk/api-adv.php?username={username}&password={password}&to={to}&from={from_}&message={message}"
    # url = "https://api.smsbroadcast.co.uk/api-adv.php?username=JasonW22&password=Stealth017???&to=447920498128&from=MyCompany& message=Hello%20World"


    if sharedMemory.stop_btn_pressed:return
    response = requests.get(url)
    response = str(response.text).lower()
    if "ok" in response:
        total_messages_sent = response.count("ok")
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