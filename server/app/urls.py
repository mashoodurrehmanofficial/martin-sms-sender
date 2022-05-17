
from django.urls import path
from .views import * 
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [ 
               
    path('verifyProductKey/<str:key>/<str:machine_id>', verifyProductKey, name='verifyProductKey'),   
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

