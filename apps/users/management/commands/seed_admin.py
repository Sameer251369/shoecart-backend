from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Command(BaseCommand):
    help = 'Create a superuser for admin access'

    def handle(self, *args, **kwargs):
        # Get credentials from environment variables or use defaults
        email = os.environ.get('ADMIN_EMAIL', 'admin@example.com')
        password = os.environ.get('ADMIN_PASSWORD', 'Admin@123456')
        username = os.environ.get('ADMIN_USERNAME', 'admin')
        
        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(
                email=email,
                password=password,
                username=username
            )
            self.stdout.write(self.style.SUCCESS(f'✅ Superuser created successfully'))
            self.stdout.write(self.style.SUCCESS(f'   Email: {email}'))
            self.stdout.write(self.style.SUCCESS(f'   Username: {username}'))
        else:
            self.stdout.write(self.style.WARNING(f'⚠️  Superuser with email {email} already exists'))