 
from PyQt5.QtCore import QThread,pyqtSignal   

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
        service = self.service
        targetBalanceGateway = None 
        if service=='messagebird.com':
            targetBalanceGateway = messageBirdApiBalanceGateway
        elif service=='twilio.com':
            targetBalanceGateway = twilioApiBalanceGateway
        elif service=='d7networks.com':
            targetBalanceGateway = d7networksApiBalanceGateway
        elif service=='vonage.co.uk':
            targetBalanceGateway = vonageApiBalanceGateway
        
        
        
        if targetBalanceGateway:
            response = targetBalanceGateway(credentials=self.credentials)
            print(self.credentials)
        else:
            response = "Not Available"  
        
        self.balance_request_status.emit(str(response))
        