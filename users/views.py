from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserCreationForm


from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib import messages 



def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserCreationForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            messages.success(request, 'Thanks for registering {}, kindly login to proceed'.format(user.firstname), "alert alert-warning alert-dismissible")
            return redirect(reverse('users:login'))
        else:

            messages.error(request, user_form.errors, "alert alert-error alert-dismissible")
            return redirect(reverse('users:register'))
            messages.error(request, user_form.errors)

            print(user_form.errors)
    else:
        user_form = UserCreationForm()
    context={'user_form':user_form,
            'registered':registered,
            }
    return render(request,'registration.html',context)




def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request,user)
                # messages.warning(request, 'logged in  {}'.format(user.firstname), "alert alert-warning alert-dismissible")
                return HttpResponseRedirect(reverse('courses:course_list'))
            else:
                messages.error(request, 'This ccount is not Active  {}'.format(user.firstname), "alert alert-warning alert-dismissible")
                return HttpResponseRedirect(reverse('users:login'))
        else:
            print("Someone tried to login and failed.")
            print("They used email: {} and password: {}".format(email,password))
            messages.error(request, 'Invalid login details given', "alert alert-warning alert-dismissible")
            return HttpResponseRedirect(reverse('users:login'))
    else:
        return render(request, 'login.html', {})





def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!", "alert alert-warning alert-dismissible")
    return redirect("core:home")