from django import forms
from app.models import *

class Topic_Form(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'