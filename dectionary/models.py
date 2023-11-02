#This Project with all app insite Created By: SUHAIB TAHA ALRIAH
#Email: alromys47@gmail.com

from django.db import models
from django.contrib.auth.models import User
from geology.models import Author
from django.utils import timezone
import datetime


###START Geo Dectinary Model###
'''
Geo dectionary model used to create a dectionary for 
syntix and definetion of geology science, and define it with two lang ('Ar, En).
'''
class Dectionary(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    en_word = models.CharField(max_length=200, blank=True, null=True, unique=True)
    ar_word = models.CharField(max_length=200, blank=True, null=True, unique=True)
    en_meaning = models.TextField()
    ar_meaning = models.TextField()
    key_words = models.CharField(max_length=400)
    edit_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.en_word

###END Geo Dectinary Model###