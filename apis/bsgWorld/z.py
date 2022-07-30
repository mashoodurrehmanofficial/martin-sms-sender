import bsg_restapi as api


def bsgWorldApiSMSGatewaySingleton(data_packet):
    api_key = data_packet['credentials']['api_key']
    data_packet['receiver'] = [data_packet['receiver']] if type(data_packet['receiver']) is not list else data_packet['receiver']
    # recipients = [(api.Recipient) for x in data_packet['receiver']]
    
    client = api.SMSAPI(config={'api_key': api_key})
    response = client.send(message=api.SMSMessage(originator=data_packet["message_title"],body=data_packet["message_body"]), recipients=api.Recipient("447920498448"))
    # response = response.__dict__
    print(response)
    if response.get("result") and response['result'].get("id"):
        print("sent")
 
    
if __name__ == '__main__':
    credentials = {   
        "api_key": "live_fmUXxusYDiufPlwoZjLJ", 
        "auth_token": "NzIyM2Y5NDk5YzZiMzVjYjBmMjdiNzU1Y2E0Mzg3", 
    }
    # +13167815639 
    data_packet = {
        "credentials":credentials,
        "receiver":["+447920498428","+447920498123"],
        "message_title":"Stick alert",
        "message_body":"vonagecApiSMSGateway Message Alert",
    }
    res = bsgWorldApiSMSGatewaySingleton(data_packet=data_packet)
    # {'result': {'error': 0, 'errorDescription': 'No errors', 'reference': '3a11ad1e', 'id': 2512631998, 'price': 0.03813, 'currency': 'GBP'}}