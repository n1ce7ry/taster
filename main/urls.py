from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import LoginForm
from . import views


urlpatterns = [
    path('', views.home, name='home__page'),
    path('about/', views.about, name='about'),
    path(
        'login/', auth_views.LoginView.as_view(
            template_name='authorization/login.html',
            authentication_form=LoginForm,
        ),
        name='login'),   
    path('signup/', views.register, name='sign_up'),
]
