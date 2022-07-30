import os,traceback,requests,json,sys,inspect,base64
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 
try: 
    from helpers.sharedMemory  import sharedMemory  
except:
    from helpers.sharedMemory  import sharedMemory



def generalSmsAPIExceptionHandler(smsAPIGatewayCaller):
    # if sharedMemory.stop_btn_pressed:return
    
    def innerDecorator(data_packet):
        try:
            smsAPIGatewayCaller(data_packet)
        except:
            data_packet['log'].emit(str(traceback.format_exc()))
        
    return innerDecorator

