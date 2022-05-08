 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys,random,uuid,json,time
from concurrent.futures import ThreadPoolExecutor
try:
    from configHandlerFile import configHandler
    from smsAPIListingContainer import *
except:
    from .configHandlerFile import configHandler
    from .smsAPIListingContainer import *
    
def demoSender(data):
    # print(data)  
    print(f"-"*10)  
    data['log'].emit((str(uuid.uuid4()))) 
    
def senderGatewayContainer(log,data):   
    service = data['service']
    log.emit("Creating data packets for ThreadPoolExecutor")
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
         
    log.emit("Initiating ThreadPoolExecutor ...")
    log.emit(f"Target SMS Gateway function name = {targetSMSGateway}")
    max_workers = int(configHandler().getThreadsThreshold())
    max_workers = 5
    try:
        max_workers = int(configHandler().getThreadsThreshold())
    except:pass
    
    log.emit(f"Max Workers for ThreadPoolExecutor = {max_workers}")
    
    with ThreadPoolExecutor(max_workers=max_workers) as exe: 
        exe.map(targetSMSGateway,data_packets) 
    
    
    
    
class workerThread(QThread): 
    def __init__(self,service,credentials,message_title,contact_list,message_body):
        super().__init__()
        self.service  = service
        self.credentials  = credentials
        self.message_title  = message_title
        self.contact_list  = contact_list
        self.message_bod  = message_body 
        
    log_input_box_component = pyqtSignal(str)
    def run(self):
        print("->   started")
        data = { 
            "service":self.service,
            "credentials":self.credentials,
            "contact_list":self.contact_list,
            "message_title":self.message_title,
            "message_body":self.message_bod,
        
        }
        self.log_input_box_component.emit("Starting senderGatewayContainer ...")
        senderGatewayContainer(log=self.log_input_box_component,data=data)
        self.log_input_box_component.emit("Operation Completed !")
        print("->   ended")