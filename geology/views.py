from django.shortcuts import render, redirect, get_object_or_404
from geology.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required
from .models import *
from provile.models import MediaUrl, ContactProfile
from provile.forms import ContactForm
from dectionary.models import Dectionary
from .forms import (ReportForm, AuthorForm, RockForm, MineralForm, FaqForm)
from django.contrib import messages
from django.views import generic
from .filters import MineralFilter
from django.contrib.auth.models import User, Group


# Create your views here.
def index(request):
    reports =   Report.objects.all()
    rocks = Rock.objects.all()
    minerals = Mineral.objects.all()
    users = User.objects.filter(groups__name__in=['customer', 'staff', 'adminstration']).count()
    rock_count = rocks.count()
    mineral_count = minerals.count()

    students = Author.objects.filter(degree="Student")
    students_count = students.count()
    students_average = int(students_count / users * 100)
    students_post = reports.filter(author__degree__in=['Student'])
    post_count = students_post.count()

    da = Author.objects.filter(degree="DA")
    da_count = da.count()
    da_average = int(da_count / users * 100)
    da_post = reports.filter(author__degree__in=['DA'])
    da_post_count = da_post.count()

    ba = Author.objects.filter(degree="BA")
    ba_count = ba.count()
    ba_average = int(ba_count / users * 100)
    ba_post = reports.filter(author__degree__in=['BA'])
    ba_post_count = ba_post.count()

    ma = Author.objects.filter(degree="MA")
    ma_count = ma.count()
    ma_average = int(ma_count / users * 100)
    ma_post = reports.filter(author__degree__in=['MA'])
    ma_post_count = ma_post.count()

    phd = Author.objects.filter(degree="PHD")
    phd_count = phd.count()
    phd_average = int(phd_count / users * 100)
    phd_post = reports.filter(author__degree__in=['PHD'])
    phd_post_count = phd_post.count()

    aa = Author.objects.filter(degree="AA")
    aa_count = aa.count()
    aa_average = int(aa_count / users * 100)
    aa_post = reports.filter(author__degree__in=['AA'])
    aa_post_count = aa_post.count()

    ta = Author.objects.filter(degree="Teaching Assistant")
    ta_count = ta.count()
    ta_average = int(ta_count / users * 100)
    ta_post = reports.filter(author__degree__in=['Teaching Assistant'])
    ta_post_count = ta_post.count()

    al = Author.objects.filter(degree="Assistant Lecturer")
    al_count = al.count()
    al_average = int(al_count / users * 100)
    al_post = reports.filter(author__degree__in=['Assistant Lecturer'])
    al_post_count = al_post.count()

    ap = Author.objects.filter(degree="Assistant Professor")
    ap_count = ap.count()
    ap_average = int(ap_count / users * 100)
    ap_post = reports.filter(author__degree__in=['Assistant Professor'])
    ap_post_count = ap_post.count()


    

    if rocks.count() == 0:
        rock_count = rocks.count()
        if minerals.count() == 0:
            mineral_count = minerals.count()
            if request.user.is_authenticated:
                user_sms =   request.user.author.contactprofile_set.all()
                #SMS
                admin_messages =  user_sms.filter(is_sent=True)
                sms_count = admin_messages.count()
                context =   {'reports': reports, 'rocks': rocks, 'minerals': minerals, 'rock_count': rock_count, 'mineral_count': mineral_count,
                        'users': users, 'students ': students, 'students_count': students_count,
                        'students_average': students_average, 'post_count': post_count, 'da': da,
                        'da_count': da_count, 'da_average': da_average, 'da_post_count': da_post_count,
                        'ba_count': ba_count, 'ba_average': ba_average, 'ba_post_count': ba_post_count,
                        'ma_count': ma_count, 'ma_average': ma_average, 'ma_post_count': ma_post_count,
                        'phd_count': phd_count, 'phd_average': phd_average, 'phd_post_count': phd_post_count,
                        'aa_count': aa_count, 'aa_average': aa_average, 'aa_post_count': aa_post_count,
                        'ta_count': ta_count, 'ta_average': ta_average, 'ta_post_count': ta_post_count,
                        'al_count': al_count, 'al_average': al_average, 'al_post_count': al_post_count,
                        'ap_count': ap_count, 'ap_average': ap_average, 'ap_post_count': ap_post_count,'admin_messages': admin_messages, 'sms_count': sms_count}
                return render(request, 'home.html',context)
            else:
                context =   {'reports': reports, 'rocks': rocks, 'minerals': minerals, 'rock_count': rock_count, 'mineral_count': mineral_count,
                        'users': users, 'students ': students, 'students_count': students_count,
                        'students_average': students_average, 'post_count': post_count, 'da': da,
                        'da_count': da_count, 'da_average': da_average, 'da_post_count': da_post_count,
                        'ba_count': ba_count, 'ba_average': ba_average, 'ba_post_count': ba_post_count,
                        'ma_count': ma_count, 'ma_average': ma_average, 'ma_post_count': ma_post_count,
                        'phd_count': phd_count, 'phd_average': phd_average, 'phd_post_count': phd_post_count,
                        'aa_count': aa_count, 'aa_average': aa_average, 'aa_post_count': aa_post_count,
                        'ta_count': ta_count, 'ta_average': ta_average, 'ta_post_count': ta_post_count,
                        'al_count': al_count, 'al_average': al_average, 'al_post_count': al_post_count,
                        'ap_count': ap_count, 'ap_average': ap_average, 'ap_post_count': ap_post_count}
                return render(request, 'home.html',context)
        else:
            new_mineral = Mineral.objects.latest()
            if request.user.is_authenticated:
                user_sms =   request.user.author.contactprofile_set.all()
                #SMS
                admin_messages =  user_sms.filter(is_sent=True)
                sms_count = admin_messages.count()
                context =   {'reports': reports, 'rocks': rocks, 'minerals': minerals, 'rock_count': rock_count, 'mineral_count': mineral_count,'new_mineral': new_mineral,
                        'users': users, 'students ': students, 'students_count': students_count,
                        'students_average': students_average, 'post_count': post_count, 'da': da,
                        'da_count': da_count, 'da_average': da_average, 'da_post_count': da_post_count,
                        'ba_count': ba_count, 'ba_average': ba_average, 'ba_post_count': ba_post_count,
                        'ma_count': ma_count, 'ma_average': ma_average, 'ma_post_count': ma_post_count,
                        'phd_count': phd_count, 'phd_average': phd_average, 'phd_post_count': phd_post_count,
                        'aa_count': aa_count, 'aa_average': aa_average, 'aa_post_count': aa_post_count,
                        'ta_count': ta_count, 'ta_average': ta_average, 'ta_post_count': ta_post_count,
                        'al_count': al_count, 'al_average': al_average, 'al_post_count': al_post_count,
                        'ap_count': ap_count, 'ap_average': ap_average, 'ap_post_count': ap_post_count,'admin_messages': admin_messages, 'sms_count': sms_count}
                return render(request, 'home.html',context)

            else:
                context =   {'reports': reports, 'rocks': rocks, 'minerals': minerals, 'rock_count': rock_count, 'mineral_count': mineral_count, 'new_mineral': new_mineral,
                            'users': users, 'students ': students, 'students_count': students_count,
                            'students_average': students_average, 'post_count': post_count, 'da': da,
                            'da_count': da_count, 'da_average': da_average, 'da_post_count': da_post_count,
                            'ba_count': ba_count, 'ba_average': ba_average, 'ba_post_count': ba_post_count,
                            'ma_count': ma_count, 'ma_average': ma_average, 'ma_post_count': ma_post_count,
                            'phd_count': phd_count, 'phd_average': phd_average, 'phd_post_count': phd_post_count,
                            'aa_count': aa_count, 'aa_average': aa_average, 'aa_post_count': aa_post_count,
                            'ta_count': ta_count, 'ta_average': ta_average, 'ta_post_count': ta_post_count,
                            'al_count': al_count, 'al_average': al_average, 'al_post_count': al_post_count,
                            'ap_count': ap_count, 'ap_average': ap_average, 'ap_post_count': ap_post_count}
                return render(request, 'home.html',context)

    elif rocks.count() != 0:
        rock_count = rocks.count()
        if minerals.count() == 0:
            mineral_count = minerals.count()
            new_rock = Rock.objects.latest()
            if request.user.is_authenticated:
                user_sms =   request.user.author.contactprofile_set.all()
                #SMS
                admin_messages =  user_sms.filter(is_sent=True)
                sms_count = admin_messages.count()
                context =   {'reports': reports, 'rocks': rocks, 'minerals': minerals, 'rock_count': rock_count, 'mineral_count': mineral_count, 'new_rock': new_rock,
                        'users': users, 'students ': students, 'students_count': students_count,
                        'students_average': students_average, 'post_count': post_count, 'da': da,
                        'da_count': da_count, 'da_average': da_average, 'da_post_count': da_post_count,
                        'ba_count': ba_count, 'ba_average': ba_average, 'ba_post_count': ba_post_count,
                        'ma_count': ma_count, 'ma_average': ma_average, 'ma_post_count': ma_post_count,
                        'phd_count': phd_count, 'phd_average': phd_average, 'phd_post_count': phd_post_count,
                        'aa_count': aa_count, 'aa_average': aa_average, 'aa_post_count': aa_post_count,
                        'ta_count': ta_count, 'ta_average': ta_average, 'ta_post_count': ta_post_count,
                        'al_count': al_count, 'al_average': al_average, 'al_post_count': al_post_count,
                        'ap_count': ap_count, 'ap_average': ap_average, 'ap_post_count': ap_post_count,'admin_messages': admin_messages, 'sms_count': sms_count}
                return render(request, 'home.html',context)
            else:
                context =   {'reports': reports, 'rocks': rocks, 'minerals': minerals, 'rock_count': rock_count, 'mineral_count': mineral_count, 'new_rock': new_rock,
                        'users': users, 'students ': students, 'students_count': students_count,
                        'students_average': students_average, 'post_count': post_count, 'da': da,
                        'da_count': da_count, 'da_average': da_average, 'da_post_count': da_post_count,
                        'ba_count': ba_count, 'ba_average': ba_average, 'ba_post_count': ba_post_count,
                        'ma_count': ma_count, 'ma_average': ma_average, 'ma_post_count': ma_post_count,
                        'phd_count': phd_count, 'phd_average': phd_average, 'phd_post_count': phd_post_count,
                        'aa_count': aa_count, 'aa_average': aa_average, 'aa_post_count': aa_post_count,
                        'ta_count': ta_count, 'ta_average': ta_average, 'ta_post_count': ta_post_count,
                        'al_count': al_count, 'al_average': al_average, 'al_post_count': al_post_count,
                        'ap_count': ap_count, 'ap_average': ap_average, 'ap_post_count': ap_post_count}
                return render(request, 'home.html',context)
        else:
            new_rock = Rock.objects.latest()
            new_mineral = Mineral.objects.latest()
            if request.user.is_authenticated:
                user_sms =   request.user.author.contactprofile_set.all()
                #SMS
                admin_messages =  user_sms.filter(is_sent=True)
                sms_count = admin_messages.count()
                context =   {'reports': reports, 'rocks': rocks, 'minerals': minerals, 'rock_count': rock_count, 'mineral_count': mineral_count, 'new_rock': new_rock, 'new_mineral': new_mineral,
                        'users': users, 'students ': students, 'students_count': students_count,
                        'students_average': students_average, 'post_count': post_count, 'da': da,
                        'da_count': da_count, 'da_average': da_average, 'da_post_count': da_post_count,
                        'ba_count': ba_count, 'ba_average': ba_average, 'ba_post_count': ba_post_count,
                        'ma_count': ma_count, 'ma_average': ma_average, 'ma_post_count': ma_post_count,
                        'phd_count': phd_count, 'phd_average': phd_average, 'phd_post_count': phd_post_count,
                        'aa_count': aa_count, 'aa_average': aa_average, 'aa_post_count': aa_post_count,
                        'ta_count': ta_count, 'ta_average': ta_average, 'ta_post_count': ta_post_count,
                        'al_count': al_count, 'al_average': al_average, 'al_post_count': al_post_count,
                        'ap_count': ap_count, 'ap_average': ap_average, 'ap_post_count': ap_post_count,'admin_messages': admin_messages, 'sms_count': sms_count}
                return render(request, 'home.html',context)
            else:

                context =   {'reports': reports, 'rocks': rocks, 'minerals': minerals, 'rock_count': rock_count, 'mineral_count': mineral_count, 'new_rock': new_rock, 'new_mineral': new_mineral,
                            'users': users, 'students ': students, 'students_count': students_count,
                            'students_average': students_average, 'post_count': post_count, 'da': da,
                            'da_count': da_count, 'da_average': da_average, 'da_post_count': da_post_count,
                            'ba_count': ba_count, 'ba_average': ba_average, 'ba_post_count': ba_post_count,
                            'ma_count': ma_count, 'ma_average': ma_average, 'ma_post_count': ma_post_count,
                            'phd_count': phd_count, 'phd_average': phd_average, 'phd_post_count': phd_post_count,
                            'aa_count': aa_count, 'aa_average': aa_average, 'aa_post_count': aa_post_count,
                            'ta_count': ta_count, 'ta_average': ta_average, 'ta_post_count': ta_post_count,
                            'al_count': al_count, 'al_average': al_average, 'al_post_count': al_post_count,
                            'ap_count': ap_count, 'ap_average': ap_average, 'ap_post_count': ap_post_count}
                return render(request, 'home.html',context)

def users_by_degree(request):
    students = Author.objects.filter(degree="Student")
    student_count = students.count()
    active_user = datetime.date.today

    if request.user.is_authenticated:
        user_sms =   request.user.author.contactprofile_set.all()
        #SMS
        admin_messages =  user_sms.filter(is_sent=True)
        sms_count = admin_messages.count()
    
        context ={'students': students, 'student_count': student_count, 'active_user': active_user, 'admin_messages': admin_messages, 'sms_count': sms_count}
        return render(request, 'users_by_degree.html',context)
    else:
        context ={'students': students, 'student_count': student_count, 'active_user': active_user}
        return render(request, 'users_by_degree.html',context)

def users_by_degree_da(request):
    students = Author.objects.filter(degree="DA")
    da_count = students.count()
    active_user = datetime.date.today

    if request.user.is_authenticated:
        user_sms =   request.user.author.contactprofile_set.all()
        #SMS
        admin_messages =  user_sms.filter(is_sent=True)
        sms_count = admin_messages.count()
    
        context ={'students': students, 'da_count': da_count, 'active_user': active_user, 'admin_messages': admin_messages, 'sms_count': sms_count}
        return render(request, 'users_by_degree.html',context)
    else:
        context ={'students': students, 'da_count': da_count, 'active_user': active_user}
        return render(request, 'users_by_degree.html',context)

def users_by_degree_ba(request):
    students = Author.objects.filter(degree="BA")
    ba_count = students.count()
    active_user = datetime.date.today

    if request.user.is_authenticated:
        user_sms =   request.user.author.contactprofile_set.all()
        #SMS
        admin_messages =  user_sms.filter(is_sent=True)
        sms_count = admin_messages.count()
    
        context ={'students': students, 'ba_count': ba_count, 'active_user': active_user, 'admin_messages': admin_messages, 'sms_count': sms_count}
        return render(request, 'users_by_degree.html',context)
    else:
        context ={'students': students, 'ba_count': ba_count, 'active_user': active_user}
        return render(request, 'users_by_degree.html',context)

def users_by_degree_ma(request):
    students = Author.objects.filter(degree="MA")
    ma_count = students.count()
    active_user = datetime.date.today

    if request.user.is_authenticated:
        user_sms =   request.user.author.contactprofile_set.all()
        #SMS
        admin_messages =  user_sms.filter(is_sent=True)
        sms_count = admin_messages.count()
    
        context ={'students': students, 'ma_count': ma_count, 'active_user': active_user, 'admin_messages': admin_messages, 'sms_count': sms_count}
        return render(request, 'users_by_degree.html',context)
    else:
        context ={'students': students, 'ma_count': ma_count, 'active_user': active_user}
        return render(request, 'users_by_degree.html',context)

def users_by_degree_phd(request):
    students = Author.objects.filter(degree="PHD")
    phd_count = students.count()
    active_user = datetime.date.today

    if request.user.is_authenticated:
        user_sms =   request.user.author.contactprofile_set.all()
        #SMS
        admin_messages =  user_sms.filter(is_sent=True)
        sms_count = admin_messages.count()
    
        context ={'students': students, 'phd_count': phd_count, 'active_user': active_user, 'admin_messages': admin_messages, 'sms_count': sms_count}
        return render(request, 'users_by_degree.html',context)
    else:
        context ={'students': students, 'phd_count': phd_count, 'active_user': active_user}
        return render(request, 'users_by_degree.html',context)

def users_by_degree_aa(request):
    students = Author.objects.filter(degree="AA")
    aa_count = students.count()
    active_user = datetime.date.today

    if request.user.is_authenticated:
        user_sms =   request.user.author.contactprofile_set.all()
        #SMS
        admin_messages =  user_sms.filter(is_sent=True)
        sms_count = admin_messages.count()
    
        context ={'students': students, 'aa_count': aa_count, 'active_user': active_user, 'admin_messages': admin_messages, 'sms_count': sms_count}
        return render(request, 'users_by_degree.html',context)
    else:
        context ={'students': students, 'aa_count': aa_count, 'active_user': active_user}
        return render(request, 'users_by_degree.html',context)

def users_by_degree_ta(request):
    students = Author.objects.filter(degree="Teaching Assistant")
    ta_count = students.count()
    active_user = datetime.date.today

    if request.user.is_authenticated:
        user_sms =   request.user.author.contactprofile_set.all()
        #SMS
        admin_messages =  user_sms.filter(is_sent=True)
        sms_count = admin_messages.count()
    
        context ={'students': students, 'ta_count': ta_count, 'active_user': active_user, 'admin_messages': admin_messages, 'sms_count': sms_count}
        return render(request, 'users_by_degree.html',context)
    else:
        context ={'students': students, 'ta_count': ta_count, 'active_user': active_user}
        return render(request, 'users_by_degree.html',context)

def users_by_degree_al(request):
    students = Author.objects.filter(degree="Assistant Lecturer")
    al_count = students.count()
    active_user = datetime.date.today

    if request.user.is_authenticated:
        user_sms =   request.user.author.contactprofile_set.all()
        #SMS
        admin_messages =  user_sms.filter(is_sent=True)
        sms_count = admin_messages.count()
    
        context ={'students': students, 'al_count': al_count, 'active_user': active_user, 'admin_messages': admin_messages, 'sms_count': sms_count}
        return render(request, 'users_by_degree.html',context)
    else:
        context ={'students': students, 'al_count': al_count, 'active_user': active_user}
        return render(request, 'users_by_degree.html',context)

def users_by_degree_ap(request):
    students = Author.objects.filter(degree="Assistant Professor")
    ap_count = students.count()
    active_user = datetime.date.today

    if request.user.is_authenticated:
        user_sms =   request.user.author.contactprofile_set.all()
        #SMS
        admin_messages =  user_sms.filter(is_sent=True)
        sms_count = admin_messages.count()
    
        context ={'students': students, 'ap_count': ap_count, 'active_user': active_user, 'admin_messages': admin_messages, 'sms_count': sms_count}
        return render(request, 'users_by_degree.html',context)
    else:
        context ={'students': students, 'ap_count': ap_count, 'active_user': active_user}
        return render(request, 'users_by_degree.html',context)

def report(request, pk):
    memo = Report.objects.get(id=pk)
    report = Report.objects.all()
    users = User.objects.all()
    media = MediaUrl.objects.all()
   
    user_media = media.filter( author_id=memo.author)
    user_reports =  report.filter(author_id=memo.author)
    if request.user.is_authenticated:
        #SMS
        user_sms =   request.user.author.contactprofile_set.all()
        admin_messages =  user_sms.filter(is_sent=True)
        sms_count = admin_messages.count()

        context =   {'memo': memo, 'report': report, 'users': users, 'user_reports': user_reports, 'media': media, 'user_media': user_media, 'admin_messages': admin_messages, 'sms_count': sms_count}

        return render(request, 'report.html', context)
    else:
        context =   {'memo': memo, 'report': report, 'users': users, 'user_reports': user_reports, 'media': media, 'user_media': user_media}

        return render(request, 'report.html', context)

def latest_report(request):
    latest_memo = Report.objects.latest()
    report = Report.objects.all()
    users = User.objects.all()
    user_reports =  report.filter(author_id=latest_memo.author)

    if request.user.is_authenticated:
        #SMS
        user_sms =   request.user.author.contactprofile_set.all()
        admin_messages =  user_sms.filter(is_sent=True)
        sms_count = admin_messages.count()

        context =   { 'latest_memo': latest_memo, 'report': report, 'users': users, 'user_reports': user_reports, 'admin_messages': admin_messages, 'sms_count': sms_count}

        return render(request, 'latest_report.html', context)
    else:
        context =   { 'latest_memo': latest_memo, 'report': report, 'users': users, 'user_reports': user_reports}

        return render(request, 'latest_report.html', context)

@allowed_users(allowed_roles=['staff', 'customer', 'adminstration'])
def repo_form(request):
    if request.method == 'POST':
        form  =   ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.author = request.user.author
            report.save()

            messages.success(request, ('Your report was successfully added!'))
            return redirect("geology:latest_report")
        else:
            messages.error(request, form.errors)
        
    form = ReportForm()
    report = Report.objects.all()

    context={'form': form, 'report': report}
    return render(request,'report_form.html', context)

@allowed_users(allowed_roles=['staff', 'customer', 'adminstration'])
def repo_update(request, repo_id):
    users=request.user.author
    memo = Report.objects.get(id=repo_id ,author_id=users)

    form = ReportForm(request.POST or None, instance=memo)
    if form.is_valid():
        form.save()
        messages.success(request, 'Post Updated Successfully.')
        return redirect('geology:report', memo.id)
                                                            
    context = {'memo': memo, 'form': form}
    return render(request, 'report_update.html', context)

@allowed_users(allowed_roles=['staff', 'customer', 'adminstration'])
def repo_delete(request, id):
    users=request.user.author
    repo = get_object_or_404(Report, pk=id, author_id=users)
    context = {'repo': repo}

    if request.method == 'GET':
        return render(request, 'repo_confirm_delete.html', context)
    elif request.method == 'POST':
        repo.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('provile:adminpage')

def search_results(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        repo = Report.objects.filter(key_word__contains=searched)
        dic = Dectionary.objects.filter(key_words__contains=searched)
        rocks = Rock.objects.filter(key_word__contains=searched)

        context={'searched':searched, 'repo': repo, 'dic': dic, 'rocks': rocks}
        return render (request, 'search.html',context)
    else:
        return redirect('geology:home')
#####################################################################
def igneous_rock(request):
    rocks = Rock.objects.filter(rock_type= 'Igneous Rocks')

    if request.user.is_authenticated:
        #SMS
        user_sms =   request.user.author.contactprofile_set.all()
        admin_messages =  user_sms.filter(is_sent=True)
        sms_count = admin_messages.count()

        context = {'rocks': rocks, 'admin_messages': admin_messages, 'sms_count': sms_count}
        return render(request, 'igneous_rocks.html', context)
    else:
        context = {'rocks': rocks}
        return render(request, 'igneous_rocks.html', context)

def metamorphic_rock(request):
    rocks = Rock.objects.filter(rock_type= 'Metamorphic Rocks')

    if request.user.is_authenticated:
        #SMS
        user_sms =   request.user.author.contactprofile_set.all()
        admin_messages =  user_sms.filter(is_sent=True)
        sms_count = admin_messages.count()

        context = {'rocks': rocks, 'admin_messages': admin_messages, 'sms_count': sms_count}
        return render(request, 'metamorphic_rock.html', context)
    else:
        context = {'rocks': rocks}
        return render(request, 'metamorphic_rock.html', context)

def sedimentary_rock(request):
    rocks = Rock.objects.filter(rock_type= 'Sedimentary Rocks')

    if request.user.is_authenticated:
        #SMS
        user_sms =   request.user.author.contactprofile_set.all()
        admin_messages =  user_sms.filter(is_sent=True)
        sms_count = admin_messages.count()

        context = {'rocks': rocks, 'admin_messages': admin_messages, 'sms_count': sms_count}
        return render(request, 'sedimentary_rock.html', context)
    else:
        context = {'rocks': rocks}
        return render(request, 'sedimentary_rock.html', context)

def rock(request, rock_id):
    rock = Rock.objects.get(id=rock_id)
    rock_type = Rock.objects.filter(rock_type=rock.rock_type)
    author_rocks =  Rock.objects.filter(author_id= rock.author)
    
    context = {'author_rocks': author_rocks, 'rock': rock, 'rock_type': rock_type}
    return render(request, 'rock.html',context)

def new_rock(request):
    rock = Rock.objects.latest()
    rock_type = Rock.objects.filter(rock_type=rock.rock_type)
    context = {'rock': rock, 'rock_type': rock_type}
    return render(request, 'new_rock.html',context)

@allowed_users(allowed_roles=['staff', 'adminstration'])
def rock_form(request):
    
    if request.method == 'POST':
        form = RockForm(request.POST, request.FILES)
        if form.is_valid():
            rocks = form.save(commit=False)
            rocks.author = request.user.author
            rocks.save()

            messages.success(request, 'Success added a new rock!')
            return redirect('geology:new_rock')
        else:
            messages.error(request, form.errors)

    rocks = Rock.objects.all()
    form = RockForm()
    context = {'rocks': rocks, 'form': form}
    return render(request, 'rock_form.html',context)

@allowed_users(allowed_roles=['staff', 'adminstration'])
def rock_update(request, repo_id):
    users=request.user.author
    memo = Rock.objects.get(id=repo_id ,author_id=users)

    form = RockForm(request.POST or None, instance=memo)
    if form.is_valid():
        form.save()
        messages.success(request, 'Updated Successfully.')
        return redirect('geology:rock', memo.id)
                                                            
    context = {'memo': memo, 'form': form}
    return render(request, 'rock_update.html', context)

@allowed_users(allowed_roles=['staff', 'adminstration'])
def rock_delete(request, id):
    myuser = request.user.author
    rock = get_object_or_404(Rock, pk=id, author_id=myuser)

    context = {'rock': rock}

    if request.method == 'GET':
        return render(request, 'delete_rock.html', context)
    elif request.method  == 'POST':
        rock.delete()
        messages.success(request, 'The Rock has been deleted ')
        return redirect('provile:adminpage')

@allowed_users(allowed_roles=['staff', 'adminstration'])
def rock_delete_admin(request, id):
    rock = get_object_or_404(Rock, pk=id)

    context = {'rock': rock}

    if request.method == 'GET':
        return render(request, 'delete_rock.html', context)
    elif request.method  == 'POST':
        rock.delete()
        messages.success(request, 'The Rock has been deleted ')
        return redirect('geology:home')

    ###############################################

###############MINERALS PAGES#####################
@allowed_users(allowed_roles=['staff', 'adminstration'])
def mineral_form(request):
    if request.method == 'POST':
        form = MineralForm(request.POST, request.FILES)
        if form.is_valid():
            minerals =form.save(commit=False)
            minerals.author = request.user.author
            minerals.save()

            messages.success(request, 'Your mineral has been posted')
            return redirect('geology:new_mineral')

        else:
            messages.error(request, form.errors)
    minerals = Mineral.objects.all()
    form = MineralForm()

    context = {'minerals': minerals, 'form': form}
    return render(request, 'mineral_form.html',context)

def new_mineral(request):
    mineral = Mineral.objects.latest()
    mineral_class = Mineral.objects.filter(classes=mineral.classes)
    mineral_author = Mineral.objects.filter(author=mineral.author)
    

    context = {'mineral': mineral, 'mineral_class': mineral_class, 'mineral_author': mineral_author}
    return render(request, 'new_mineral.html',context)

def minerals(request):
    minerals = Mineral.objects.all()
    mineral = Mineral.objects.all()
    myFilter = MineralFilter(request.GET, queryset=minerals)
    minerals = myFilter.qs

    if request.user.is_authenticated:
        #SMS
        user_sms =   request.user.author.contactprofile_set.all()
        admin_messages =  user_sms.filter(is_sent=True)
        sms_count = admin_messages.count()

        context = {'minerals' : minerals, 'myFilter': myFilter, 'mineral': mineral, 'admin_messages':admin_messages, 'sms_count': sms_count}
        return render(request, 'minerals.html',context)
    else:
        context = {'minerals' : minerals, 'myFilter': myFilter, 'mineral': mineral}
        return render(request, 'minerals.html',context)

def mineral_detail(request, mineral_id):
    mineral = Mineral.objects.get(id=mineral_id)
    minerals = Mineral.objects.filter(classes=mineral.classes)
    mineral_author = Mineral.objects.filter(author=mineral.author)

    context = {'mineral': mineral, 'minerals': minerals, 'mineral_author': mineral_author}
    return render(request, 'mineral_details.html',context)

@allowed_users(allowed_roles=['staff', 'adminstration'])
def mineral_update(request, repo_id):
    users=request.user.author
    memo = Mineral.objects.get(id=repo_id ,author_id=users)

    form = MineralForm(request.POST or None, instance=memo)
    if form.is_valid():
        form.save()
        messages.success(request, 'Updated Successfully.')
        return redirect('geology:mineral_detail', memo.id)
                                                            
    context = {'memo': memo, 'form': form}
    return render(request, 'mineral_update.html', context)

def mineral_update_admin(request, repo_id):
    memo = Mineral.objects.get(id=repo_id )
    mineral = Mineral.objects.all()
    form = MineralForm(request.POST or None, instance=memo)
    if form.is_valid():
        mineral = form.save(commit=False)
        mineral.edit_by = request.user
        mineral.save()

        messages.success(request, 'Updated Successfully.')
        return redirect('geology:mineral_detail', memo.id)
                                                            
    context = {'memo': memo, 'form': form, 'mineral': mineral}
    return render(request, 'mineral_update.html', context)

@allowed_users(allowed_roles=['staff', 'adminstration'])
def mineral_delete(request, id):
    myuser = request.user.author
    mineral = get_object_or_404(Mineral, pk=id, author_id=myuser)

    context = {'mineral': mineral}

    if request.method == 'GET':
        return render(request, 'delete_mineral.html', context)
    elif request.method  == 'POST':
        mineral.delete()
        messages.success(request, 'Has been deleted ')
        return redirect('provile:adminpage')

@allowed_users(allowed_roles=['staff', 'adminstration'])
def mineral_delete_admin(request, id):
    mineral = get_object_or_404(Mineral, pk=id)

    context = {'mineral': mineral}

    if request.method == 'GET':
        return render(request, 'delete_mineral.html', context)
    elif request.method  == 'POST':
        mineral.delete()
        messages.success(request, 'Has been deleted ')
        return redirect('geology:minerals')
#########################################################
def faq(request):
    faq = FAQ.objects.filter(is_active=True)
    if request.user.is_authenticated:
        #SMS
        user_sms =   request.user.author.contactprofile_set.all()
        admin_messages =  user_sms.filter(is_sent=True)
        sms_count = admin_messages.count()

        context = {'faq': faq, 'admin_messages': admin_messages, 'sms_count': sms_count}
        return render(request, 'faq.html', context)
    else:
        context = {'faq': faq}
        return render(request, 'faq.html', context)

def answered_faq(request):
    if request.method == 'GET':
        faq = FAQ.objects.filter(is_active=False)
        faq_count = faq.count()
        if request.user.is_authenticated:
            #SMS
            user_sms =   request.user.author.contactprofile_set.all()
            admin_messages =  user_sms.filter(is_sent=True)
            sms_count = admin_messages.count()
            context = {'faq': faq, 'faq_count': faq_count,  'admin_messages': admin_messages, 'sms_count': sms_count}
            return render(request, 'faq_answered.html', context)
        else:
            context = {'faq': faq,'faq_count': faq_count, }
            return render(request, 'faq_answered.html', context)
    elif request.method == 'POST':
        search_faq = request.POST['search_faq']
        faqs = FAQ.objects.filter(question__contains=search_faq, is_active=False)
        faq = FAQ.objects.filter(is_active=False)
        faq_count = faq.count()
        if request.user.is_authenticated:
            #SMS
            user_sms =   request.user.author.contactprofile_set.all()
            admin_messages =  user_sms.filter(is_sent=True)
            sms_count = admin_messages.count()
        
            context = {'faq': faq, 'faqs': faqs, 'faq_count': faq_count, 'search_faq': search_faq, 'admin_messages': admin_messages, 'sms_count': sms_count}
            return render(request, 'faq_answered.html', context)
        else:
            context = {'faq': faq, 'faqs': faqs, 'faq_count': faq_count,  'search_faq': search_faq}
            return render(request, 'faq_answered.html', context)
    else:
        return redirect('geology:faq_answered')

def faqform(request):
    faq = FAQ.objects.all()
  
    form =FaqForm()
    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            faq=form.save(commit=False)
            faq.author = request.user.author
            faq.save()

            messages.success(request, 'Your question has been send, well reply you soon')
            return redirect('geology:faq_answered')
        else:
            messages.error(request, form.errors)

                                                            
    context = {'form': form, 'faq': faq}
    return render(request, 'faqform.html', context)
        
#############################################################3
def cv(request):
    context ={}
    return render(request, 'cv.html', context)


    

