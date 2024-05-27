from django.contrib import admin
from .models import EducationLanguage,EducationType,Degree, Enrollment,University,Program,ProgramScholarship

# Register your models here.

admin.site.register(EducationLanguage)
admin.site.register(EducationType)
admin.site.register(Degree)
admin.site.register(Enrollment)
admin.site.register(University)
admin.site.register(Program)
admin.site.register(ProgramScholarship)
