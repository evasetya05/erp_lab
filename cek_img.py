import requests

url = "https://www.sdmportabel.my.id/hris/static/images/hero1.png"
response = requests.get(url)

if response.status_code == 200:
    print("✅ Gambar bisa diakses!")
else:
    print(f"❌ Gambar masih error {response.status_code}")
