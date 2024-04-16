from rest_framework.exceptions import APIException
from ..models import Staff
from datetime import datetime

def Designation_services(user,**data):
      try:
            desi= Staff.Designation.objects.create(
                  Designation_name = data.get('Designation_name'),
                  
               
            )
            return data.get('Designation_name')


      except APIException as e:
            raise(e)

def Get_Designation_detail(data):
      try:
            desi = Staff.Designation.objects.filter(Designation_id=data)
            return desi.values()
      
      except APIException as e:
            raise(e)

def Fetch_Designation_detail():
      try:
            desi = Staff.Designation.objects.all()
            values = desi.values()
            return values
      except APIException as e:
            raise(e)

def Delete_Designation_detail(**data):
      try :
            desi = Staff.Designation.objects.filter(Designation_id=data.get('Designation_id')).first()
            desi.delete()
            return "Successfully Deleted"

      except APIException as e:
            raise(e)

def Update_Designation_detail(**data):
      try :
            desi = Staff.Designation.objects.filter(Designation_id=data.get('Designation_id')).first()
            desi.Designation_name = data.get('Designation_name')
            desi.Update_date = datetime.now()
            desi.save()

            return desi.Designation_id

      except APIException as e:
            raise(e)