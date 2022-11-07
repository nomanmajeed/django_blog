from django.contrib.auth import logout
from django.shortcuts import render, redirect

from home.models import Blog, Profile

def login_view(request):
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def home_page(request):
    context = {'blogs': Blog.objects.all()}
    return render(request, 'home.html', context)


def register_view(request):
    return render(request, 'register.html')


def verify(request, token):
    try:
        profile_obj = Profile.objects.filter(token=token).first()

        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e:
        print(e)

    return redirect('/')
