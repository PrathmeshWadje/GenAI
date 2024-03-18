from allauth.account.forms import SignupForm
from django import forms


class AccountSignUpForm(SignupForm):
    mobile_number = forms.CharField(max_length=20, label='Mobile Number')

    def clean(self):
        cleaned_data = super().clean()
        mobile_number = cleaned_data.get('mobile_number')
        if not mobile_number:
            raise forms.ValidationError("All fields are required.")
        return cleaned_data

    def save(self, request):
        user = super().save(request)
        user.mobile_number = self.cleaned_data['mobile_number']
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
    
