from django.urls import path
from . import views

app_name ='provile'
urlpatterns = [
    #Users Profile pages
    path('adminpage', views.adminpage, name='adminpage'),
    path('staff', views.stafpage, name='stafpage'),
    path('', views.userpage, name='userpage'),
    #######################################################

    #Update user profile
    path('userprofile_new', views.userprofile_new, name='userprofile_new'),
    path('userprofile', views.userprofile, name='userprofile'),
    #######################################################

    #View user profile
    path('<auth_id>', views.viewUserpage, name='viewuserpage'),
    #######################################################

    #User skills page, edit and delete
    path('skill/', views.skill, name='skill'),
    path('update_skill/<skill_id>', views.edite_skill, name='edite_skill'),
    path('delete/<skill_id>', views.delete_skill, name='delete_skill'),
    #######################################################

    #User certificates page, edit and delete
    path('certificate/', views.certificate, name='certificate'),
    path('update_certificate/<certificate_id>', views.edite_certificate, name='edite_certificate'),
    path('del/<certificate_id>', views.delete_certificate, name='delete_certificate'),
    #######################################################

    #User experiences page, edit and delete
    path('experience/', views.experience, name='experience'),
    path('update_experiences/<experience_id>', views.edite_experience, name='edite_experience'),
    path('del/obj/<experience_id>', views.delete_experience, name='delete_experience'),
    #######################################################

    #User contact page, edit and delete
    path('media/', views.media, name='media'),
    path('media_update/<media_id>', views.edite_media_url, name='edite_media_url'),
    path('del/social_media/<media_id>', views.delete_media_url, name='delete_media_url'),
    #######################################################

    #Edit & delete users posts by admin & staff
    path('admin_edit_report/<user_id>', views.admin_edit_report, name='admin_edit_report'),
    path('admin_delete_post/<id>', views.admin_delete_post, name='admin_delete_post'),
    #######################################################

    #Edit users rocks by admin & staff
    path('admin_edit_rock/<user_id>', views.admin_edit_rock, name='admin_edit_rock'),

    #Answer FAQ
    path('admin_answer_faq/<user_id>', views.admin_answer_faq, name='admin_answer_faq'),
    path('delete_faq/<id>', views.delete_faq, name='delete_faq'),

    #SMS
    path('replaysms/', views.replaysms, name='replaysms'),
    path('admin_replay_sms/<user_id>', views.admin_replay_sms, name='admin_replay_sms'),
    path('geologesd/email', views.user_sms, name='user_sms'),
    path('geologeSD/email/<sms_id>', views.user_sms_id, name='user_sms_id'),
    path('geologeSD/email/messages/<sms_id>', views.message_sms_id, name='message_sms_id'),
]