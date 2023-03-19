from pyexpat.errors import messages
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from .forms import UserRegistration
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.


def user_registeration(request):
    if request.method=="POST":
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            messages.success(request, "Congratulation !! Your account has been created successfully !!! Login now")
            fm.save()
            return HttpResponseRedirect('signin')
    else:
        fm = UserRegistration()
    context = {
        'form' : fm
    }
    return render(request, 'flipcart_authentication/signup.html', context)



def user_signin(request):
    if request.method=="POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data.get('username')
            upass = fm.cleaned_data.get('password')
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, "Welcome you logged in successfully !!")
                return HttpResponseRedirect('/account/profile')
                
    else:
        fm = AuthenticationForm()

    context = {
        'form': fm
    }

    return render(request, 'flipcart_authentication/login.html', context)


def user_profile(request):
    return render(request, 'flipcart_authentication/profile.html')


def user_logout(request):
    logout(request)
    messages.success(request, "You logged out successfully")
    return HttpResponseRedirect('signin')


def change_password(request):
    return render(request, 'flipcart_authentication/changepass.html')