import json
import pandas as pd,os,csv ,json


dir_path = os.path.dirname(__file__)
config_file_path = os.path.join(dir_path,"config.json") 


class  configHandler():
    def __init__(self):
        self.config_file_path = config_file_path 
        self.data = self.readDataFile(file_name=self.config_file_path) 
        
    def readDataFile(self,file_name):
        return eval(open(file_name, 'r', ).read()) 
 
    def updateDataFile(self,):
        with open(self.config_file_path, 'w') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)
    
    # Configuration Tab
    def getThreadsThreshold(self):
        return int(self.data['threads_threshold'])
    def setThreadsThreshold(self,new_threads_threshold):
        self.data['threads_threshold'] = new_threads_threshold
        self.updateDataFile()
            
            
    def getAllServices(self):
        return list(self.data['services'].keys())
        
    def getServiceCredentialsList(self,service):
        return list(self.data['services'][service])
    
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