from django.db import models
from datetime import datetime

class Designation(models.Model):
    
    Designation_id = models.BigAutoField(auto_created=True, primary_key=True, serialize = False)
    Designation_name = models.CharField(max_length=1000, null=True)
    
    
      
    Create_date =  models.DateTimeField(default=datetime.now, null=True, blank=True)
    Update_date =  models.DateTimeField(default=datetime.now, null=True, blank=True)