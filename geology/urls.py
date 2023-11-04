from django.urls import path
from . import views

app_name = 'geology'
urlpatterns = [
    path('', views.index, name='home'),

    path('geologysd/users/student{{}}$^', views.users_by_degree, name='users_by_degree'),
    path('geologysd/users/degree/deploma{{}}$^', views.users_by_degree_da, name='users_by_degree_da'),
    path('geologysd/users/degree/Bachelor{{}}$^', views.users_by_degree_ba, name='users_by_degree_ba'),
    path('geologysd/users/degree/Master{{}}$^', views.users_by_degree_ma, name='users_by_degree_ma'),
    path('geologysd/users/degree/Doctoral{{}}$^', views.users_by_degree_phd, name='users_by_degree_phd'),
    path('geologysd/users/degree/Associate{{}}$^', views.users_by_degree_aa, name='users_by_degree_aa'),
    path('geologysd/users/degree/Teaching^Assistant{{}}$^', views.users_by_degree_ta, name='users_by_degree_ta'),
    path('geologysd/users/degree/Assistant^Lecturer"{{}}$^', views.users_by_degree_al, name='users_by_degree_al'),
    path('geologysd/users/degree/Assistant^Professor{{}}$^', views.users_by_degree_ap, name='users_by_degree_ap'),

    path('repo_form/', views.repo_form, name='repo_form'),
    path('post/<pk>', views.report, name='report'),
    path('post/newpost/', views.latest_report, name='latest_report'),
    path('post/update/<repo_id>', views.repo_update, name='repo_update'),
    path('post/delete/<id>', views.repo_delete, name='repo_delete'),
    path('search_results', views.search_results, name='search_results'),
    ########################
    path('rocks/igneous_rock', views.igneous_rock, name='igneous_rock'),
    path('rocks/metamorphic_rock', views.metamorphic_rock, name='metamorphic_rock'),
    path('rocks/sedimentary_rock', views.sedimentary_rock, name='sedimentary_rock'),
    path('rocks/{rock}{{{}}}$^rock', views.new_rock, name='new_rock'),

    path('rocks/<rock_id>', views.rock, name='rock'),

    path('rocks/rock_form/', views.rock_form, name='rock_form'),

    path('rock/update/<repo_id>', views.rock_update, name='rock_update'),
    path('rock/delete/<id>', views.rock_delete, name='rock_delete'),
    path('staff/rock/delete/<id>', views.rock_delete_admin, name='rock_delete_admin'),
    #################################################

    ####################MINERALS#####################
    path('mineral_form/', views.mineral_form, name='mineral_form'),
    path('minerals/{mineral}{{{}}}$^mineral', views.new_mineral, name='new_mineral'),
    path('minerals/', views.minerals, name='minerals'),
    path('mineral_detail/<mineral_id>', views.mineral_detail, name='mineral_detail'),
    path('mineral/update/<repo_id>', views.mineral_update, name='mineral_update'),
    path('staff/mineral/update/<repo_id>', views.mineral_update_admin, name='mineral_update_admin'),
    path('mineral/delete/<id>', views.mineral_delete, name='mineral_delete'),
    path('staff/mineral/delete/<id>', views.mineral_delete_admin, name='mineral_delete_admin'),
    #################################################
    #############FAQ############
    path('faq/', views.faq, name='faq'),
    path('faq/answer/', views.answered_faq, name='faq_answered'),
    path('faq/question/', views.faqform, name='faqform'),

    ###########################################
    path('cv/', views.cv, name='cv'),
    
]