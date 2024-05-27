from .models import EducationLanguage,EducationType,Degree, Enrollment,University,Program,ProgramScholarship
from rest_framework.serializers import ModelSerializer

class ELangModelSerializer(ModelSerializer):
    class Meta :
        model = EducationLanguage
        fields = "__all__"
    
class ETypeModelSerializer(ModelSerializer):
    class Meta :
        model = EducationType
        fields = "__all__"
    
class DegreeModelSerializer(ModelSerializer):
    class Meta :
        model = Degree
        fields = "__all__"
    
class ProgramModelSerializer(ModelSerializer):
    class Meta :
        model = Program
        fields = "__all__"

class UniversityModelSerializer(ModelSerializer):
    class Meta :
        model = University
        fields = "__all__"

class ProgramScholarshipModelSerializer(ModelSerializer):
    class Meta:
        model=ProgramScholarship
        fields="__all__"

class EnrollmentModelSerializer(ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"




