import django_filters
from .models import ProgramScholarship

class ProgramScholarshipFilter(django_filters.FilterSet):
    program_name = django_filters.CharFilter(field_name='program__program_name', lookup_expr='icontains')
    degree_name = django_filters.CharFilter(field_name='program__degree__degree_name', lookup_expr='exact')
    scholarship_percentage = django_filters.RangeFilter()

    class Meta:
        model = ProgramScholarship
        fields = {
            'scholarship_year': ['exact'],
        }


