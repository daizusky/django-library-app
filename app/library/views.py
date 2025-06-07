from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from .models import Publisher


class PublisherListView(ListView):
    model = Publisher
    template_name = "library/publisher_list.html"
    context_object_name = "publishers"
    paginate_by = 20


class PublisherCreateView(CreateView):
    model = Publisher
    fields = ["name", "address", "publisher_type"]
    template_name = "library/publisher_form.html"
    success_url = reverse_lazy("library:publisher_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "出版社を登録しました。")
        return response


class PublisherDetailView(DetailView):
    model = Publisher
    template_name = "library/publisher_detail.html"
    context_object_name = "publisher"
