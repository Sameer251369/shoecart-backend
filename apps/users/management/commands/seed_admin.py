from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        email = "admin@example.com"
        password = "Password123!"

        # 1. Clean up any existing admin to avoid conflicts
        User.objects.filter(email=email).delete()
        User.objects.filter(username="admin").delete()

        # 2. Create a fresh superuser
        # We use create_superuser and provide both username and email 
        # to satisfy whichever one your model uses as the 'USERNAME_FIELD'
        admin_user = User.objects.create_superuser(
            username="admin", 
            email=email, 
            password=password
        )
        
        # 3. Explicitly force permissions just in case
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()

        self.stdout.write(self.style.SUCCESS(f'SUCCESS: Admin created for {email}'))