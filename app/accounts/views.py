from allauth.account.views import SignupView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class CustomSignupView(SignupView):
    template_name = "accounts/signup.html"

    def get_success_url(self):
        return reverse_lazy("account_login")


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/dashboard.html"
