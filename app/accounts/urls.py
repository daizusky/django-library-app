from django.urls import path

from .views import CustomSignupView, DashboardView

app_name = "accounts"

urlpatterns = [
    path("signup/", CustomSignupView.as_view(), name="signup"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]
