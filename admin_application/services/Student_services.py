from rest_framework.exceptions import APIException
from ..models import Course, Student
from datetime import datetime

def Enquiry_services(**data):
      try: 
            stud = Student.Student_Details.objects.create(
                  Enquiry_date =data.get("Enquiry_date"),
                  Student_name=data.get("Student_name"),
                  Father_name=data.get("Father_name"),
                  Date_birth=data.get("Date_birth"),
                  Gender=data.get("Gender"),
                  Blood_group=data.get("Blood_group"),
                  Address=data.get("Address"),
                  City = data.get("City"),
                  State = data.get("State"),
                  zipCode = data.get("zipCode"),
                  Phone_number=data.get("Phone_number"),
                  Email=data.get("Email"),
                  Marital_status=data.get("Marital_status"),
                  Qualification_code=data.get("Qualification_code"),
                  Counsellor_name=data.get("Counsellor_name"),
                  Reference_name=data.get("Reference_name"),
                  Course_name=data.get("course_name"),
                  Course_fee=data.get("Course_fee"),
                  Discount=data.get("Discount"),
                  Discount_fee=data.get("Discount_fee"),
                  Total_course_fee=data.get("Total_course_fee"),
            )
            return data.get("Student_name")
            
      
      except APIException as e :
            raise(e)

def Get_Enquiry_detail(data):
      try:
            stud = Student.Student_Details.objects.filter(Enquiry_id=data).values()
            return stud
      except APIException as e:
            raise(e)

def Fetch_Enquiry_detail():
      try:
            stud = Student.Student_Details.objects.all().values()
            return stud
      except APIException as e:
            raise(e)

def Delete_Enquiry_detail(**data):
      try :
            cour = Student.Student_Details.objects.filter(Enquiry_id=data.get('Enquiry_id')).first()
            cour.delete()
            return "Successfully Deleted"

      except APIException as e:
            raise(e)

def Update_Enquiry_Registration(**data):
      try : 
            stud = Student.Student_Details.objects.filter(Enquiry_id=data.get('Enquiry_id')).first()
            stud.status = data.get("status")
            stud.save()

            return stud.Enquiry_id
            
      except APIException as e :
            raise(e)

def Update_Enquiry_detail(**data):
      try :
            stud = Student.Student_Details.objects.filter(Enquiry_id=data.get('Enquiry_id')).first()
            stud.Enquiry_date =data.get("Enquiry_date")
            stud.Student_name=data.get("Student_name")
            stud.Father_name=data.get("Father_name")
            stud.Date_birth=data.get("Date_birth")
            stud.Gender=data.get("Gender")
            stud.Blood_group=data.get("Blood_group")
            stud.Address=data.get("Address")
            stud.City = data.get("City")
            stud.State = data.get("State")
            stud.zipCode = data.get("zipCode")
            stud.Phone_number=data.get("Phone_number")
            stud.Email=data.get("Email")
            stud.Marital_status=data.get("Marital_status")
            
            stud.Counsellor_name=data.get("Counsellor_name")
            stud.Reference_name=data.get("Reference_name")
            stud.Course_name=data.get("Course_name")
            stud.Course_fee=data.get("Course_fee")
            stud.Discount=data.get("Discount")
            stud.Discount_fee=data.get("Discount_fee")
            stud.Total_course_fee=data.get("Total_course_fee")
            stud.Update_date = datetime.now()
            stud.save()

            return stud.Enquiry_id

      except APIException as e:
            raise(e)

def Student_Qualification_services(**data):      

      try:
            qual = Student.Student_Qualification.objects.create(
                 Student_name= data.get("Student_name"),
                 Qualification_name = data.get("Qualification_name"),
                 Qualification_code=data.get("Qualification_code"),
            )
            return data.get("Qualification_name")

      except APIException as e :
            raise(e)   

def Get_Student_Qualification_detail(data):
      try:
            print(data)
            stud = Student.Student_Qualification.objects.filter(Qualification_code=data).values()
            return stud
      except APIException as e:
            raise(e)

def Fetch_Student_Qualification_detail():
      try:
            stud = Student.Student_Qualification.objects.all()
            values = stud.values()
            return values
      except APIException as e:
            raise(e)

def Delete_Student_Qualification_detail(**data):
      try :
            stud = Student.Student_Qualification.objects.filter(Qualification_id=data.get('Qualification_id')).first()
            stud.delete()
            return "Successfully Deleted"

      except APIException as e:
            raise(e) 

def Update_Student_Qualification_detail(**data):
      try :
            stud = Student.Student_Qualification.objects.filter(Qualification_code=data.get('Qualification_code')).first()
            stud.Student_name = data.get('Student_name')
            stud.Qualification_name = data.get('Qualification_name')
            stud.Update_date = datetime.now()
            stud.save()

            return stud.Qualification_id

      except APIException as e:
            raise(e)
