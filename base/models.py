from django.db import models
import uuid

# Create your models here.
# base model for commen data like uuid and created at updated at 
class BaseModel(models.Model):
    uuid = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False) 
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
