 
from PyQt5.QtCore import QThread,pyqtSignal  
# import uuid
from concurrent.futures import ThreadPoolExecutor
try:
    from configHandlerFile import configHandler
    from smsAPIListingContainer import *
except:
    try:
        from configHandlerFile import configHandler
    except:
        from .configHandlerFile import configHandler
    try:
        from smsAPIListingContainer import *
    except:
        from .smsAPIListingContainer import * 
    
    
import time
    
def getMessagePrototypes(message,total_contacts):
    message_prototypes = [] 
    if '##' not in message: 
        message_prototypes.append(message) 
        
    else:
        detected_macros = [x for x in message.split() if "#" in str(x) ]
        # detected_macros = [x for x in message.split() if x.startswith("##") and x.endswith("##")]
        detected_macros = ["##"+x.split("##")[1]+"##" for x in detected_macros]
        # print("detected_macros = ",detected_macros)
        
        detected_macros = [x for x in detected_macros if x.replace("#","") in configHandler().getAvailableMacros()]
        iterable_macros = [x for x in detected_macros  if type(configHandler().getMacroBody(key=str(x).replace("#",""))) is list]
        non_iterable_macros = [x for x in detected_macros  if type(configHandler().getMacroBody(key=str(x).replace("#",""))) is not list]
        # print("all = ", configHandler().getAvailableMacros())
        # print("detected_macros = ",detected_macros)
        # print("iterable_macros = ",iterable_macros)
        # print("non_iterable_macros = ",non_iterable_macros)
        
        
        for non_iterable_macro in non_iterable_macros:    
            message = message.replace(non_iterable_macro,configHandler().getMacroBody(key=str(non_iterable_macro).replace("#","")))
        if len(iterable_macros)>0:
            temp_iterable_macros_dict = [{x: configHandler().getMacroBody(key=str(x).replace("#",""))  } for x in iterable_macros]
            iterable_macros_dict = {}
            [iterable_macros_dict.update(x) for x in temp_iterable_macros_dict]
            
            # print(iterable_macros_dict)
            
            max_counter = max([len(x) for x in list(iterable_macros_dict.values())]) 
            for counter in range(max_counter):
                temp_message = message
                for iterable_macro in iterable_macros: 
                    current_macro_value = iterable_macros_dict[iterable_macro][counter%len(iterable_macros_dict[iterable_macro])]
                    temp_message = temp_message.replace(iterable_macro,current_macro_value)     
                # print(temp_message)
                message_prototypes.append(temp_message)
        else:
            message_prototypes.append(message)
    message_prototypes = message_prototypes * (total_contacts - len(message_prototypes) + 1)
    message_prototypes = message_prototypes[:total_contacts]
    return message_prototypes     
    
    
    
    
    
    
    
# def demoSender(data):
#     # print(data)  
#     print(f"-"*10)  
#     data['log'].emit((str(uuid.uuid4()))) 
    
def senderGatewayContainer(log,data):  
    log.emit("-"*50+"\n")
    log.emit("-> data in raw form ")
    log.emit(str(data))
    log.emit("-"*50+"\n")
    
    message_prototypes = getMessagePrototypes(data['message_body'], len(data['contact_list']) ) 
    service = data['service']
    log.emit("Creating data packets for ThreadPoolExecutor")
    data_packets = [
        {
            # "receiver_index":receiver_index+1,
            "service":data['service'],
            "credentials":data['credentials'],
            "receiver":receiver,
            "message_title":data['message_title'],
            "message_body":message_text,
            "log":log,
        }
        for message_text,receiver in zip( message_prototypes ,data['contact_list'])
    ] 
    log.emit("-"*50+"\n")
    log.emit("-> Data Packets ")
    log.emit(str(data_packets))
    log.emit("-"*50+"\n")
    # log.emit(str(data_packets ))
    # print(data_packets)
    # return
    
    targetSMSGateway = None
    if service=='sinch.com':
        targetSMSGateway = sinchApiSMSGateway
    elif service=='clicksend.com':
        targetSMSGateway = clickSendApiSMSGateway
    elif service=='telnyx.com':
        targetSMSGateway = telnyxApiSMSGateway
    
    elif service=='messagebird':
        targetSMSGateway = messageBirdApiSMSGateway
    elif service=='twilio': 
        targetSMSGateway = twilioApiSMSGateway
    elif service=='d7networks':
        targetSMSGateway = d7networksApiSMSGateway
        
    elif service=='tyntec.com':
        targetSMSGateway = tyntecApiSMSGateway
    elif service=='vonage':
        targetSMSGateway = vonagecApiSMSGateway
        
        
    
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
    def __init__(self,service,credentials,message_title,contact_list,message_body,timer_difference):
        super().__init__()
        self.service  = service
        self.credentials  = credentials
        self.message_title  = message_title
        self.contact_list  = contact_list
        self.message_body  = message_body 
        self.timer_difference  = timer_difference 
    
        
    log_input_box_component = pyqtSignal(str)
    def run(self):
        print(f"-> Waiting for {self.timer_difference} seconds")
        time.sleep(self.timer_difference)
        print("->   started")
        data = { 
            "service":self.service,
            "credentials":self.credentials,
            "contact_list":self.contact_list,
            "message_title":self.message_title,
            "message_body":self.message_body,
        
        }
        self.log_input_box_component.emit("Starting senderGatewayContainer ...")
        senderGatewayContainer(log=self.log_input_box_component,data=data)
        self.log_input_box_component.emit("Operation Completed !")
        print("->   ended")