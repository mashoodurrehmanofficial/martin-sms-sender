from django.shortcuts import render
from django.http.response import JsonResponse
try:
    from .models import  *
except:
    from models import  *
    


# Create your views here.


def verifyProductKey(request,key,machine_id):
    
    response = {
        "is_valid":False,
        "used":False,
        "allowed":True, 
    }
    
    required_key = ProductKeyTable.objects.filter(key=str(key))
    if required_key.exists():
        required_key = required_key.first()
        response['is_valid'] = True
        response['allowed'] = required_key.allowed
        if required_key.machine_id == '':
            # set machine id
            required_key.machine_id = str(machine_id)
            required_key.save()
        
        elif machine_id != required_key.machine_id:    
            response['used'] = True        
        
        
        
    
        
    return JsonResponse(response) 
    