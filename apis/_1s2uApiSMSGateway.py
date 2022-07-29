try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *
 
# 1s2u.com - Username: qiv3jason.wi022 | Password: web12093 
# - API credentials are username and password 
# - API: https://api.1s2u.io/bulksms? 
# - Example: https://api.1s2u.io/bulksms?username=Your Username&password=Your Password&mt=Message Type&fl=Flash/None Flash Message &sid=Sender Name&mno=Mobile Number&msg=Message 
# use commas for bulk between numbers -> max: 15 


@generalSmsAPIExceptionHandler
def _1s2uApiSMSGatewaySingleton(data_packet):   
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']
    data_packet['receiver'] = ",".join(data_packet['receiver'][:15])
    username = data_packet["credentials"]['username']
    password = data_packet["credentials"]['password']
    sid = data_packet['message_title']
    mno = data_packet['receiver']
    msg = data_packet['message_body']
    
    url = f"https://api.1s2u.io/bulksms?username={username}&password={password}&mt=Message Type&fl=Flash/None Flash Message &sid={sid}&mno={mno}&msg={msg}"
    response = requests.get(url)
    print(response.text)
    if "ok" in str(response.text).lower():
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
def _1s2uApiSMSGatewayBulk(data_packet):   
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']
    data_packet['receiver'] = ",".join(data_packet['receiver'][:15])
    username = data_packet["credentials"]['username']
    password = data_packet["credentials"]['password']
    sid = data_packet['message_title']
    mno = data_packet['receiver']
    msg = data_packet['message_body']
    
    url = f"https://api.1s2u.io/bulksms?username={username}&password={password}&mt=Message Type&fl=Flash/None Flash Message &sid={sid}&mno={mno}&msg={msg}"
    response = requests.get(url)
    print(response.text)
    if "ok" in str(response.text).lower():
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