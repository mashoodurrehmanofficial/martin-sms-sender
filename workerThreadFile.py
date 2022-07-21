 
from PyQt5.QtCore import QThread,pyqtSignal  
# import uuid
from concurrent.futures import ThreadPoolExecutor
try:
    from configHandlerFile import configHandler 
    from smsAPIListingContainer import *
    from sharedMemory  import sharedMemory  

except:
    try: 
        from configHandlerFile import configHandler
    except: 
        from .configHandlerFile import configHandler
    try:
        from smsAPIListingContainer import *
    except:
        from .smsAPIListingContainer import * 
    try:
        from sharedMemory  import sharedMemory  
    except:
        from .sharedMemory  import sharedMemory
    
import time,json,datetime
    
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
            # print("iterable_macros_dict = ", iterable_macros_dict)
            max_counter = max([len(x) for x in list(iterable_macros_dict.values())]) 
            
            # print("max_counter = ", max_counter)
            
            for counter in range(max_counter):
                temp_message = message
                for iterable_macro in iterable_macros: 
                    current_macro_value = iterable_macros_dict[iterable_macro][counter%len(iterable_macros_dict[iterable_macro])]
                    temp_message = temp_message.replace(iterable_macro,current_macro_value)     
                    message_prototypes.append(temp_message)
                    print(temp_message)
        else:
            message_prototypes.append(message)
            
    # print("orignal message_prototypes len = ", len(message_prototypes))
    if total_contacts>len(message_prototypes):      
        message_prototypes = message_prototypes * (total_contacts - len(message_prototypes) + 1)
    message_prototypes = message_prototypes[:total_contacts]
    return message_prototypes     
    
    
    
    
def senderGatewayContainer(log,data):  
    log.emit("-"*50+"\n")
    log.emit("-> data in raw form ")
    log.emit(str(data))
    log.emit("-"*50+"\n")
    message_prototypes = getMessagePrototypes(data['message_body'], len(data['contact_list']) ) 
    service = data['service']
    contacts = data['contact_list']
    
    data_packets = [
        { 
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
    
 
    
    targetSMSGateway = None
    if service=='sinch.com':
        targetSMSGateway = sinchApiSMSGateway
    elif service=='clicksend.com':
        targetSMSGateway = clickSendApiSMSGateway
    elif service=='telnyx.com':
        targetSMSGateway = telnyxApiSMSGateway
    
    elif service=='messagebird.com':
        targetSMSGateway = messageBirdApiSMSGateway
    elif service=='twilio.com': 
        targetSMSGateway = twilioApiSMSGateway
    elif service=='d7networks.com':
        targetSMSGateway = d7networksApiSMSGateway
        
    elif service=='tyntec.com':
        targetSMSGateway = tyntecApiSMSGateway
    elif service=='vonage.co.uk':
        targetSMSGateway = vonagecApiSMSGateway
    elif service=='cm.com':
        targetSMSGateway = cmTextApiSMSGateway
        
         
    log.emit("Initiating ThreadPoolExecutor ...")
    log.emit(f"Target SMS Gateway function name = {targetSMSGateway}")
    max_workers = int(configHandler().getThreadsThreshold())
    max_workers = 5
    try:
        max_workers = int(configHandler().getThreadsThreshold())
    except:pass
    
    log.emit(f"Max Workers for ThreadPoolExecutor = {max_workers}")
    
    log.emit("Creating data packets for ThreadPoolExecutor")
    print('--> ', data['contact_list'])
    print('--> message_prototypes = ',message_prototypes)
    print('--> ',data['message_body'], len(data['contact_list']))
    
    api_service_configuration = configHandler().getServiceConfiguration(service)
    api_service_configuration = eval(str(api_service_configuration))
    print("api_service_configuration = ",api_service_configuration)
    print("api_service_configuration = ",type(api_service_configuration))
    request_load = int(api_service_configuration['request_load'])
    request_interval_wait = int(api_service_configuration['request_interval_wait'])
    
    
    
    message_prototypes = list(set(message_prototypes))
    contacts = contacts
    request_session_contacts_container = [contacts[x:x+request_load] for x in range(0, len(contacts), request_load)]
    print("-"*100)
    for request_session_index,request_session_contacts in enumerate(request_session_contacts_container):
        # Checking if stop button is pressed
        if sharedMemory.stop_btn_pressed:
            return
            
        
        
        cuurent_message = message_prototypes[ request_session_index%len(message_prototypes) ]
        
        log.emit(f"-"*200)
        log.emit(f"Current Request Session Index =  {request_session_index+1}/{len(request_session_contacts_container)} ")
        data_packet =   { 
            "service":data['service'],
            "credentials":data['credentials'],
            "receiver":request_session_contacts,
            "message_title":data['message_title'],
            "message_body":cuurent_message,
            "log":log,
        }
        
        print("data_packets = ",data_packet)
        
        
        print("request_session_index = ",request_session_index)
        print("request_session_contact = ",request_session_contacts)
        print("cuurent_message = ",cuurent_message)
        print("api_service_configuration = ",eval(str(api_service_configuration)))
        print("api_service_configuration = ",api_service_configuration['allow_bulk'] in [True,"True"] )
        
        
        
        # with ThreadPoolExecutor(max_workers=max_workers) as exe: 
        #     exe.map(targetSMSGateway,data_packet) 
        
        if api_service_configuration['allow_bulk'] in [True,"True"] :  
            # ->  Send Request t API
            targetSMSGateway(data_packet=data_packet) 
            # Checking if last request Session
            # print("**--**")
            # print(request_session_index !=len(request_session_contacts_container))
            # print(request_session_index )
            # print(len(request_session_contacts_container))
            # print("**--**") 
            if request_session_index !=len(request_session_contacts_container)-1:  
                # ->  Enable Stop button
                log.emit("ENABLE_STOP_BUTTON")
                # ->  time.sleep(request_interval_wait)
                for second in range(1,request_interval_wait+1):
                    time.sleep(1)
                    log.emit(f"[{datetime.datetime.today()}] | Seconds left = {request_interval_wait-second}")
                    print(f"[{datetime.datetime.today()}] | Seconds left = {request_interval_wait-second}")
                    print("sharedMemory.stop_btn_pressed = ", sharedMemory.stop_btn_pressed)
                    if sharedMemory.stop_btn_pressed:
                        log.emit("DISABLE_STOP_BUTTON")  
                        break 
                # ->  Dsiable Stop button
                log.emit("DISABLE_STOP_BUTTON")
                
             
            
            
        
        print("-"*50)
    
    
    return 
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