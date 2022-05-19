import requests
import clicksend_client
from clicksend_client import SmsMessage
from clicksend_client.rest import ApiException

# try:
#     from configHandlerFile import configHandler 
# except:
#     from .configHandler import configHandler 




def sinchApiSMSGateway(data_packet):
    service_plan_id = data_packet['credentials']['service_plan_id']
    url = "https://us.sms.api.sinch.com/xms/v1/" + service_plan_id + "/batches"
    payload = {
        "from": data_packet['message_title'],
        "to": [data_packet['receiver']],
        "body": data_packet['message_body']
    } 
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {data_packet['credentials']['api_token']}"
    } 
    
    
    response = requests.post(url, json=payload, headers=headers,timeout=60)
    response = response.json()
    data_packet['log'].emit("-"*50+"\n"+str(response))
    print(response)
    if response.get('id') is not None:  
        print(f"-> Message sent to {data_packet['receiver']}")
        print(response['id'])
        data_packet['log'].emit("-"*50+"\n")
        data_packet['log'].emit(f"-> Message sent to {data_packet['receiver']}")
        data_packet['log'].emit(str(response['id']))
        data_packet['log'].emit("-"*50+"\n")
    # print(data)
 


def clickSendApiSMSGateway(data_packet): 
    configuration = clicksend_client.Configuration()
    configuration.username = data_packet['credentials']['username']
    configuration.password = data_packet['credentials']['api_key']
    api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
    sms_message = SmsMessage(
        source="php",
        _from=data_packet['message_title'],
        body=data_packet['message_body'],
        to=data_packet['receiver'],
    )
    sms_messages = clicksend_client.SmsMessageCollection(messages=[sms_message])
    try: 
        api_response = api_instance.sms_send_post(sms_messages)
        print(api_response) 
        data_packet['log'].emit("-"*50+"\n"+str(api_response))
        try:
            api_response = eval(api_response)
            if str(api_response.get('http_code')) == str(200) and str(api_response.get('response_code')) == 'SUCCESS' :
                print(f"-> Message sent to {data_packet['receiver']}")
                data_packet['log'].emit("-"*50+"\n")
                data_packet['log'].emit(f"-> Message sent to {data_packet['receiver']}")
        except:
            print("Exception when while evaluating eval(api_response) from clicksend API")
            data_packet['log'].emit("-"*50+"\n")
            data_packet['log'].emit("Exception when while evaluating eval(api_response) from clicksend API"  )
                
            
    except ApiException as e:
        print("Exception when calling SMSApi->sms_send_post: %s\n" % e)
        data_packet['log'].emit("-"*50+"\n")
        data_packet['log'].emit("Exception when calling SMSApi->sms_send_post: %s\n" % e)
 
    
    
    
    
    
    
def telnyxApiSMSGateway(data_packet):
    headers = { 
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f"Bearer {data_packet['credentials']['api_key']}",
    }
    
    # data_packet['receiver'] = str(data_packet['receiver']).strip().replace
    
    data_packet['receiver'] = data_packet['receiver'] if str(data_packet['receiver']).startswith("+") else "+"+str(data_packet['receiver'])
    # print(f"-- {data_packet['receiver']}")
    json_data = {
        'from':data_packet['message_title'], 
        "messaging_profile_id": data_packet['credentials']['messaging_profile_id'],
        'to': data_packet['receiver'],
        'text': data_packet['message_body'], 
    } 

    response = requests.post('https://api.telnyx.com/v2/messages', headers=headers, json=json_data,timeout=60) 
    response = response.json() 
    data_packet['log'].emit("-"*50+"\n")
    data_packet['log'].emit(str(response))
    if type(response['data']) is dict and response['data']['id'] not in ['',None]:
        # print(f"-> Message sent to {data_packet['receiver']}")
        data_packet['log'].emit("-"*50+"\n")
        data_packet['log'].emit(f"-> Message sent to {data_packet['receiver']}")
        # print(response['data']['id']) 
        data_packet['log'].emit(str(response['data']['id'])) 
        data_packet['log'].emit("-"*50+"\n")
    
    
    
if __name__=="__main__": 
    pass