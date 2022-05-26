
import os,uuid
from json import dump
 

config_prototype = {
    "threads_threshold": 5,
    "prodcut_key":"",
    "services": {
        "vonage.co.uk":[{       "api_key": "",    "api_secret": "",}],
        "tyntec.com":[{  "api_key": "",}],
        "d7networks.com":[{    "username": "",   "password": "",  "auth_token": "", }],
        "twilio.com":[{     "account_sid" : "",  "auth_token" : ""  }],
        "messagebird.com":[ {   "access_key": ""   }  ],
        "sinch.com": [ {  "service_plan_id": "",  "api_token": ""  }],
        "clicksend.com": [  { "username": "", "api_key": "" }  ],
        "telnyx.com": [ { "api_key": "",  "messaging_profile_id": ""  }  ] 
    },
    "templates": [],
    "macros": []
}


activation_file_path = os.path.join(os.environ['WINDIR'] , "custom-machine-id-quicksms.txt")

dir_path = os.path.dirname(__file__)
config_file_path = os.path.join(dir_path,"config.json") 
icon_file_path = os.path.join(dir_path,"data","icon.png") 
if not os.path.exists(config_file_path):
    config_file_path = os.path.join(os.getcwd(),"config.json") 
    icon_file_path = os.path.join(os.getcwd(),"data","icon.png") 



class  configHandler():
    def __init__(self):
        self.config_file_path = config_file_path 
        self.data = self.readDataFile(file_name=self.config_file_path) 
        self.icon_file_path = icon_file_path 
        
    def makeSureConfigFileExists(self):
        if not os.path.exists(self.config_file_path):
            self.data = config_prototype
            self.updateDataFile()
            
    
    def setMachineId(self):
        if not os.path.exists(activation_file_path):
            with open(activation_file_path,"w",encoding="utf-8") as file:
                file.write(str(uuid.uuid4())+str(uuid.uuid4()))
            
            
    def getMachineId(self):
        with open(activation_file_path,"r",encoding="utf-8") as file:
            machine_id =  str(file.read()).replace("\n","")
            if len(machine_id)>10:
                return machine_id
            return None
     
     
    def getCredentialsPrototype(self,service):
        return self.data['services'][service][0]
    
    def getProductKey(self):
        return str(self.data['prodcut_key'])
    
    def setproductKey(self,new_key):
        self.data['prodcut_key'] = str(new_key)
        self.updateDataFile()
          
    def getIconFilePath(self):
        return self.icon_file_path
            
            
    def readDataFile(self,file_name):
        self.makeSureConfigFileExists()
        return eval(open(file_name, 'r', ).read()) 
 
    def updateDataFile(self,):
        with open(self.config_file_path, 'w') as f:
            dump(self.data, f, ensure_ascii=False, indent=4)
    
    # Configuration Tab
    def getThreadsThreshold(self):
        return int(self.data['threads_threshold'])
    
    def setThreadsThreshold(self,new_threads_threshold):
        self.data['threads_threshold'] = new_threads_threshold
        self.updateDataFile()
            
            
    def getAllServices(self):
        return sorted(list(self.data['services'].keys())[:len(config_prototype['services'])])

        
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
            
    def getAvailableTemplates(self):
        return [list(x.keys())[0] for x in self.data['templates']]
    
    def getAvailableMacros(self):
        return [list(x.keys())[0] for x in self.data['macros']]
    
    
    def getTemplatesBody(self,key):
        for x in self.data['templates']:
            if list(x.keys())[0]==key:
                return x[key]
        return '' 
    
    
    def getMacroBody(self,key):
        for x in self.data['macros']:
            if list(x.keys())[0]==key:
                return x[key]        
        return '' 
    
    
    
    def getTemplateMacroList(self,key):
        temp = self.data[key]
        temp = [
            f"{list(x.keys())[0]} - {list(x.values())[0]}"    for x in temp
        ] 
        return temp
    
    def addNewTemplateMacro(self,key,value):
        available_keys = sum([list(x.keys()) for x  in self.data[key]],[])
        incoming_key = list(value.keys())[0]
        if incoming_key in available_keys:
            return "duplicate"
        
        self.data[key].append(value)
        self.updateDataFile()
            
            
    def deleteTemplateMacroRecord(self,key,index):
        try:
            del self.data[key][index]
            self.updateDataFile()
        except:
            pass
            
        self.updateDataFile()
            
            

if __name__ == '__main__':        
    config = configHandler()
    print(config.getTemplatesBody(key='Body2'))