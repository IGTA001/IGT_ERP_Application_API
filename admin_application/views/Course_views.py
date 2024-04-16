import logging
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from ..services import *
 
logger = logging.getLogger('django')


class CreateCourse(APIView):
      class InputSerializer(serializers.Serializer):
            Course_name = serializers.CharField()
            Course_Fees = serializers.FloatField()
            Course_Status = serializers.CharField()
      def post(self, request):
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = Course_services.Course_services(request.user.username,**serializer.validated_data)

            return Response({'Course name': user},status=status.HTTP_200_OK)

class GetCourseDetail(APIView):
      class InputSerializer(serializers.Serializer):
            Course_id = serializers.CharField(required=True)
      
      def post(self, request):
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            Course_detail =Course_services.Get_Course_detail(serializer.validated_data.get('Course_id'))
            return Response(Course_detail, status=status.HTTP_200_OK)

class FetchCourseDetail(APIView):
      def post(self, request):
            list = Course_services.Fetch_course_detail()
            return Response(list, status=status.HTTP_200_OK)

class UpdateCourseDetail(APIView):
      class InputSerializer(serializers.Serializer):
            Course_id = serializers.CharField(required=True)
            Course_name = serializers.CharField(required=True)
            Course_Fees = serializers.FloatField(required=True)
            Course_Status = serializers.CharField()
      def post(self, request):
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = Course_services.Update_course_detail(**serializer.validated_data)

            return Response({'Course id': user},status=status.HTTP_200_OK)

class DeleteCourseDetail(APIView):
      class InputSerializer(serializers.Serializer):
            Course_id = serializers.CharField(required=True)
      def post(self, request):
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = Course_services.Delete_course_detail(**serializer.validated_data)

            return Response({'mgs': user},status=status.HTTP_200_OK)