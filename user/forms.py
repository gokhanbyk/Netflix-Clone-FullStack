from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.forms import widgets
from .models import *

class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Giriniz'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Giriniz'}))

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')

        if not CustomUser.objects.filter(email = email).exists():
            self.add_error('email', 'Bu email mevcut değil!')

        return email
    

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['image'].widget = widgets.FileInput(attrs={'class': 'form-control'})


class ChangePass(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})
        self.fields['new_password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})
        self.fields['new_password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'phone', 'birth_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['last_name'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['username'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'class': 'form-control'})
        self.fields['phone'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['birth_date'].widget = widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})
