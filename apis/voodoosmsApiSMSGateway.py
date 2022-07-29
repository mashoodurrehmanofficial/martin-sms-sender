try:
    from _sharedFuncsVaribales import *
except:
    from ._sharedFuncsVaribales import *


# https://www.voodoosms.com/api/http/send-sms#single-textual-message-to-multiple-destinations
# https://www.voodoosms.com/api/rest/introduction#getting-started
@generalSmsAPIExceptionHandler
def voodoosmsApiSMSGateway(data_packet): 
    
    headers = {
        'Authorization': f'Bearer {data_packet["credentials"]["key"]}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {   "to": data_packet['receiver'],  "from": data_packet['message_title'],   "msg": data_packet['message_body']   }
    response = requests.post('https://api.voodoosms.com/sendsms', headers=headers, data=json.dumps(data))
    response = response.json()
    
    
    
    
    
 