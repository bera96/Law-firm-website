import captcha
from django import forms
from django.forms import fields
from .models import Message 
from captcha.fields import ReCaptchaField
from django.utils.translation import gettext as _
import re




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




    
    def clean_phone_number(self):
        data = self.cleaned_data["phone_number"]
        pattern =  re.compile("(0)?[5][0-9]{9}")
        if not pattern.search(data):
            raise forms.ValidationError(
            _("This phone number is not valid. Please supply a valid phone number."))
        return data



    def clean_name(self):
        data = self.cleaned_data["name"]
        pattern = re.compile("[a-zA-Z\s]+$")
        if not pattern.search(data):
            raise forms.ValidationError(
            _("This name is not valid. Please supply a valid name."))
        return data


    def clean_subject(self):
        data = self.cleaned_data["subject"]
        if len(data)<7:
            raise forms.ValidationError(
            _("Subject can not be shorter that."))
        return data
    
    
    