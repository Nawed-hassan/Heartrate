from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)

    # Add unique related_name to prevent clashes
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",  # Prevents conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # Prevents conflict
        blank=True
    )

    def __str__(self):
        return self.username
