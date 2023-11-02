import django_filters
from django_filters import CharFilter
from django import forms
from django.contrib.auth.models import User

class UserFilter(django_filters.FilterSet):
    username = CharFilter(field_name='username', lookup_expr='icontains',
    widget=forms.TextInput(attrs={
        'placeholder': 'Search by Username'
    }))

    class Meta:
        model = User
        fields = ['username']