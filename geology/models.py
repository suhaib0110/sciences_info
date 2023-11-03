from django.db import models

from django_ckeditor_5.fields import CKEditor5Field
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.template.defaultfilters import slugify
from PIL import Image
#from crequest.middleware import CrequestMiddleware
#from rest_framework.request import Request


class Author(models.Model):
    class Meta:
        verbose_name_plural = 'Authors'
        verbose_name = 'Author'

    DEGREE = (
        ("Student", 'Student'),
        ('DA', "Diploma's degree"),
        ('BA', "Bachelor's degree"),
        ('MA', "Master's degree"),
        ('PHD', "Doctoral's degree"),
        ('AA', "Associate's degree"),
        ("Teaching Assistant", 'Teaching Assistant'),
        ("Assistant Lecturer", 'Assistant Lecturer'),
        ("Assistant Professor", 'Assistant Professor'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatar/',  default='avatar/icon.jpg')
    title = models.CharField(max_length=200, blank=True, null=True)
    degree = models.CharField(max_length=100, blank=True, null=True, choices=DEGREE)
    user_bio = models.TextField(blank=True, null=True, max_length=200)
    cv = models.FileField(blank=True, null=True, upload_to='cv', default='cv/geologysd.txt')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Report(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    title   =   models.CharField(max_length=200, unique=True, help_text="please write the title")
    intro_repo = models.TextField(blank=True, null=True)
    key_word = models.CharField(max_length=400)
    repo_prograph   =   CKEditor5Field('Text',blank=True, null=True, config_name='extends')
    repo_prograph_users   =   CKEditor5Field('Text',blank=True, null=True, config_name='default')
    pub_date    =   models.DateTimeField(default=timezone.now, blank=True)
    edit_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    edit_date    =   models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        get_latest_by = 'pub_date'
    

    def __str__(self):
        return self.title

class Rock(models.Model):
    class Meta:
        verbose_name_plural = 'Rocks'
        verbose_name = 'Rock'

    TYPE = (
        ('Igneous Rocks', 'Igneous Rocks'),
        ('Sedimentary Rocks', 'Sedimentary Rocks'),
        ('Metamorphic Rocks', 'Metamorphic Rocks'),
    )

    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    rock_type = models.CharField(max_length=100, choices=TYPE )
    name   =   models.CharField(max_length=200, unique=True, help_text="rock name..")
    intro = models.TextField(max_length=500)
    rock_img = models.ImageField(upload_to='Rocks/' )
    rock_details   =   CKEditor5Field(blank=True, null=True, config_name='extends')
    key_word = models.CharField(max_length=400)
    edit_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    pub_date    =   models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        get_latest_by = 'pub_date'

    def __str__(self):
        return self.name

class Mineral(models.Model):
    class Meta:
        verbose_name_plural = 'Minerals'
        verbose_name = 'Mineral'

    CLASSES = (
        ('Native Elements', 'Native Elements'),
        ('Sulfides', 'Sulfides'),
        ('Sulfates', 'Sulfates'),
        ('Halides', 'Halides'),
        ('Oxides', 'Oxides'),
        ('Carbinates', 'Carbinates'),
        ('Phosphates', 'Phosphates'),
        ('Silicates', 'Silicates'),
        ('Organic Minerals', 'Organic Minerals'),
        ('Other', 'Other'),
    )
    '''
    SILICATES = (
        ('Nesosilicates', 'Nesosilicates'),
        ('Sorosilicates', 'Sorosilicates'),
        ('Cyclosilicates', 'Cyclosilicates'),
        ('Inosilicates', 'Inosilicates'),
        ('Phyllosilicates', 'Phyllosilicates'),
        ('Tectosilicates', 'Tectosilicates'),
    )
    '''
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    classes = models.CharField(verbose_name='Classes', max_length=200, choices=CLASSES )
    name   =   models.CharField(max_length=200, unique=True, help_text="mineral name..")
    intro = models.TextField(max_length=500)
    mineral_img = models.ImageField(verbose_name='Picture', upload_to='Minerals/' )
    details   =   CKEditor5Field(verbose_name='Details', blank=True, null=True, config_name='extends')
    key_words = models.CharField(max_length=400)
    edit_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    pub_date    =   models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        get_latest_by = 'pub_date'

    def __str__(self):
        return self.name

class FAQ(models.Model):
    class  Meta:
        verbose_name_plural = 'FAQs'
        verbose_name = 'FAQ'

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    question = models.CharField(max_length=400, unique=True, help_text='Write your question')
    answer = CKEditor5Field(blank=True, null=True, config_name='extends')
    pub_date    =   models.DateTimeField(default=timezone.now, blank=True)
    answer_date    =   models.DateTimeField(default=timezone.now, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        get_latest_by = 'pub_date'

    def __str__(self):
        return self.question

