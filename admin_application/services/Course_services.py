from rest_framework.exceptions import APIException
from ..models import Course
from datetime import datetime

def Course_services(user,**data):
      try:
            cour = Course.Course.objects.create(
                  Course_name = data.get('Course_name'),
                  Course_Fees = data.get('Course_Fees'),
                  Course_Status = data.get('Course_Status')
            )
            return data.get('Course_name')


      except APIException as e:
            raise(e)

def Get_Course_detail(data):
      try:
            cour = Course.Course.objects.filter(Course_id=data).values()
            return cour
      except APIException as e:
            raise(e)

def Fetch_course_detail():
      try:
            cour = Course.Course.objects.all()
            values = cour.values()
            return values
      except APIException as e:
            raise(e)

def Delete_course_detail(**data):
      try :
            cour = Course.Course.objects.filter(Course_id=data.get('Course_id')).first()
            cour.delete()
            return "Successfully Deleted"

      except APIException as e:
            raise(e)

def Update_course_detail(**data):
      try :
            cour = Course.Course.objects.filter(Course_id=data.get('Course_id')).first()
            cour.Course_name = data.get('Course_name')
            cour.Course_Fees = data.get('Course_Fees')
            cour.Course_Status = data.get('Course_Status')
            cour.Update_date = datetime.now()
            cour.save()

            return cour.Course_id

      except APIException as e:
            raise(e)