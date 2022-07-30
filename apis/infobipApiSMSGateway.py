try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *
    


# # 11 - infobip    
# # infobip.com - API: 23c7a956498ccb3bb68bd40b1180b58d-114c0e72-a36c-40d9-9e41-d90415417a61 
# # pip install infobip-api-python-client
# # https://github.com/infobip/infobip-api-python-client#documentation
# # Configuration
# # Let's first set the configuration. For that you will need your specific URL. To see your base URL, log in to the Infobip API Resource hub with your Infobip credentials.
# https://www.infobip.com/docs/api/channels/sms/sms-messaging/outbound-sms/send-sms-message
@generalSmsAPIExceptionHandler
def infobipApiSMSGatewaySingleton(data_packet):
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']
    url = f'https://{data_packet["credentials"]["base_url"]}/sms/2/text/advanced'
    payload = json.dumps({
        "messages": [         
            {
                "destinations": [
                    {
                        "to": receiver
                    } 
                    for receiver  in data_packet['receiver']
                ],
                "from": data_packet["message_title"],
                "text": data_packet["message_body"],
            }
        ]
    })
    headers = {
        'Authorization': f'App {data_packet["credentials"]["auth_token"]}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post(url, data=payload, headers=headers)
    response = response.json()
    if response.get("messages"):
        total_messages_sent = len(response.get("messages"))
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
def infobipApiSMSGatewayBulk(data_packet):
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']
    url = f'https://{data_packet["credentials"]["base_url"]}/sms/2/text/advanced'
    payload = json.dumps({
        "messages": [         
            {
                "destinations": [
                    {
                        "to": receiver
                    } 
                    for receiver  in data_packet['receiver']
                ],
                "from": data_packet["message_title"],
                "text": data_packet["message_body"],
            }
        ]
    })
    headers = {
        'Authorization': f'App {data_packet["credentials"]["auth_token"]}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post(url, data=payload, headers=headers)
    response = response.json()
    if response.get("messages"):
        total_messages_sent = len(response.get("messages"))
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
    
