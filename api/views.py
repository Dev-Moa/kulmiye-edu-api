from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializer import ELangModelSerializer,ETypeModelSerializer,DegreeModelSerializer,ProgramModelSerializer,UniversityModelSerializer,EnrollmentModelSerializer,ProgramScholarshipModelSerializer
from .models import EducationLanguage,EducationType,Degree,Program,University,Enrollment,ProgramScholarship
from .permission import IsAdminOrReadOnly
from rest_framework.permissions import DjangoObjectPermissions,IsAuthenticatedOrReadOnly

# Create your views here.


# Education language
class ELangAPIView(generics.ListCreateAPIView):
    queryset = EducationLanguage.objects.all()
    serializer_class = ELangModelSerializer
    permission_classes = [IsAdminOrReadOnly]

class ELangDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EducationLanguage.objects.all()
    serializer_class = ELangModelSerializer
    permission_classes = [IsAdminOrReadOnly]

# Education Type
class ETypeAPIView(generics.ListCreateAPIView):
    queryset = EducationType.objects.all()
    serializer_class = ETypeModelSerializer
    permission_classes = [IsAdminOrReadOnly]

class ETypeDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EducationType.objects.all()
    serializer_class = ETypeModelSerializer
    permission_classes = [IsAdminOrReadOnly]

# Degree 
class DegreeAPIView(generics.ListCreateAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeModelSerializer
    permission_classes = [IsAdminOrReadOnly]

class DegreeDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeModelSerializer
    permission_classes = [IsAdminOrReadOnly]
    
# Program 
class ProgramAPIView(generics.ListCreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramModelSerializer
    permission_classes = [IsAdminOrReadOnly]

class ProgramDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramModelSerializer
    permission_classes = [IsAdminOrReadOnly]

# University
class UniversityAPIView(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityModelSerializer
    permission_classes = [IsAdminOrReadOnly]

class UniversityDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityModelSerializer
    permission_classes = [IsAdminOrReadOnly]

# ProgramScholarship
class ProgramScholarshipAPIView(generics.ListCreateAPIView):
    queryset = ProgramScholarship.objects.all()
    serializer_class = ProgramScholarshipModelSerializer
    permission_classes = [IsAdminOrReadOnly]

class ProgramScholarshipDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProgramScholarship.objects.all()
    serializer_class = ProgramScholarshipModelSerializer
    permission_classes = [IsAdminOrReadOnly]

# Enrollment
class EnrollmentAPIView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EnrollmentDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentModelSerializer
    permission_classes = [IsAdminOrReadOnly]

