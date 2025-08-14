# import form class from django
from django import forms
 
# import GeeksModel from models.py
from .models import File
 
# create a ModelForm
class Image(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = File
        fields = ["filename", 'image']



