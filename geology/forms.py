from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Report, Author, Rock, Mineral, FAQ


class createUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*First name..',
            'class': 'form-control'
        }))

    last_name = forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Last name..',
            'class': 'form-control'
        }))

    email = forms.EmailField(max_length=254, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Email..',
            'class': 'form-control'
        }))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        exclude = ['user']


        

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = (
            'title', 'intro_repo', 'repo_prograph', 'repo_prograph_users', 'key_word')
        labels = {
            'title': 'Title',
            'repo_prograph': 'Write or copy your repo here'
        }


class AuthorForm(forms.ModelForm):
    title = forms.CharField(max_length=200, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Your gob title',
            'class': 'form-control'
        }))

    avatar = forms.ImageField(
        widget= forms.FileInput(attrs={
            'class': 'form-control'
        }))

    user_bio =forms.Textarea( 
        attrs={
            'placeholder': 'Write bio',
            'class': 'form-control'
        })

    cv = forms.FileField(max_length=200, required=True,
        widget=forms.FileInput(attrs={
            
            'class': 'form-control'
        }))



    class Meta:
        model = Author
        fields = '__all__'
        exclude = ['user']
        labels = {
            'title': 'Title',
            'degree': 'Education Degree',
            'avatar': 'Avatar',
            'user_bio': 'Bio',
            'cv': 'Upload your cv as pdf',
        }

class RockForm(forms.ModelForm):
    name = forms.CharField(max_length=200, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Rock name..',
            'class': 'form-control'
        }))
    rock_img = forms.ImageField(required=True,
        widget=forms.FileInput(attrs={
            'class': 'form-control-file'
        }))

    class Meta:
        model = Rock
        fields = ('rock_type', 'name', 'intro', 'rock_img', 'rock_details', 'key_word')
        labels = {
            'rock_type': 'Rock Type',
            'name': 'Name',
            'rock_img': 'Image',
            'rock_details': 'Details',
            'key_word': 'key words',
        }

class MineralForm(forms.ModelForm):
    name = forms.CharField(max_length=200, required=True, 
    widget=forms.TextInput(attrs={
        'class ' : 'form-control',
        'placeholder' : 'Mineral name ..'
        }))
    mineral_img = forms.ImageField(required=True,
        widget=forms.FileInput(attrs={
            'class': 'form-control-file'
        }))

    class Meta:
        model = Mineral
        fields = ('classes', 'name', 'intro', 'mineral_img', 'details', 'key_words')
            
class FaqForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ('question', )
        
      