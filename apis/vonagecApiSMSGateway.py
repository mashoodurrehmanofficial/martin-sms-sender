try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *

import vonage 



@generalSmsAPIExceptionHandler
def vonagecApiSMSGatewaySingleton(data_packet):
    client = vonage.Client(key=data_packet['credentials']['api_key'], secret=data_packet['credentials']['api_secret'])
    sms = vonage.Sms(client)
    response = sms.send_message(
        { 
            'from':data_packet['message_title'], 
            "to": data_packet['receiver'],
            "text": data_packet['message_body'],
        }
    )
 
    if response["messages"][0]["status"] == "0":
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
