from django import forms
from .models import Skill, ContactProfile, Certificate, Experience, MediaUrl
from django.contrib.auth.models import User
from geology.models import Author, Report, FAQ


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, 
    widget= forms.TextInput(attrs={
        'class': 'form-control',
    }))

    first_name = forms.CharField(max_length=100, required=True, 
    widget= forms.TextInput(attrs={
        'class': 'form-control'
    }))

    last_name = forms.CharField(max_length=100, required=True, 
    widget= forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class AdminUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, 
    widget= forms.TextInput(attrs={
        'class': 'form-control',
    }))

    first_name = forms.CharField(max_length=100, required=True, 
    widget= forms.TextInput(attrs={
        'class': 'form-control'
    }))

    last_name = forms.CharField(max_length=100, required=True, 
    widget= forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'groups', 'last_login', 'is_active', 'is_staff')

class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={
        'class' : 'form-control-file'
    }))

    title = forms.CharField(max_length=400, required=True, 
    widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    user_bio = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control-file',
            'rows': 5
        }
    ))

    cv = forms.FileField(widget=forms.FileInput(attrs={
        'class' : 'form-control-file'
    }))

    class Meta:
        model = Author
        fields = ('avatar', 'title', 'degree', 'user_bio', 'cv')



class SkillForm(forms.ModelForm):
    name = forms.CharField(max_length=20, required=True,
    widget=forms.TextInput(attrs={
        'placeholder': 'Skill name..'
    }))

    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['author']

class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactProfile
        fields = ('title', 'message')

class ContactFormReplay(forms.ModelForm):


    class Meta:
        model = ContactProfile
        fields = ('replay', 'is_sent')

class ContactFormSend(forms.ModelForm):


    class Meta:
        model = ContactProfile
        fields = ('is_sent',)

class CertificateForm(forms.ModelForm):
    date = forms.DateTimeField(required=True,
        widget=forms.DateTimeInput(attrs={
            'type': 'date',
         
        })
    )

    name = forms.CharField(max_length=50, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Certificate from..',
            'class': 'form-control',
        }))
        
    title = forms.CharField(max_length=50, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Certificate name..',
            'class': 'form-control'
        }))

    description = forms.CharField(max_length=1000, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Description..',
            'rows': 6,
        }))

    images = forms.ImageField(required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control-file'
        }))


    class Meta:
        model = Certificate
        fields = ('date', 'name', 'title', 'description', 'images')
        

class ExperienceForm(forms.ModelForm):
    date_from = forms.DateTimeField(required=True,
        widget=forms.DateTimeInput(attrs={
            'type': 'date',
         
        })
    )

    date_to = forms.DateTimeField(required=True,
        widget=forms.DateTimeInput(attrs={
            'type': 'date',
         
        })
    )

    name = forms.CharField(max_length=50, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*The place of work..',
            'class': 'form-control',
        })
    )
        
    title = forms.CharField(max_length=50, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Experience title..',
            'class': 'form-control'
        }))

    description = forms.CharField(max_length=1000, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Description..',
            'rows': 6,
        }))

    images = forms.ImageField(required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control-file'
        }))



    class Meta:
        model = Experience
        fields = ('date_from','date_to', 'name', 'title', 'description', 'images')

class MediaUrlForm(forms.ModelForm):
   
    media_url = forms.URLField(required=True,
    widget=forms.URLInput(attrs={
        'placeholder': 'Media url..',
        'class': 'form-control'
        }))

    class Meta:
        model = MediaUrl
        fields = ('name', 'media_url')

class AdminEditReportForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True, 
    widget= forms.TextInput(attrs={
        'class': 'form-control',
    }))

    intro_repo = forms.CharField(max_length=500, required=True, 
    widget= forms.TextInput(attrs={
        'class': 'form-control'
    }))

    key_word = forms.CharField(max_length=400, required=True, 
    widget= forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Report
        fields = ('title', 'intro_repo', 'key_word', 'repo_prograph', 'repo_prograph_users', 'edit_by', 'edit_date')

class FaqFormAdmin(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ('question', 'answer', 'answer_date')