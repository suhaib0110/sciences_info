from django.db import models
from django.contrib.auth.models import User
from geology.models import Author
from django.core.validators import MaxValueValidator,  MinValueValidator
from django_ckeditor_5.fields import CKEditor5Field
from tinymce import models as tinymce_models
from django.conf import settings




class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=5, validators=[ MinValueValidator(5), MaxValueValidator(100)]  , blank=True, null=True)
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificates'

    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    images = models.ImageField(blank=True, null=True, upload_to='certificate/', default='/certificate/work-img.jpg')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class MediaUrl(models.Model):
    class Meta:
        verbose_name_plural = 'MediaUrls'
        verbose_name = 'MediaUrl'

    NAME = (
        ('Facebook', 'Facebook'),
        ('Twitter', 'Twitter'),
        ('Instagram', 'Instagram'),
        ('LinkedIn', 'LinkedIn'),
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, choices=NAME)
    media_url = models.URLField(verbose_name="Url")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    class Meta:
        verbose_name_plural = 'Experiences'
        verbose_name = 'Experience'

    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    date_from = models.DateTimeField(blank=True, null=True)
    date_to = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    images = models.ImageField(blank=True, null=True, upload_to='certificate/', default='/certificate/work-img.jpg')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ContactProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ['timestamp']
    
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(verbose_name="Title", max_length=100)
    message = tinymce_models.HTMLField(verbose_name="Message")
    replay = tinymce_models.HTMLField(verbose_name="Replay")
    is_active = models.BooleanField(default=True)
    is_sent = models.BooleanField(default=False)

    class Meta:
        get_latest_by = 'timestamp'

    def __str__(self):
        return f"{self.title}"


