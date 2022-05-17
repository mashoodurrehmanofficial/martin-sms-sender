from django.shortcuts import render
from django.http.response import JsonResponse
try:
    from .models import  *
except:
    from models import  *
    


# Create your views here.


def verifyProductKey(request,key):
    required_key = ProductKeyTable.objects.filter(key=str(key))
    if required_key.exists():
        required_key = required_key.first()
        return {
            "is_valid":True,
            "used":required_key.used,
            "allowed":required_key.allowed, 
        }
    
        
    return JsonResponse({
            "is_valid":False,
            "used":None,
            "allowed":None, 
        }) 
    