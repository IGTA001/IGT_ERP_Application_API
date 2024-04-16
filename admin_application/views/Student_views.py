import logging
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from ..services import *

logger = logging.getLogger('django')
  
class CreateEnquiry(APIView):
      class InputSerializer(serializers.Serializer):
            Enquiry_date = serializers.DateField()
            Student_name = serializers.CharField()
            Father_name = serializers.CharField()
            Date_birth = serializers.DateField()
            Gender = serializers.CharField()
            Blood_group = serializers.CharField()
            Address = serializers.CharField()

            City = serializers.CharField()
            State = serializers.CharField()
            zipCode = serializers.CharField()

            Phone_number = serializers.CharField()
            Email = serializers.CharField()
            Marital_status = serializers.CharField()
            Qualification_code = serializers.CharField()
            Counsellor_name = serializers.CharField()
            Reference_name = serializers.CharField()
            course_name = serializers.CharField()
            Course_fee = serializers.FloatField()
            Discount = serializers.CharField()
            Discount_fee = serializers.FloatField()
            Total_course_fee = serializers.FloatField()
      def post(self, request):
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = Student_services.Enquiry_services(**serializer.validated_data)

            return Response({'Student name': user},status=status.HTTP_200_OK)

class GetenquiryDetail(APIView):
      class InputSerializer(serializers.Serializer):
            Enquiry_id = serializers.CharField(required=True)
      
      def post(self, request):
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            enquiry_detail =Student_services.Get_Enquiry_detail(serializer.validated_data.get('Enquiry_id'))
            return Response( enquiry_detail, status=status.HTTP_200_OK)


class FetchenquiryDetail(APIView):
      def post(self, request):
            list = Student_services.Fetch_Enquiry_detail()
            return Response(list, status=status.HTTP_200_OK)

class UpdateenquiryDetail(APIView):
      class InputSerializer(serializers.Serializer):
            Enquiry_id= serializers.CharField(required=True)
            Enquiry_date = serializers.DateField()
            Student_name = serializers.CharField()
            Father_name = serializers.CharField()
            Date_birth = serializers.DateField()
            Gender = serializers.CharField()
            Address = serializers.CharField()
            City = serializers.CharField()
            State = serializers.CharField()
            zipCode = serializers.CharField()
            Phone_number = serializers.CharField()
            Email = serializers.CharField()
            Marital_status = serializers.CharField()
            Counsellor_name = serializers.CharField()
            Reference_name = serializers.CharField()
            Course_name = serializers.CharField()
            Course_fee = serializers.FloatField()
            Discount = serializers.CharField()
            Discount_fee = serializers.FloatField()
            Total_course_fee = serializers.FloatField()
      def post(self, request):
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = Student_services.Update_Enquiry_detail(**serializer.validated_data)

            return Response({'enquiry id': user},status=status.HTTP_200_OK)

class DeleteenquiryDetail(APIView):
      class InputSerializer(serializers.Serializer):
            Enquiry_id = serializers.CharField(required=True)
      def post(self, request):
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = Student_services.Delete_Enquiry_detail(**serializer.validated_data)

            return Response({'mgs': user},status=status.HTTP_200_OK)

class UpdateEnquiryRegistration(APIView):
      class InputSerializer(serializers.Serializer):
            Enquiry_id = serializers.CharField(required=True)
            status = serializers.CharField(required=True)

      def post(self, request):
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = Student_services.Update_Enquiry_Registration(**serializer.validated_data)

            return Response({'enquiry': user},status=status.HTTP_200_OK)


class CreateStudent_Qualification(APIView) :
      class InputSerializer(serializers.Serializer):
            Student_name = serializers.CharField()
            Qualification_name = serializers.JSONField()
            Qualification_code = serializers.CharField()
      def post(self, request):
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = Student_services.Student_Qualification_services(**serializer.validated_data)

            return Response({'Qualification name': user},status=status.HTTP_200_OK)


class GetStudent_Qualification_Detail(APIView):
      class InputSerializer(serializers.Serializer):
            Qualification_code = serializers.CharField(required=True)
      
      def post(self, request):
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            Qualification_detail =Student_services.Get_Student_Qualification_detail(serializer.validated_data.get('Qualification_code'))
            return Response(Qualification_detail, status=status.HTTP_200_OK)


class FetchStudent_Qualification_Detail(APIView):
      def post(self, request):
            list = Student_services.Fetch_Student_Qualification_detail()
            return Response(list, status=status.HTTP_200_OK)

class UpdateStudent_Qualification_Detail(APIView):
      class InputSerializer(serializers.Serializer):
            Qualification_code = serializers.CharField(required=True)
            Student_name = serializers.CharField(required=True)
            Qualification_name = serializers.JSONField(required=True)
            
      def post(self, request):
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = Student_services.Update_Student_Qualification_detail(**serializer.validated_data)

            return Response({'Qualification id': user},status=status.HTTP_200_OK)

class DeleteStudent_Qualification_Detail(APIView):
      class InputSerializer(serializers.Serializer):
            Qualification_id = serializers.CharField(required=True)
      def post(self, request):
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = Student_services.Delete_Student_Qualification_detail(**serializer.validated_data)

            return Response({'mgs': user},status=status.HTTP_200_OK)