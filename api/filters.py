import django_filters
from .models import ProgramScholarship

class ProgramScholarshipFilter(django_filters.FilterSet):
    program_name = django_filters.CharFilter(field_name='program__program_name', lookup_expr='icontains')
    university_name = django_filters.CharFilter(field_name='university__university_name', lookup_expr='icontains')
    scholarship_percentage = django_filters.RangeFilter()

    class Meta:
        model = ProgramScholarship
        fields = {
            'scholarship_year': ['exact',],
        }
