from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Set email as unique and the primary login field
    email = models.EmailField(unique=True)
    
    # Make username optional to avoid unique constraint errors during quick registration
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"] # Still required for createsuperuser

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        # Auto-generate username from email if not provided
        if not self.username:
            self.username = self.email.split('@')[0]
        super().save(*args, **kwargs)