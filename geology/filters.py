import django_filters
from django_filters import CharFilter
from django import forms
from .models import *

class   MineralFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': "What's mineral you look for.."
    }))
    class Meta:
        model = Mineral
        fields = ('name',)
        