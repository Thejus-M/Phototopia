from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = "home/home.html"
    extra_content={"RandomNumber":"8"}


class LoginInterfaceView(LoginView):
    template_name = "home/login.html"

