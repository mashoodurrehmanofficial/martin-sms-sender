#cell 4
import plivo
# 9 - plivo.com
# https://www.plivo.com/docs/sms/api/message#send-a-message

# - NO BULK
def plivoApiSMSGateway(data_packet):
    
    auth_id = data_packet['credentials']['auth_id']
    auth_token = data_packet['credentials']['auth_token']
    client = plivo.RestClient(auth_id,auth_token)
    response = client.messages.create(
        src='plivo MSG',
        dst='+447826926850',
        text='Hello, this is plivo', 
        )
    print(response)
    #prints only the message_uuid
    print(response.message_uuid)
    
  

credentials = {   
    "auth_id": "MAMGNIN2E1MDLIM2Q0YJ", 
    "auth_token": "NzIyM2Y5NDk5YzZiMzVjYjBmMjdiNzU1Y2E0Mzg3", 
    "sender_id": "", 
    "phlo_id": "", 
}
# +13167815639 
data_packet = {
    "credentials":credentials,
    "receiver":"+923167815639",
    "message_title":"Stick alert",
    "message_body":"vonagecApiSMSGateway Message Alert",
}
res = plivoApiSMSGateway(data_packet=data_packet)

