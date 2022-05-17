 
from PyQt5.QtCore import QThread,pyqtSignal  
# import uuid
import requests
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
    
    
 
    
    
 
    
    
class serverThread(QThread): 
    def __init__(self,key,machine_id):
        super().__init__()
        self.key  = key 
        self.machine_id  = machine_id 
    
        
    activation_request_status = pyqtSignal(str)
    def run(self):
        print("calling request")
        url = f'http://localhost:8000/api/verifyProductKey/{self.key}/{self.machine_id}'
        url = f'https://martin12345.pythonanywhere.com/api/verifyProductKey/{self.key}/{self.machine_id}'
        response = requests.get(url).json()
        self.activation_request_status.emit(str(response))
        