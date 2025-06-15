import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dev_env.settings')  # Use your actual project name
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Superuser credentials
USERNAME = "admin"
EMAIL = "eva.setyabudi1986@gmail.com"
PASSWORD = "@Pontianak123"

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(username=USERNAME, email=EMAIL, password=PASSWORD)
    print("Superuser created successfully.")
else:
    print("Superuser already exists.")
