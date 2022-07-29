try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *
from clicksend_client.rest import ApiException
import clicksend_client
from clicksend_client import SmsMessage
 
# allow bulk if we use HTTP API 
# https://developers.clicksend.com/docs/http/v2/#ClickSend-v2-API-SMS
@generalSmsAPIExceptionHandler
def clickSendApiSMSGatewaySingleton(data_packet): 
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
 
    
    