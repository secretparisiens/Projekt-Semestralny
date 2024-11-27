from django.urls import path
from . import views
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', lambda request: redirect('log', permanent=False)),
    path('about', views.about, name='about'),
    path('todolist', views.todolist, name='todolist'),
    path('finance', views.finance, name='finance'),
    path('reg', views.reg, name='reg'),
    path('log', views.log, name='log'),
    path('acc', views.acc, name='acc'),
    path('home', views.home, name='home'),
    path('log', LoginView.as_view(template_name='log.html'), name='log'),
    ]
