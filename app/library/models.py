from django.db import models


class Publisher(models.Model):
    class PublisherType(models.TextChoices):
        GENERAL = "general", "総合出版社"
        ACADEMIC = "academic", "学術専門出版社"
        MANGA = "manga", "漫画出版社"
        NEWS = "news", "新聞社系"
        OTHER = "other", "その他"

    name = models.CharField(max_length=100, unique=True)
    publisher_type = models.CharField(
        max_length=20,
        choices=PublisherType.choices,
        default=PublisherType.GENERAL,
    )
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
