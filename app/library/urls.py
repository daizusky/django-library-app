from django.urls import path

from .views import PublisherCreateView, PublisherDetailView, PublisherListView

app_name = "library"

urlpatterns = [
    path("publishers/", PublisherListView.as_view(), name="publisher_list"),
    path("publishers/new/", PublisherCreateView.as_view(), name="publisher_create"),
    path(
        "publishers/<int:pk>/", PublisherDetailView.as_view(), name="publisher_detail"
    ),
]
