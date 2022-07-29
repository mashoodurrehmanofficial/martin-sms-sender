try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *
from twilio.rest import Client 

        
        
@generalSmsAPIExceptionHandler   
def twilioApiSMSGateway(data_packet):   
    account_sid =  data_packet['credentials']['account_sid']
    auth_token =  data_packet['credentials']['auth_token']
    client = Client(account_sid, auth_token)    
    try:
        message = client.messages.create(
                    from_=data_packet['message_title'],
                    to=data_packet['receiver'],
                    body=data_packet['message_body'],
                )
    
    except Exception as e:
        message=traceback.print_exc()
        print(message) 
    data_packet['log'].emit(str(message))  
    try:
        message_sid = str(message.sid)
        if len(message_sid)>5:
            print(f"-> Message sent to {data_packet['receiver']}")
            print(message_sid) 
            data_packet['log'].emit("-"*50+"\n")
            data_packet['log'].emit(f"-> Message sent to {data_packet['receiver']}")
            data_packet['log'].emit(str(message_sid))
            data_packet['log'].emit("-"*50+"\n")
    except:
        pass