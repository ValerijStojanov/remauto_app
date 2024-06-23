from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'phone_number', 'email', 'telegram', 'whatsapp', 'viber', 'instagram', 'facebook', 'tiktok']


class LoginForm(forms.Form):
    phone_number = forms.CharField(label='Номер телефона', max_length=100)
    auth_code = forms.CharField(label='Код аутентификации', max_length=6)