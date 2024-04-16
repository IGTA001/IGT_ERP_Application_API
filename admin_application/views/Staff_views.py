import logging
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import status
from ..services import Staff_services

logger = logging.getLogger('django')


class CreateDesignation(APIView):
      class InputSerializer(serializers.Serializer):
            Designation_name = serializers.CharField()
           
      def post(self, request):
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = Staff_services.Designation_services(request.user.username,**serializer.validated_data)

            return Response({'Designation name': user},status=status.HTTP_200_OK)

class GetDesignationDetail(APIView):
      class InputSerializer(serializers.Serializer):
            Designation_id = serializers.CharField(required=True)
      
      def post(self, request):
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            Designation_detail =Staff_services.Get_Designation_detail(serializer.validated_data.get('Designation_id'))
            return Response(Designation_detail, status=status.HTTP_200_OK)

class FetchDesignationDetail(APIView):
      def post(self, request):
            list = Staff_services.Fetch_Designation_detail()
            return Response(list, status=status.HTTP_200_OK)

class UpdateDesignationDetail(APIView):
      class InputSerializer(serializers.Serializer):
            Designation_id = serializers.CharField(required=True)
            Designation_name = serializers.CharField(required=True)
      def post(self, request):
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = Staff_services.Update_Designation_detail(**serializer.validated_data)

            return Response({'Designation id': user},status=status.HTTP_200_OK)

class DeleteDesignationDetail(APIView):
      class InputSerializer(serializers.Serializer):
            Designation_id = serializers.CharField(required=True)
      def post(self, request):
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = Staff_services.Delete_Designation_detail(**serializer.validated_data)

            return Response({'mgs': user},status=status.HTTP_200_OK)