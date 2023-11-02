from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('repo_form/', views.repo_form, name='repo_form'),
    path('<int:pk>/', views.report, name='report'),
    
]