from CMText.TextClient import TextClient 



def cmTextApiSMSGateway(data_packet):
    client = TextClient(apikey=data_packet['credentials']['api_key']) 
    receiver = data_packet['receiver']
    if type(receiver) is not list:
        receiver = [receiver] 
    response = client.SendSingleMessage(message=data_packet['message_body'],from_=data_packet['message_title'], to=receiver)  
    # response = client.send()
    print(response)
    print(response.json())
    
    # total_messages_sent = res.get("messages")
    # if total_messages_sent:
    #     total_messages_sent = len(total_messages_sent)
    # else:
    #     total_messages_sent = 0
    
    # return response.json()
     

credentials = {   
    "api_key": "b43c8147-6df1-4d5e-9dc4-03df4cb0740b", 
}
# +13167815639 
data_packet = {
    "credentials":credentials,
    "receiver": ["+923167815639",] ,
    "message_title":"alert",
    "message_body":"cmTextApiSMSGateway Message Alert",
}
response = cmTextApiSMSGateway(data_packet=data_packet)