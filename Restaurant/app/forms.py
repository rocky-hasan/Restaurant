from django import forms
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm, PasswordChangeForm, \
    PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from app.models import ContactModel, Customer, Booking


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'icon': 'fas fa-eye-slash'}))
    password2 = forms.CharField(label='Confirm Password (Again)',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'icon': 'fas fa-eye-slash'}))
    email = forms.CharField(required=True,
                            widget=forms.EmailInput(attrs={'class': 'form-control', 'icon': 'fas fa-envelope'}), )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'username': 'Name', 'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'icon': 'fas fa-user'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'icon': 'fas fa-user'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'icon': 'fas fa-user'}),
        }


class UserLogin(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'icon': 'fas fa-user'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput(
                                   attrs={'autocomplete': 'current-password', 'class': 'form-control',
                                          'icon': 'fas fa-eye-slash'}))


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['username', 'email', 'subject', 'desc']
        labels = {
            'username': 'Name',
            'email': 'Email',
            'subject': 'Subject',
            'desc': 'How can i help',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'icon': 'fas fa-user'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'icon': 'fas fa-envelope'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'icon': 'fas fa-book'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'icon': 'fas fa-comment'}),
        }


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True, 'class': 'form-control',
                   'icon': 'fas fa-eye-slash'}
        ),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True, 'class': 'form-control',
                   'icon': 'fas fa-eye-slash'}
        ),
    )
    new_password2 = forms.CharField(
        label=_("New password(Again)"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True, 'class': 'form-control',
                   'icon': 'fas fa-eye-slash'}
        ),
    )


class MyPasswordResetForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", 'class': 'form-control', 'icon': 'fas fa-eye-slash'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", 'class': 'form-control', 'icon': 'fas fa-eye-slash'}),
    )


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'city', 'house_no', 'state', 'zipcode']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'city': 'City',
            'house_no': 'House No',
            'state': 'State',
            'zipcode': 'Zipcode',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'house_no': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'})
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone_no', 'date', 'time', 'people', 'msg']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone_no': 'Mobile Number',
            'date': 'Date',
            'time': 'Time',
            'people': 'People',
            'msg': 'Message'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'col': 'md-6', 'form': 'group'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'col': 'md-6', 'form': 'group'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'class': 'form-control'}),
            'people': forms.NumberInput(attrs={'class': 'form-control'}),
            'msg': forms.Textarea(attrs={'class': 'form-control'})
        }
