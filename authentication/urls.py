from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signin_new', views.signin_new, name='signin_new'),
    path('signout', views.signout, name='signout'),
    path('user/uptate/<user_id>', views.admin_update_user, name='admin_update_user'),
    #path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('user/delete/<id>', views.delete_user, name='delete_user'),
]