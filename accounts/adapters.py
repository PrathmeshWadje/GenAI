from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form=form)
        if form:
            if 'mobile_number' in form.cleaned_data:
                user.mobile_number = form.cleaned_data['mobile_number']
            user.save()
        return user