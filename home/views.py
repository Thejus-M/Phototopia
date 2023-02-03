from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = "home/home.html"
    extra_content={"RandomNumber":"8"}


class LoginView(LoginRequiredMixin ,TemplateView):
    template_name = "home/login.html"
    login_url='/admin'

