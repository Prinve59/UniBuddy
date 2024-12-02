from django.forms import ModelForm
from django import forms
from .models import *

class ChatmessageCreateForm(ModelForm):
    class Meta:
        model=GroupMessage
        fields=['body']
        widgets={
            '':forms.TextInput(attrs={'placeholder':'Add message ...',
            'class':'p-4 text-black border border-gray-300 rounded-lg',
            'maxlength':'300',
            'autofocus':True})
        }