from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def profile(request):
    if not request.user.is_authenticated:
        return redirect('account_login')

    RESPONSE : str

    return render(request, 'account/profile.html')