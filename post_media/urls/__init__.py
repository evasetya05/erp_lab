from django.urls import path, include
from post_media.views.post_media_home import post_media_home_page  # ← ini langsung fungsi, BUKAN modul

app_name = 'post_media'

urlpatterns = [
    path('', post_media_home_page, name='post_media_home'),
]
