 
import time
from PyQt5.QtCore import QThread,pyqtSignal  
# import uuid
import requests
from concurrent.futures import ThreadPoolExecutor

try:
    from configHandlerFile import configHandler
    from balanceAPIListingContainer import *
    from smsAPIListingContainer import *
except:
    try:
        from configHandlerFile import configHandler
    except:
        from .configHandlerFile import configHandler
    try:
        from balanceAPIListingContainer import *
    except:
        from .balanceAPIListingContainer import * 
    
 
    
    
 
    
    
class remainingBalanceThread(QThread): 
    def __init__(self,service,credentials):
        super().__init__()
        self.service  = service  
        self.credentials  = eval(str(credentials))  
    
        
    balance_request_status = pyqtSignal(str)
    def run(self): 
        pass 
        service = self.service
        targetBalanceGateway = None
        # if service=='sinch.com':
        #     targetBalanceGateway = sinchApiSMSGateway
        # elif service=='clicksend.com':
        #     targetBalanceGateway = clickSendApiSMSGateway
        # elif service=='telnyx.com':
        #     targetBalanceGateway = telnyxApiSMSGateway
            
        if service=='messagebird':
            targetBalanceGateway = messageBirdApiBalanceGateway
        elif service=='twilio':
            targetBalanceGateway = twilioApiBalanceGateway
        elif service=='d7networks':
            targetBalanceGateway = d7networksApiBalanceGateway
        
        
        
        if targetBalanceGateway:
            response = targetBalanceGateway(credentials=self.credentials)
            print(self.credentials)
        else:
            response = "Not Available"  
        
        self.balance_request_status.emit(str(response))
        