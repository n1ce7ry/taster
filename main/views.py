from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import logout


def home(request):
    return render(request, 'main/main_page.html')


def about(request):
    return render(request, 'main/about.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('/login/')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'authorization/signup.html', {'user_form': user_form})


def user_logout(request):
    logout(request)
    return redirect('home__page')
