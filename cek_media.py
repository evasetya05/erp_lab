import os
import django
import requests

# 🔹 Set environment Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HRManagement.settings')  # Ganti 'nama_project' dengan nama proyek Django Anda
django.setup()

from django.conf import settings

def check_local_file():
    """Cek apakah file gambar ada di folder media di server"""
    image_path = os.path.join(settings.MEDIA_ROOT, 'blog_images/blog1.PNG')

    if os.path.exists(image_path):
        print(f"✅ File ditemukan di path: {image_path}")
    else:
        print(f"❌ File tidak ditemukan di path: {image_path}")

def check_image_url():
    """Cek apakah URL gambar bisa diakses"""
    image_url = f"{settings.MEDIA_URL}blog_images/blog1.PNG"

    # Jika MEDIA_URL relatif, tambahkan domain server
    if not image_url.startswith("http"):
        image_url = f"https://www.sdmportabel.my.id/hris{image_url}"

    print(f"🔎 Mengecek URL gambar: {image_url}")

    try:
        response = requests.get(image_url, timeout=5)
        if response.status_code == 200:
            print(f"✅ File dapat diakses di URL: {image_url}")
        else:
            print(f"❌ File tidak ditemukan di URL: {image_url}, status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"⚠️ Error saat mengakses URL: {e}")

if __name__ == "__main__":
    check_local_file()
    check_image_url()
