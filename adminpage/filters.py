import django_filters

from account.models import *

class UserFiler(django_filters.FilterSet):
    usr = django_filters.CharFilter(field_name='username', lookup_expr='icontains', label='search username',)

    class Meta:
        model = User
        fields = ['usr']