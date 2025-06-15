import os
import django

# Set environment ke settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dev_env.settings")
django.setup()

from django.conf import settings

print("BASE_DIR:", settings.BASE_DIR)
print("STATIC_ROOT:", settings.STATIC_ROOT)
print("STATIC_URL:", settings.STATIC_URL)
print("INSTALLED_APPS:", settings.INSTALLED_APPS)
print("ROOT_URLCONF:", settings.ROOT_URLCONF)
print("WSGI_APPLICATION:", settings.WSGI_APPLICATION)


# jika hasilnya keluar untuk static root, file collectstatic diarahkan kesana

