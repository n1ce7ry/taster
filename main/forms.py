from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={'class': 'auth__input', 'placeholder': 'Enter the name'}
        )
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'auth__input', 'placeholder':'Enter the password'}
        ) 
        self.fields['password'].label = False


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_repeat = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = forms.TextInput(
            attrs={'class': 'auth__input', 'placeholder': 'Enter the name'}
        )
        self.fields['username'].label = False

        self.fields['email'].widget = forms.TextInput(
            attrs={'class': 'auth__input', 'placeholder': 'Enter the email'}
        )
        self.fields['email'].label = False

        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'auth__input', 'placeholder':'Enter the password'}
        ) 
        self.fields['password'].label = False
    
        self.fields['password_repeat'].widget = forms.PasswordInput(
            attrs={'class': 'auth__input', 'placeholder':'Repeat the password'}
        ) 
        self.fields['password_repeat'].label = False
    
    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password_repeat(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_repeat']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password_repeat']