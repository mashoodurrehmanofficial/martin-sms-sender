 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys,random,uuid,json,time
from concurrent.futures import ThreadPoolExecutor
try:
    from configHandler import configHandler
    from smsAPIListingContainer import *
except:
    from .smsAPIListingContainer import *
    
def demoSender(data):
    # print(data)  
    print(f"-"*10)  
    data['log'].emit((str(uuid.uuid4()))) 
    
def senderGatewayContainer(log,data):   
    service = data['service']
    data_packets = [
        {
            "receiver_index":receiver_index+1,
            "service":data['service'],
            "credentials":data['credentials'],
            "receiver":receiver,
            "message_title":data['message_title'],
            "message_body":data['message_body'],
            "log":log,
        }
        for receiver_index,receiver in enumerate(data['contact_list'])
    ] 
    targetSMSGateway = demoSender
    if service=='sinch.com':
        targetSMSGateway = sinchApiSMSGateway
    elif service=='clicksend.com':
        targetSMSGateway = clickSendApiSMSGateway
    elif service=='telnyx.com':
        targetSMSGateway = telnyxApiSMSGateway
    
    # print(type(data['credentials']))
         
    with ThreadPoolExecutor(max_workers=5) as exe: 
        exe.map(targetSMSGateway,data_packets) 
    
    
    
    
class workerThread(QThread): 
    def __init__(self,service,credentials,message_title,contact_list,message_body):
        super().__init__()
        self.service  = service
        self.credentials  = credentials
        self.message_title  = message_title
        self.contact_list  = contact_list
        self.message_bod  = message_body

        
        
        
    update_component = pyqtSignal(str)
    def run(self):
        print("->   started")
        data = { 
            "service":self.service,
            "credentials":self.credentials,
            "contact_list":self.contact_list,
            "message_title":self.message_title,
            "message_body":self.message_bod,
        
        }
        senderGatewayContainer(log=self.update_component,data=data)
        print("->   ended")