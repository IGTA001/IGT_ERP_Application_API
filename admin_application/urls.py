from django.urls import path
from .views import user_views,Course_views,Student_views,Staff_views
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

router =routers.DefaultRouter()
urlpatterns =router.urls
urlpatterns += [
    path('token', user_views.CreateToken.as_view(), name='token_obtain_pair'),
        # course
    path('course_create', Course_views.CreateCourse.as_view(), name='course_create'),
    path('get_course_datail', Course_views.GetCourseDetail.as_view(), name='get_course_datail'),
    path('fetch_course_datail', Course_views.FetchCourseDetail.as_view(), name='fetch_course_datail'),
    path('update_course_datail', Course_views.UpdateCourseDetail.as_view(), name='update_course_datail'),
    path('delete_course_datail', Course_views.DeleteCourseDetail.as_view(), name='delete_course_datail'),
        
        # Enquiry
    path('Create_Enquiry',Student_views.CreateEnquiry.as_view(),name="Create_Enquiry"),
    path('get_enquiry_datail', Student_views.GetenquiryDetail.as_view(), name='get_enquiry_datail'),
    path('fetch_enquiry_datail', Student_views.FetchenquiryDetail.as_view(), name='fetch_enquiry_datail'),
    path('update_enquiry_datail', Student_views.UpdateenquiryDetail.as_view(), name='update_enquiry_datail'),
    path('delete_enquiry_datail', Student_views.DeleteenquiryDetail.as_view(), name='delete_enquiry_datail'),
    path('update_enquiry_registration', Student_views.UpdateEnquiryRegistration.as_view(), name='update_enquiry_registration'),
         
        # Qualification
    path('Create_Student_Qualification',Student_views.CreateStudent_Qualification.as_view(),name="Create_Student_Qualification"),
    path('get_Student_Qualification_datail', Student_views.GetStudent_Qualification_Detail.as_view(), name='get_Student_Qualification_datail'),
    path('fetch_Student_Qualification_datail', Student_views.FetchStudent_Qualification_Detail.as_view(), name='fetch_Student_Qualification_datail'),
    path('update_Student_Qualification_datail', Student_views.UpdateStudent_Qualification_Detail.as_view(), name='update_Student_Qualification_datail'),
    path('delete_Student_Qualification_datail', Student_views.DeleteStudent_Qualification_Detail.as_view(), name='delete_Student_Qualification_datail'),
        
        # Designation
    path('Designation_create', Staff_views.CreateDesignation.as_view(), name='Designation_create'),
    path('get_Designation_detail', Staff_views.GetDesignationDetail.as_view(), name='get_Designation_detail'),
    path('fetch_Designation_detail', Staff_views.FetchDesignationDetail.as_view(), name='fetch_Designation_detail'),
    path('update_Designation_detail', Staff_views.UpdateDesignationDetail.as_view(), name='update_Designation_detail'),
    path('delete_Designation_detail', Staff_views.DeleteDesignationDetail.as_view(), name='delete_Designation_detail'),    
]
 