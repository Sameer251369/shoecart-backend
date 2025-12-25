import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        
        # This pulls the EXACT values you typed into the Render dashboard
        username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'Password123!')

        # Delete any existing conflicts
        User.objects.filter(email=email).delete()
        User.objects.filter(username=username).delete()

        # Create the superuser using your Render settings
        admin_user = User.objects.create_superuser(
            username=username, 
            email=email, 
            password=password
        )
        
        self.stdout.write(self.style.SUCCESS(f'SUCCESS: Admin created using Render Environment Variables!'))