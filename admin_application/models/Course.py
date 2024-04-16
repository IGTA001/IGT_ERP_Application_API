from django.db import models
from datetime import datetime

class Course(models.Model):

      Course_id = models.BigAutoField(auto_created=True, primary_key=True, serialize = False)
      Course_name = models.CharField(max_length=1000, null=True)
      Course_Fees = models.FloatField(null=True)
      Course_Create_date = models.DateTimeField(default=datetime.now, null=True, blank=True)
      Course_Status = models.CharField(max_length=30, null=True)

      Create_date =  models.DateTimeField(default=datetime.now, null=True, blank=True)
      Update_date =  models.DateTimeField(default=datetime.now, null=True, blank=True)