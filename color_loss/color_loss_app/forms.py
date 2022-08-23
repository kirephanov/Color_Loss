from .models import Clan
from django import forms
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=10, widget=forms.TextInput(attrs={'class': 'authorization__form-input'}))
    password = forms.CharField(label='Password', max_length=128, widget=forms.PasswordInput(attrs={'class': 'authorization__form-input'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=10, widget=forms.TextInput(attrs={'class': 'authorization__form-input'}))
    password1 = forms.CharField(label='Password', max_length=128, widget=forms.PasswordInput(attrs={'class': 'authorization__form-input'}))
    password2 = forms.CharField(label='Confirm password', max_length=128, widget=forms.PasswordInput(attrs={'class': 'authorization__form-input'}))
    email = forms.EmailField(label='Email', max_length=320, widget=forms.EmailInput(attrs={'class': 'authorization__form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ClanForm(ModelForm):
    class Meta:
        model = Clan
        fields = ['clan_name', 'clan_description', 'clan_is_open']

        widgets = {
            'clan_name': TextInput(attrs={
                'class': 'form-input',
                'id': 'clan_name'
            }),
            'clan_description': Textarea(attrs={
                'class': 'form-textarea',
                'id': 'clan_description'
            }),
            'clan_is_open': CheckboxInput(attrs={
                'class': 'form-checkbox',
                'id': 'clan_is_open'
            }),
        }