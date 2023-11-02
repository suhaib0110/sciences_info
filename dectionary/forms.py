#This Project with all app insite Created By: SUHAIB TAHA ALRIAH
#Email: alromys47@gmail.com

from django import forms
from .models import Dectionary

class DectionaryForm(forms.ModelForm):
    class Meta:
        model = Dectionary
        fields = ('en_word', 'ar_word', 'en_meaning', 'ar_meaning', 'key_words') #word, en_meaning, ar_maninig, key_word, pub_date
