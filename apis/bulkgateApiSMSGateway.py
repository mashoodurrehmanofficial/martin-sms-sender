try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *
#cell 12
# 9 - bulkgate    
# bulkgate.com - API: Application ID - 27605 | HTTP simple - ajrYOTN4wscifqa88d2qGh6IPAAHdQgop6fh3gRqYZOieCZ5Lv 
# https://help.bulkgate.com/docs/en/http-simple-transactional.html
# https://help.bulkgate.com/docs/en/http-advanced-transactional.html


# POST /bulkgate/api/2.0/advanced/transactional HTTP/1.1 
@generalSmsAPIExceptionHandler
def bulkgateApiSMSGatewaySingleton(data_packet):       
    url = """https://portal.bulkgate.com/api/1.0/simple/transactional"""
    
    params = {
        "application_id": data_packet["credentials"]['application_id'],
        "application_token": data_packet["credentials"]['application_token'],
        "number":data_packet["receiver"],
        # "number":"447700900000",
        'sender_id': data_packet["message_title"],
        'sender_id_value': data_packet["message_title"],
        "text": data_packet["message_body"],
        "country":"gb",  
    }
    
    
    response = requests.post(url,data=params)
    response = response.json()
    
    
    if response.get("data") and response['data'].get("status") == "accepted":
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
