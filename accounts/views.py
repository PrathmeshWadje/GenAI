from django.shortcuts import render, redirect

# Create your views here.
def profile(request):
    if not request.user.is_authenticated:
        return redirect('account_login')

    return render(request, 'account/profile.html')
