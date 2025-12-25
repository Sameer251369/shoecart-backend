from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        # Use a simple username for the first login
        username = "admin" 
        password = "Password123!" 
        email = "admin@example.com"

        # This will delete any old 'admin' and create a fresh one
        User.objects.filter(username=username).delete()
        User.objects.create_superuser(username=username, email=email, password=password)
        
        self.stdout.write(self.style.SUCCESS(f'Fresh admin created. User: {username} Pwd: {password}'))