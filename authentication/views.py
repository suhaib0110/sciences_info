from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from sciences import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string 
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .tokens import generate_token
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from six import text_type
from geology.decorators import unauthenticated_user
from geology.models import Author
from provile.models import Skill
from provile.forms import AdminUserForm, UpdateProfileForm
from geology.forms import AuthorForm, createUserForm
from geology.decorators import unauthenticated_user, admin_only

@unauthenticated_user
def signup(request):
    if request.method == 'POST':

        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, 'This username already existed')
            return redirect('authentication:signup')
            
        if User.objects.filter(email=email):
            messages.error(request, 'This Email already registered')
            return redirect('authentication:signup')
            
        if len(username)>10:
            messages.error(request, 'username mast be under 10 characters')
            return redirect('authentication:signup')
            
        if len(username)<4:
            messages.error(request, 'username mast more than 4 characters')
            return redirect('authentication:signup')
            
        if not username.isalnum():
            messages.error(request, 'username must be Alpha-Numeric')
            return redirect('authentication:signup')
            

        if len(fname)>10:
            messages.error(request, 'Frist Name mast be under 10 characters')
            return redirect('authentication:signup')
            
        if len(fname)<4:
            messages.error(request, 'First Name mast by more than 4 characters')
            return redirect('authentication:signup')
            
        if not fname.isalpha(): 
            messages.error(request, 'The characters in frist name must be letters')
            return redirect('authentication:signup')

        if not lname.isalpha(): 
            messages.error(request, 'The characters in last name must be letters')
            return redirect('authentication:signup')

        if len(lname)>10:
            messages.error(request, 'Last Name mast be under 10 characters')
            return redirect('authentication:signup')

        if len(lname)<4:
            messages.error(request, 'Last Name must be more than 4 characters')
            return redirect('authentication:signup')

        if len(pass1)<6:
            messages.error(request, 'Password must be more than 6 characters')
            return redirect('authentication:signup')

        if pass1 != pass2:
            messages.error(request, 'password did not match')
            return redirect('authentication:signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        #myuser.is_active = False

        

        myuser.save()

        group = Group.objects.get(name='customer')
        myuser.groups.add(group)

        
        messages.success(request, 'Your accont has been successfolly created, please confirmation your email in order to active your accout.')
        return redirect('authentication:signin_new')
    

        #Welcome Email
        '''
        subject = "Welcome to SciencesInfo"
        message = "Hello" + myuser.first_name + "!! \n" + "welcame SciencesInfo \n Thank You"
        from_email = [settings.EMAIL_HOST_USER]
        to_list = [myuser,email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        #Email Address Confirmation Email

        current_site = get_current_site(request)
        email_subject = text_type("Confirm your email @ SciencesInfo")
        message2 = render_to_string('email_confirmation.html', {
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser),
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email]
        )
        email.fail_silently= True
        email.send()

        '''

    


    return render(request, 'authentication\signup.html')
    
@unauthenticated_user
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            context = {'fname': fname}
            return redirect('provile:adminpage')
        else:

            messages.error(request, 'Username or Password wrong')


    return render(request, 'authentication\signin.html')

def signin_new(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            context = {'fname': fname}
            return redirect('provile:userprofile_new')
        else:

            messages.error(request, 'Username or Password wrong')


    return render(request, 'authentication\signin_new.html')

def signout(request):
    logout(request)
    return redirect('geology:home')
'''
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('geology:home')
    else:
        return render(request, 'activation_failed.html')
'''

@admin_only
def admin_update_user(request, user_id):
    users =User.objects.get(id=user_id)
    group = Group.objects.all()
    form =AdminUserForm(instance=users)
    if request.method == 'POST':
        form = AdminUserForm(request.POST, instance=users)
        if form.is_valid():
            form.save()

            messages.success(request, 'User Updated Successfully.')
            return redirect('provile:adminpage')
        else:
            messages.error(request, form.errors)

                                                            
    context = {'form': form,'group': group, 'users': users}
    return render(request, 'authentication/admin_apdate_user.html', context)

@admin_only
def delete_user(request, id):
    users = get_object_or_404(User, pk=id)
    context = {'users': users}

    if request.method == 'GET':
        return render(request, 'authentication/user_confirm_delete.html', context)
    elif request.method == 'POST':
        users.delete()
        messages.success(request,  'User has been deleted successfully.')
        return redirect('provile:adminpage')
