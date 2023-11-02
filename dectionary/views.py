#This Project with all app insite Created By: SUHAIB TAHA ALRIAH
#Email: alromys47@gmail.com

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dectionary
from .forms import DectionaryForm
from django.contrib import messages
from django.conf import settings
from geology.decorators import allowed_users


###START Dectionary link page###
'''
dec --> Dectionary
This is link dec page to main dec page 'geo_dec_results' 
contain a search button, and additional link
linked directery to navbar.
'''
def index(request):
    if request.method == 'GET':
        #SMS
        if request.user.is_authenticated:
            user_sms =   request.user.author.contactprofile_set.all()
            admin_messages =  user_sms.filter(is_sent=True)
            sms_count = admin_messages.count()
            return render(request, 'geo_dec.html', {'admin_messages': admin_messages, 'sms_count': sms_count})
        else:
            return render(request, 'geo_dec.html')
    elif request.method == 'POST':
        chick = request.POST['chick'] #Pass input name to variable.
        dectionary = Dectionary.objects.filter(key_words__contains=chick) #Filter the model using chick variable.

        #SMS
        if request.user.is_authenticated:
            user_sms =   request.user.author.contactprofile_set.all()
            admin_messages =  user_sms.filter(is_sent=True)
            sms_count = admin_messages.count()
            context={'chick': chick, 'dectionary': dectionary, 'admin_messages': admin_messages, 'sms_count': sms_count}
            return render(request, 'geo_dec.html', context)
        else:
            context={'chick': chick, 'dectionary': dectionary}
            return render(request, 'geo_dec.html', context)
###START Dectionary main page###
#__________________________________________________________

###START Dectionary main page###
def geo_dec_results(request, dic_id):
    dics = Dectionary.objects.get(id=dic_id)
    #SMS
    if request.user.is_authenticated:
        user_sms =   request.user.author.contactprofile_set.all()
        admin_messages =  user_sms.filter(is_sent=True)
        sms_count = admin_messages.count()

        context ={'dics': dics, 'admin_messages': admin_messages, 'sms_count': sms_count}
        return render(request, 'geo_dec_results.html', context)
    else:
        context ={'dics': dics}
        return render(request, 'geo_dec_results.html', context)
###END Dectionary main page###

@allowed_users(allowed_roles=['adminstration', 'staff'])
def dectionary_form(request):
    if request.method == 'POST':
        form = DectionaryForm(request.POST)
        if form.is_valid():
            dectionary = form.save(commit=False)
            dectionary.author = request.user.author
            dectionary.save()
            messages.success(request, ('successfully uploaded'))
        else:
            messages.error(request, form.errors)

        return redirect('dectionary:dectionary_form')
    
    form = DectionaryForm()
    dectionary = Dectionary.objects.all()
    context = {'form': form, 'dectionary': dectionary}

    return render(request, 'dectionary_form.html',context)

def dectionary_form_edit(request, id):
    dectionary = Dectionary.objects.get(id=id)
    dics =Dectionary.objects.all()
    form = DectionaryForm(instance=dectionary)
    if request.method == 'POST':
        form = DectionaryForm(request.POST, instance=dectionary)
        if form.is_valid():
            dics = form.save(commit=False)
            dics.edit_by = request.user
            dics.save()
            messages.success(request, 'successfully Updated..')
            return redirect('dectionary:geo_dec')
        else:
            messages.error(request, form.errors)
    
    context = {'dectionary': dectionary, 'form': form}
    return render(request, 'dectionary_form.html',context)

