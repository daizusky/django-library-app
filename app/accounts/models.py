from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """表示用のユーザーネームを保持（ログインには使わない）"""

    policy = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = "custom_user"
