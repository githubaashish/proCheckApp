from django.shortcuts import render
from procheckapp import forms
from procheckapp.forms import UserForm

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse



# Create your views here.

def index(request):
    return render(request, 'procheckapp/index.html')

def register(request):
    registered = False

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        user_form = forms.UserForm(request.POST)
        data_form = forms.UserDetailsInfoForm(request.POST)

        if user_form.is_valid() and data_form.is_valid() :

            user = user_form.save()
            # user.set_password(user.password)
            user.save()

            data = data_form.save(commit=False)
            data.user = user
            data.save()
            registered = True

        else:
            print(user_form.errors,data_form.errors)
    else:
        user_form = forms.UserForm()
        data_form = forms.UserDetailsInfoForm()


    return render(request, 'procheckapp/users.html',{'user_form':user_form, 'data_form':data_form,'registered':registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return render(request, 'procheckapp/homepage.html')
            else:
                return HttpResponse("account is not active")
        else:
            return HttpResponse("invalid credentials , please verify and login again")


    else :
        return render(request, 'procheckapp/login.html', {})


@login_required
def user_logout(request):
    logout(request, user)
    
