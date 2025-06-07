from allauth.account.views import LoginView, SignupView
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.urls import reverse_lazy
from django.views.generic import TemplateView


class CustomSignupView(SignupView):
    template_name = "accounts/signup.html"


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/dashboard.html"
