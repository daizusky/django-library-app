from django.contrib import admin

from .models import Publisher


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "created_at")
    search_fields = ("name",)
