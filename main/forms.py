import captcha
from django import forms
from django.forms import fields
from .models import Message 
from captcha.fields import ReCaptchaField




class MessageForm(forms.ModelForm):

    #captcha = ReCaptchaField()

    class Meta:
        model=Message
        fields=[
            'name',
            'phone_number',
            'email',
            'subject',
        ]