from django.db import models
import uuid
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
# Create your models here.

class ProductKeyTable(models.Model):
    name = models.CharField(max_length=200,blank=False, verbose_name="Username")
    key = models.CharField(max_length=100,default=str(uuid.uuid4()),verbose_name="Product Key")
    used = models.BooleanField(default=False, verbose_name="Already being used by another machine")
    allowed = models.BooleanField(default=True,verbose_name="Activate / Deactivate")
    class Meta:
        verbose_name = 'Product Key'

# method for updating
@receiver(post_save, sender=ProductKeyTable, dispatch_uid="update_uuid_val")
def update_uuid_val(sender, instance, **kwargs):
    current_uuid = instance.key
    # available_uuids = [str(x.key) for x in ProductKeyTable.objects.all()]
    # while current_uuid in available_uuids:
    #     current_uuid = str(uuid.uuid4())
    
    # instance.key = current_uuid 
    # instance.save()