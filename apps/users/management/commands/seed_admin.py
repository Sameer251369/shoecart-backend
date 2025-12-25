from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        email = "admin@example.com"
        password = "Password123!" 

        # Delete any existing user with this email to ensure a fresh start
        User.objects.filter(email=email).delete()
        
        # Use create_superuser which handles both username/email based models
        User.objects.create_superuser(
            username="admin", # Some models still require a username field
            email=email, 
            password=password
        )
        
        self.stdout.write(self.style.SUCCESS(f'Admin created! Login with: {email}'))