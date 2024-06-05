from .models import EducationLanguage, EducationType, Degree, Enrollment, University, Program, ProgramScholarship
from rest_framework.serializers import ModelSerializer

class ELangModelSerializer(ModelSerializer):
    class Meta:
        model = EducationLanguage
        fields = "__all__"

class ETypeModelSerializer(ModelSerializer):
    class Meta:
        model = EducationType
        fields = "__all__"

class DegreeModelSerializer(ModelSerializer):
    class Meta:
        model = Degree
        fields = "__all__"

class ProgramModelSerializer(ModelSerializer):
    degree = DegreeModelSerializer()

    class Meta:
        model = Program
        fields = "__all__"

class UniversityModelSerializer(ModelSerializer):
    programs = ProgramModelSerializer(many=True, read_only=True)
    education_types = ETypeModelSerializer(many=True, read_only=True)
    education_languages = ELangModelSerializer(many=True, read_only=True)

    class Meta:
        model = University
        fields = "__all__"

class ProgramScholarshipModelSerializer(ModelSerializer):
    university = UniversityModelSerializer()
    program = ProgramModelSerializer()

    class Meta:
        model = ProgramScholarship
        fields = "__all__"

class EnrollmentModelSerializer(ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"
