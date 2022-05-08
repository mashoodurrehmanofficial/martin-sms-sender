import json
import os

config_prototype = {
    "threads_threshold": 5,
    "services": {
        "sinch.com": [ {  "service_plan_id": "",  "api_token": ""  }],
        "clicksend.com": [  { "username": "", "api_key": "" }  ],
        "telnyx.com": [ { "api_key": "",  "messaging_profile_id": ""  }  ] 
    }
}




dir_path = os.path.dirname(__file__)
config_file_path = os.path.join(dir_path,"config.json") 
if not os.path.exists(config_file_path):
    config_file_path = os.path.join(os.getcwd(),"config.json") 



class  configHandler():
    def __init__(self):
        self.config_file_path = config_file_path 
        self.data = self.readDataFile(file_name=self.config_file_path) 
        
    def makeSureConfigFileExists(self):
        if not os.path.exists(self.config_file_path):
            self.data = config_prototype
            self.updateDataFile()
            
            
            
            
            
    def readDataFile(self,file_name):
        self.makeSureConfigFileExists()
        return eval(open(file_name, 'r', ).read()) 
 
    def updateDataFile(self,):
        with open(self.config_file_path, 'w') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)
    
    # Configuration Tab
    def getThreadsThreshold(self):
        # threshold = int(self.data['threads_threshold'])
        return int(self.data['threads_threshold'])
    
    def setThreadsThreshold(self,new_threads_threshold):
        self.data['threads_threshold'] = new_threads_threshold
        self.updateDataFile()
            
            
    def getAllServices(self):
        return list(self.data['services'].keys())[:3]
        
    def getServiceCredentialsList(self,service):
        return list(self.data['services'][service][1:])
    
    def addServiceCredentials(self,service,creds):
        if len(self.data['services'][service])>0:
            cred_prototype = self.data['services'][service][0]
            if sorted(list(cred_prototype.keys())) != sorted(list(creds.keys())):
                return cred_prototype
            
        self.data['services'][service].append(creds)
        self.updateDataFile()
        return True
    
    
    def removeServiceCredentials(self,service,credential_index):
        try:
            del self.data['services'][service][credential_index]
            self.updateDataFile()
        except:
            pass
            
            
    
            
            
            
            
            
            
config = configHandler()
# print(config.removeServiceCredentials('service_name1',-1))