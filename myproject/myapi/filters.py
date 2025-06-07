import django_filters
from .models import *


class EmployeeFilter(django_filters.FilterSet):
    designation=django_filters.CharFilter(field_name='designation',lookup_expr='iexact')
    empname=django_filters.CharFilter(field_name='empname',lookup_expr='iexact')
    # id=django_filters.RangeFilter(fie)
    id_min=django_filters.CharFilter(method='filter_by_id_range',label='From EMP ID')
    id_max=django_filters.CharFilter(method='filter_by_id_range',label='TO EMP ID')


    class Meta:
        model=Employee
        fields=['designation','empname','id_min','id_max']

    def filter_by_id_range(self,queryset,name,value):
        if name == 'id_min':
            return queryset.filter(empn0__gte=value)
        elif name == 'id_max':
            return queryset.filter(empn0__lte=value)    
        return queryset    
