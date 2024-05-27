from django.urls import path
from . import views

urlpatterns = [
    # education language 
    path("elang/", views.ELangAPIView.as_view()),
    path("elang/<int:pk>/", views.ELangDetailsAPIView.as_view()),
    # education type
    path("etype/", views.ETypeAPIView.as_view()),
    path("etype/<int:pk>/", views.ETypeDetailsAPIView.as_view()),
    #Degree
    path("degree/", views.DegreeAPIView.as_view()),
    path("degree/<int:pk>/", views.DegreeDetailsAPIView.as_view()),
    #Program
    path("program/", views.ProgramAPIView.as_view()),
    path("program/<int:pk>/", views.ProgramDetailsAPIView.as_view()),
    # ProgramScholarship
    path("scholarship/", views.ProgramScholarshipAPIView.as_view()),
    path("scholarship/<int:pk>/", views.ProgramDetailsAPIView.as_view()),
    # University
    path("university/", views.UniversityAPIView.as_view()),
    path("university/<int:pk>/", views.UniversityDetailsAPIView.as_view()),
    # Enrollment
    path("enroll/", views.EnrollmentAPIView.as_view()),
    path("enroll/<int:pk>/", views.EnrollmentDetailsAPIView.as_view()),

]
