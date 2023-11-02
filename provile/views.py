from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from geology.decorators import unauthenticated_user, allowed_users, admin_only
from geology.models import Report, Author, Rock, Mineral, FAQ
from .models import Skill, Certificate, Experience, MediaUrl, ContactProfile
from .forms import (SkillForm, CertificateForm, ExperienceForm, MediaUrlForm, UpdateUserForm,
                    UpdateProfileForm, AdminEditReportForm, FaqFormAdmin, ContactForm, ContactFormReplay, ContactFormSend)
from geology.forms import AuthorForm, createUserForm, RockForm
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.conf import settings
from authentication.filters import UserFilter


##########START ADMIN PAGE#########
'''
import used:
-from django.contrib.auth.decorators import login_required
-from geology.decorators import admin_only
-from geology.models import Report, Author
-from .models import Skill, Certificate, Experience, MediaUrl
-from django.contrib.auth.models import User, Group
-from authentication.filters import UserFilter
-from django.shortcuts import render
'''
@login_required
@admin_only
def adminpage(request):
    #Preparing models:
    reports =   request.user.author.report_set.all() #use in POSTs title to git user's post.
    skills =   request.user.author.skill_set.all()   #use in Skills title to git user's skills.
    certificates =   request.user.author.certificate_set.all() #...
    experiences =   request.user.author.experience_set.all() #...
    rocks = request.user.author.rock_set.all()
    minerals = request.user.author.mineral_set.all()
    media =   request.user.author.mediaurl_set.all() #Social media url: facebook, twitter, ins, linkedin.
    
    #FAQ
    faq = FAQ.objects.filter(is_active=True)
    faq_count = faq.count()

    #SMS
    sms = ContactProfile.objects.filter(is_active=True)
    sms_count = sms.count()

    #Filtering users by group:
    Admin_users = User.objects.filter(groups__name__in=['staff'])
    customer_users = User.objects.filter(groups__name__in=['customer'])

    #Filtering customer user by search box:
    myFilter = UserFilter(request.GET, queryset=customer_users) #This variable using django-filter tools which install in first by pip and added to install-app in settings. i using here a form UserFilter from filters.py in authentication app.
    customer_users = myFilter.qs

    #Count customer users:
    user_cout = customer_users.count()
    admin_cout = Admin_users.count()

    context = {'skills': skills, 'user_cout': user_cout, 'admin_cout': admin_cout, 'Admin_users': Admin_users, 'reports': reports,
                'customer_users': customer_users, 'certificates': certificates,
                'experiences': experiences, 'media': media, 'myFilter': myFilter,
                'rocks': rocks, 'faq': faq, 'faq_count': faq_count, 'sms_count': sms_count,
                'minerals': minerals}

    return render(request, 'adminpage.html', context)
###############END ADMIN PAGE##############

##########START STAFF PAGE#########
'''
import used:
-from django.contrib.auth.decorators import login_required
-from geology.decorators import allowed_users
-from geology.models import Report, Author
-from .models import Skill, Certificate, Experience, MediaUrl
-from django.contrib.auth.models import User
-from django.shortcuts import render
'''
@login_required
@allowed_users(allowed_roles=['staff'])
def stafpage(request):
    #Preparing models:
    reports =   request.user.author.report_set.all()
    skills =   request.user.author.skill_set.all()
    certificates =   request.user.author.certificate_set.all()
    experiences =   request.user.author.experience_set.all()
    media =   request.user.author.mediaurl_set.all()
    rocks = request.user.author.rock_set.all()
    minerals = request.user.author.mineral_set.all()
    user_sms =   request.user.author.contactprofile_set.all()
    author = request.user.author
    #SMS
    admin_messages =  user_sms.filter(is_sent=True)
    sms_count = admin_messages.count()

    context ={'reports': reports, 'skills': skills, 'author': author, 
            'certificates': certificates,'experiences': experiences,
             'media': media, 'rocks': rocks, 'minerals': minerals,
              'sms_count': sms_count, 'admin_messages': admin_messages}
    return render(request, 'stafpage.html', context)
###############END STAFF PAGE##############

@login_required
@allowed_users(allowed_roles=['customer'])
def userpage(request):
    reports =   request.user.author.report_set.all()
    skills =   request.user.author.skill_set.all()
    certificates =   request.user.author.certificate_set.all()
    experiences =   request.user.author.experience_set.all()
    media =   request.user.author.mediaurl_set.all()
    user_sms =   request.user.author.contactprofile_set.all()
    author = request.user.author
    #SMS
    admin_messages =  user_sms.filter(is_sent=True)
    sms_count = admin_messages.count()
   

    context ={'reports': reports, 'skills': skills, 'author': author,
            'certificates': certificates, 'experiences': experiences,
             'media': media, 'sms_count': sms_count, 'admin_messages': admin_messages}
    return render(request, 'userpage.html',context)

@login_required
def userprofile_new(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.author)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated successfully Welcome in GeologySD Community, now you can add your Skills, Certifications and Experiences.')
            return redirect('provile:adminpage')
        
    else:
        form = UpdateProfileForm(instance=request.user.author)

    context = {'form': form}
    return render(request, 'userprofile_new.html', context)


@login_required
def userprofile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.author)

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']


        if len(username)>10:
            messages.error(request, 'username must be less than 10 characters')
            return redirect('provile:userprofile')

        if len(username)<4:
            messages.error(request, 'Username must be more than 4 characters')
            return redirect('provile:userprofile')

        if not username.isalnum(): 
            messages.error(request, 'username must be Alpha-Numeric')
            return redirect('provile:userprofile')

        if not first_name.isalpha(): 
            messages.error(request, 'The characters in frist name must be letters')
            return redirect('provile:userprofile')

        if not last_name.isalpha(): 
            messages.error(request, 'The characters in last name must be letters')
            return redirect('provile:userprofile')

        if user_form.is_valid() and profile_form.is_valid():
            
            
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('provile:adminpage')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.author)

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'userprofile.html', context)

def viewUserpage(request, auth_id):
    reports =   Author.objects.get(id=auth_id)
    

    auther =  Report.objects.all()
    skills =   Skill.objects.all()
    certificates= Certificate.objects.all()
    experiences= Experience.objects.all()
    media = MediaUrl.objects.all()
    
    user_reports =  auther.filter(author_id=reports)
    user_skills = skills.filter( author_id=reports)
    user_certificates = certificates.filter( author_id=reports)
    user_experiences = experiences.filter( author_id=reports)
    user_media = media.filter( author_id=reports)

    if request.user.is_authenticated:
        #SMS
        user_sms =   request.user.author.contactprofile_set.all()
        admin_messages =  user_sms.filter(is_sent=True)
        sms_count = admin_messages.count()

        context ={'reports': reports, 'user_reports': user_reports, 'auther': auther, 'skills': skills, 'user_skills': user_skills,
        'certificates': certificates, 'user_certificates': user_certificates,
        'experiences': experiences, 'user_experiences': user_experiences, 'media': media, 'user_media': user_media, 'admin_messages': admin_messages, 'sms_count': sms_count}
        return render(request, 'viewuserpage.html', context)
    else:
        context ={'reports': reports, 'user_reports': user_reports, 'auther': auther, 'skills': skills, 'user_skills': user_skills,
        'certificates': certificates, 'user_certificates': user_certificates,
        'experiences': experiences, 'user_experiences': user_experiences, 'media': media, 'user_media': user_media}
        return render(request, 'viewuserpage.html', context)


@allowed_users(allowed_roles=['staff', 'customer', 'adminstration'])
def skill(request):
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            skills = form.save(commit=False)
            skills.author = request.user.author
            skills.save()

            messages.success(request, 'New skill was uploted successfully')
            return redirect('provile:skill')
        else:
            messages.error(request,'Skill degree ovrage must be btween 5-100 !')
           

    context = {'form': form}
    return render(request, 'skill_form.html', context)


@allowed_users(allowed_roles=['staff', 'customer', 'adminstration'])
def edite_skill(request, skill_id):
    skills =Skill.objects.get(id=skill_id)

    form = SkillForm(request.POST or None, instance=skills)
    if form.is_valid():
        form.save()

        messages.success(request, 'Updated Successfully..')
        return redirect('provile:adminpage')

    else:
        messages.error(request, 'Skill degree value must be btween 5-100 !')

    context = {'skills': skills, 'form': form}
    return render(request, 'edite_skill.html', context)


@allowed_users(allowed_roles=['staff', 'customer', 'adminstration'])
def delete_skill(request, skill_id):
    skills = get_object_or_404(Skill, pk=skill_id)
    context = {'skills': skills}

    if request.method == 'GET':
        return render(request, 'skill_confirm_delete.html', context)
    elif request.method == 'POST':
        skills.delete()
        messages.success(request,  'Skill has been deleted successfully.')
        return redirect('provile:adminpage')  


@allowed_users(allowed_roles=['staff', 'customer', 'adminstration'])
def certificate(request):
    form = CertificateForm()

    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            certificates = form.save(commit=False)
            certificates.author = request.user.author
            certificates.save()

            messages.success(request, 'New Certificate was uploted successfully')
            return redirect('provile:certificate')
        else:
            messages.error(request, form.errors)
           

    context = {'form': form}
    return render(request, 'certificate_form.html', context)


@allowed_users(allowed_roles=['staff', 'customer', 'adminstration'])
def edite_certificate(request, certificate_id):
    certificate =Certificate.objects.get(id=certificate_id)
    form = CertificateForm(instance=certificate)
    if request.method == 'POST':

        form = CertificateForm(request.POST, request.FILES , instance=certificate)
        if form.is_valid():
            form.save()

            messages.success(request, 'Updated Successfully..')
            return redirect('provile:adminpage')

        else:
            messages.error(request, form.errors)

    context = {'certificate': certificate, 'form': form}
    return render(request, 'edite_certificate.html', context)


@allowed_users(allowed_roles=['staff', 'customer', 'adminstration'])
def delete_certificate(request, certificate_id):
    certificates = get_object_or_404(Certificate, pk=certificate_id)
    context = {'certificates': certificates}

    if request.method == 'GET':
        return render(request, 'certificate_delete.html', context)
    elif request.method == 'POST':
        certificates.delete()
        messages.success(request,  'Object has been deleted.')
        return redirect('provile:adminpage')  


@allowed_users(allowed_roles=['staff', 'customer', 'adminstration'])
def experience(request):
    form = ExperienceForm()

    if request.method == 'POST':
        

        form = ExperienceForm(request.POST, request.FILES)
        if form.is_valid():
            date_from = request.POST['date_from']
            date_to = request.POST['date_to']

            if (date_from) >= (date_to):
                messages.error(request, 'date to most be greater than date from')
                return redirect('provile:experience')

            experience = Experience.objects.all()
            experience.date_from = date_from
            experience.date_to = date_to
            experiences = form.save(commit=False)
            experiences.author = request.user.author
            experiences.save()

            messages.success(request, 'New Experience was uploted successfully')
            return redirect('provile:experience')
        else:
            messages.error(request, form.errors)
    context = {'form': form}
    return render(request, 'experience_form.html', context)


@allowed_users(allowed_roles=['staff', 'customer', 'adminstration'])
def edite_experience(request, experience_id):
    experience =Experience.objects.get(id=experience_id)
    form = ExperienceForm(instance=experience)
    if request.method == 'POST':

        form = ExperienceForm(request.POST, request.FILES , instance=experience)
        if form.is_valid():
            date_from = request.POST['date_from']
            date_to = request.POST['date_to']
            if (date_from) >= (date_to):
                messages.error(request, " 'date to' most be greater than 'date from' ")
                return redirect('provile:experience')

            experience = Experience.objects.all()
            experience.date_from = date_from
            experience.date_to = date_to
            form.save()

            messages.success(request, 'Updated Successfully..')
            return redirect('provile:adminpage')

        else:
            messages.error(request, form.errors)

    context = {'experience': experience, 'form': form}
    return render(request, 'edite_experience.html', context)

@allowed_users(allowed_roles=['staff', 'customer', 'adminstration'])
def delete_experience(request, experience_id):
    experiences = get_object_or_404(Experience, pk=experience_id)
    context = {'experiences': experiences}

    if request.method == 'GET':
        return render(request, 'experience_delete.html', context)
    elif request.method == 'POST':
        experiences.delete()
        messages.success(request,  'Object has been deleted.')
        return redirect('provile:adminpage')  


@allowed_users(allowed_roles=['staff', 'customer', 'adminstration'])
def media(request):
    form = MediaUrlForm()

    if request.method == 'POST':
        form = MediaUrlForm(request.POST, request.FILES)
        if form.is_valid():
            medias = form.save(commit=False)
            medias.author = request.user.author
            medias.save()

            messages.success(request, 'New Media was uploted successfully')
            return redirect('provile:media')
        else:
            messages.error(request, form.errors)

    context = {'form': form}
    return render(request, 'media_form.html', context)


@allowed_users(allowed_roles=['staff', 'customer', 'adminstration'])
def edite_media_url(request, media_id):
    media = MediaUrl.objects.get(id=media_id)
    form = MediaUrlForm(instance=media)

    if request.method == 'POST':
        form = MediaUrlForm(request.POST, request.FILES, instance=media)
        if form.is_valid():
            form.save()
            messages.success(request, 'your media contact updated')
            return redirect('provile:adminpage')

        else:
            messages.error(request, form.errors)

    context = {'media': media, 'form': form}
    return render(request, 'edite_media.html', context)


@allowed_users(allowed_roles=['staff', 'customer', 'adminstration'])
def delete_media_url(request, media_id):
    media_url = get_object_or_404(MediaUrl, pk=media_id)
    context = {'media_url': media_url}

    if request.method == 'GET':
        return render(request, 'media_url_delete.html', context)
    if request.method == 'POST':
        media_url.delete()
        messages.success(request,  'Object has been deleted.')
        return redirect('provile:adminpage')  


@allowed_users(allowed_roles=['staff', 'adminstration'])
def admin_edit_report(request, user_id):
    reports =Report.objects.get(id=user_id)
    repo = Report.objects.all()
  
    form =AdminEditReportForm(instance=reports)
    if request.method == 'POST':
        form = AdminEditReportForm(request.POST, instance=reports)
        if form.is_valid():
            repo=form.save(commit=False)
            repo.edit_by = request.user
            repo.save()

            messages.success(request, 'Post Updated Successfully.')
            return redirect('geology:report', reports.id)
        else:
            messages.error(request, form.errors)

                                                            
    context = {'form': form,'reports': reports, 'repo': repo}
    return render(request, 'admin_edit_report.html', context)

@allowed_users(allowed_roles=['staff','adminstration'])
def admin_delete_post(request, id):
    reports = get_object_or_404(Report, id=id)
    context = {'reports': reports}

    if request.method == 'GET':
        return render(request, 'delete_post_by_admin.html', context)
    elif request.method == 'POST':
        reports.delete()
        messages.success(request,  'User has been deleted successfully.')
        return redirect('geology:home')


@allowed_users(allowed_roles=['staff', 'adminstration'])
def admin_edit_rock(request, user_id):
    rocks =Rock.objects.get(id=user_id)
    rock = Rock.objects.all()
  
    form =RockForm(instance=rocks)
    if request.method == 'POST':
        form = RockForm(request.POST, instance=rocks)
        if form.is_valid():
            rock=form.save(commit=False)
            rock.edit_by = request.user
            rock.save()

            messages.success(request, 'Updated Successfully.')
            return redirect('geology:rock', rocks.id)
        else:
            messages.error(request, form.errors)

                                                            
    context = {'form': form,'rocks': rocks, 'rock': rock}
    return render(request, 'admin_edit_rock.html', context)

@admin_only
def admin_answer_faq(request, user_id):
    faqs =FAQ.objects.get(id=user_id)
    faq = FAQ.objects.all()
  
    form =FaqFormAdmin(instance=faqs)
    if request.method == 'POST':
        form = FaqFormAdmin(request.POST, request.FILES, instance=faqs)
        if form.is_valid():
            faq=form.save(commit=False)
            faq.is_active = False
            faq.save()

            messages.success(request, 'Answered..')
            return redirect('geology:faq')
        else:
            messages.error(request, form.errors)

                                                            
    context = {'form': form,'faqs': faqs, 'faq': faq}
    return render(request, 'admin_answer_faq.html', context)

@admin_only
def delete_faq(request, id):
    faq = get_object_or_404(FAQ, id=id)
    context = {'faq': faq}

    if request.method == 'GET':
        return render(request, 'delete_faq.html', context)
    elif request.method == 'POST':
        faq.delete()
        messages.success(request,  'Question has been deleted')
        return redirect('geology:faq')

@admin_only
def replaysms(request):
    sms = ContactProfile.objects.filter(is_active=True)
    user_sms =   request.user.author.contactprofile_set.all()
    sms_back = ContactProfile.objects.filter(is_active=False)
    #SMS
    admin_messages =  user_sms.filter(is_sent=True)
    sms_count = admin_messages.count()

    context = {'sms': sms, 'sms_back': sms_back, 'admin_messages': admin_messages, 'sms_count': sms_count}
    return render(request, 'sms_admin.html', context)

@admin_only
def admin_replay_sms(request, user_id):
    sms = ContactProfile.objects.filter(is_active=True)
    sms_back = ContactProfile.objects.filter(is_active=False)
    faqs =ContactProfile.objects.get(id=user_id)
    faq = ContactProfile.objects.filter(author_id=faqs.author_id)
    user_sms =   request.user.author.contactprofile_set.all()
    #SMS
    admin_messages =  user_sms.filter(is_sent=True)
    sms_count = admin_messages.count()
    form =ContactFormReplay(instance=faqs)
    if request.method == 'POST':
        form = ContactFormReplay(request.POST, instance=faqs)
        if form.is_valid():
            faq=form.save(commit=False)
            faq.is_active = False
            faq.is_sent = True
            faq.save()

            messages.success(request, 'Answered..')
            return redirect('provile:replaysms')
        else:
            messages.error(request, form.errors)

                                                            
    context = {'sms': sms, 'sms_back': sms_back, 'form': form,'faqs': faqs, 'faq': faq, 'admin_messages': admin_messages, 'sms_count': sms_count}
    return render(request, 'sms_admin.html', context)

def user_sms(request):
    sms = request.user.author.contactprofile_set.all()
    user_sms =  sms.filter(is_sent=True)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.author = request.user.author
            contact.save()
            
            messages.info(request, "We received your massege, w'll replay you soon, chik  Messages Box.")
        else:
            messages.error(request, form.errors)
    form = ContactForm()
    contact = ContactProfile.objects.all()

    user_sms =   request.user.author.contactprofile_set.all()
    #SMS
    admin_messages =  user_sms.filter(is_sent=True)
    sms_count = admin_messages.count()

    context = {'sms': sms, 'user_sms': user_sms, 'form': form, 'contact': contact, 'admin_messages': admin_messages, 'sms_count': sms_count}
    return render(request, 'user_sms.html', context)

def user_sms_id(request, sms_id):
    faqs =ContactProfile.objects.get(id=sms_id)
    faq = ContactProfile.objects.all()
    form =ContactFormSend(instance=faqs)
    if request.method == 'POST':
        form = ContactFormSend(request.POST, instance=faqs)
        if form.is_valid():
            faq=form.save(commit=False)
            faq.is_sent = False
            faq.save()

            return redirect('provile:user_sms')
        else:
            messages.error(request, form.errors)

                                                            
    context = {'form': form,'faqs': faqs, 'faq': faq}
    return render(request, 'user_sms_id.html', context)

def message_sms_id(request, sms_id):
    faqs =ContactProfile.objects.get(id=sms_id)
    sms = request.user.author.contactprofile_set.all()
    user_sms =   request.user.author.contactprofile_set.all()
    #SMS
    admin_messages =  user_sms.filter(is_sent=True)
    sms_count = admin_messages.count()

    context = {'faqs': faqs, 'sms': sms, 'admin_messages': admin_messages, 'sms_count': sms_count}
    return render(request, 'user_sms.html', context)

