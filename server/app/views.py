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
        return JsonResponse({"is_valid":True})
        
    return JsonResponse({"is_valid":False}) 
    