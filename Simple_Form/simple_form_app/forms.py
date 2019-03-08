from django import forms
from captcha.fields import CaptchaField
class SimpleForm(forms.Form):
    name = forms.CharField(label='Name',max_length=20)
    department = forms.CharField(label='Department',max_length=50)


class CaptchaForm(SimpleForm):
    captcha = CaptchaField()
