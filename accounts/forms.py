from allauth.account.forms import SignupForm
from django import forms


class AccountSignUpForm(SignupForm):
    mobile_number = forms.CharField(max_length=20, label='Mobile Number')
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def clean(self):
        cleaned_data = super().clean()
        mobile_number = cleaned_data.get('mobile_number')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if not mobile_number or not first_name or not last_name:
            raise forms.ValidationError("All fields are required.")
        return cleaned_data

    def save(self, request):
        user = super().save(request)
        user.mobile_number = self.cleaned_data['mobile_number']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
    

from allauth.socialaccount.forms import SignupForm

class SocialAccountSignUpForm(SignupForm):
    mobile_number = forms.CharField(max_length=20, label='Mobile Number')

    def clean(self):
        cleaned_data = super().clean()
        mobile_number = cleaned_data.get('mobile_number')
        if not mobile_number:
            raise forms.ValidationError("All fields are required.")
        return cleaned_data

    def init_sociallogin(self, request, sociallogin):
        user = super().init_sociallogin(request, sociallogin)
        if hasattr(self, 'cleaned_data') and 'mobile_number' in self.cleaned_data:
            user.mobile_number = self.cleaned_data['mobile_number']
        user.save()
        return user

    def save(self, request):
        user = super().save(request)
        user.mobile_number = self.cleaned_data['mobile_number']
        user.save()
        return user
    
