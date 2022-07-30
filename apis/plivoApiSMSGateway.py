try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *
    
import plivo
# 9 - plivo.com
# https://www.plivo.com/docs/sms/api/message#send-a-message


@generalSmsAPIExceptionHandler
def plivoApiSMSGatewaySingleton(data_packet):
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']
    data_packet['receiver'] = "<".join(data_packet['receiver'])
    
    auth_id = data_packet['credentials']['auth_id']
    auth_token = data_packet['credentials']['auth_token']
    client = plivo.RestClient(auth_id,auth_token)
    response = client.messages.create(
        src=data_packet['message_title'],
        dst=data_packet['receiver'] ,
        text=data_packet['message_body'], 
        )
    response = response.__dict__
    if response.get("api_id"):
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



@generalSmsAPIExceptionHandler
def plivoApiSMSGatewayBulk(data_packet):
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']
    data_packet['receiver'] = "<".join(data_packet['receiver'])
    
    auth_id = data_packet['credentials']['auth_id']
    auth_token = data_packet['credentials']['auth_token']
    client = plivo.RestClient(auth_id,auth_token)
    response = client.messages.create(
        src=data_packet['message_title'],
        dst=data_packet['receiver'] ,
        text=data_packet['message_body'], 
        )
    response = response.__dict__
    if response.get("api_id"):
        total_messages_sent = str(data_packet['receiver']).count("<") + 1
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