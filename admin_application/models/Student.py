from django.db import models
from datetime import datetime
import jsonfield

class Student_Details(models.Model):

      Enquiry_id = models.BigAutoField(auto_created=True, primary_key=True, serialize = False)
      Enquiry_date = models.DateField( null=True, blank=True)

      Student_name = models.CharField(max_length= 150,null= True)
      Father_name = models.CharField(max_length= 150,null= True)

      Date_birth = models.DateField( null=True, blank=True)
      Gender = models.CharField(max_length= 50,null= True)

      Blood_group = models.CharField(max_length= 50,null= True)

      Address = models.CharField(max_length= 350,null= True)
      City = models.CharField(max_length= 50,null= True)
      State =models.CharField(max_length= 50,null= True)
      zipCode = models.CharField(max_length= 50,null= True)
      Phone_number = models.BigIntegerField(unique=True,null=True)

      Email = models.EmailField(max_length= 150,null= True)
      Marital_status = models.CharField(max_length= 50,null= True)

      Qualification_code = models.CharField(max_length= 50,null= True)

      Counsellor_name = models.CharField(max_length= 50,null= True)
      Reference_name = models.CharField(max_length= 50,null= True)
      
      Course_name = models.CharField(max_length= 250,null= True)
      Course_fee = models.FloatField(null=True)

      Discount = models.CharField(max_length= 50,null=True)
      Discount_fee = models.CharField(max_length= 50,null=True)
      
      Total_course_fee = models.FloatField(null=True)
      
      status = models.CharField(max_length= 150,null= True, default="Enquiry")
      Create_date =  models.DateTimeField(default=datetime.now, null=True, blank=True)
      Update_date =  models.DateTimeField(default=datetime.now, null=True, blank=True)

class Student_Qualification(models.Model):
      Qualification_id = models.BigAutoField(auto_created=True, primary_key=True, serialize = False)
      Student_name = models.CharField(max_length= 150,null= True)
      Qualification_name = jsonfield.JSONField()

      Qualification_code = models.CharField(max_length= 50,null= True,unique=True)
     

      Create_date =  models.DateTimeField(default=datetime.now, null=True, blank=True)
      Update_date =  models.DateTimeField(default=datetime.now, null=True, blank=True)