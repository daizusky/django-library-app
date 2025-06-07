from django.urls import path

from .views import CustomLoginView, CustomSignupView, DashboardView

app_name = "accounts"

urlpatterns = [
    path("signup/", CustomSignupView.as_view(), name="account_signup"),
    path("login/", CustomLoginView.as_view(), name="account_login"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]
