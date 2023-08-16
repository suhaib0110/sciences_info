from django.db import models
from tinymce import models as tinymce_models
import datetime
from django.utils import timezone

# Create your models here.
class Report(models.Model):
    title   =   models.CharField(max_length=200)
    repo_prograph   =   tinymce_models.HTMLField()
    repo_img    =   models.ImageField(upload_to = 'repo_img/')
    pub_date    =   models.DateTimeField('date published')

    def __str__(self):
        return self.title



