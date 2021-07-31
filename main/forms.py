from django import forms
from django.forms import fields
from .models import Message 




class MessageForm(forms.ModelForm):

    class Meta:
        model=Message
        fields=[
            'name',
            'phone_number',
            'email',
            'subject',
        ]