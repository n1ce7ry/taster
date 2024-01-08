from django.shortcuts import render


def home(request):
    return render(request, 'main/main_page.html')


def login(request):
    return render(request, 'authorization/login.html')


def sign_up(request):
    return render(request, 'authorization/signup.html')