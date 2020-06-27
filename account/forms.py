from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from account.models import Profile


STATUS_CHOICES = (
        ('', '--Pilih Status--'),
        (True, 'ADMIN'),
        (False, 'PEGAWAI')
    )


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=150,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(max_length=30,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=30,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))
    is_staff = forms.ChoiceField(label='Status', choices=STATUS_CHOICES)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_staff')


class SignUpFormUser(UserCreationForm):
    first_name = forms.CharField(max_length=30,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=150,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(max_length=30,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=30,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=30,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')
