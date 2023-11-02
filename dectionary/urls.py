#This Project with all app insite Created By: SUHAIB TAHA ALRIAH
#Email: alromys47@gmail.com
from django.urls import path
from . import views

app_name = 'dectionary'

urlpatterns = [
    path('', views.index, name='geo_dec'), #link page def=1.
    path('geo_dec_results/<dic_id>', views.geo_dec_results, name='geo_dec_results'), #link page def=1, Main dec page.
    path('dectionary_form', views.dectionary_form, name='dectionary_form'),
    path('dectionary_form_edit/<id>', views.dectionary_form_edit, name='dectionary_form_edit'),
  
]