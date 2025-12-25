import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        
        email = os.getenv('DJANGO_SUPERUSER_EMAIL')
        username = os.getenv('DJANGO_SUPERUSER_USERNAME')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

        # This DELETE is the most important part to clear old "bad" data
        User.objects.filter(email=email).delete()
        User.objects.filter(username=username).delete()

        # Create fresh
        admin_user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        self.stdout.write(self.style.SUCCESS(f'DELETED OLD AND CREATED NEW ADMIN: {email}'))