
from django.urls import path, include
from post_media import views


app_name = 'post_media'

urlpatterns = [

    path('linkedin/', include('post_media.urls.linkedin')),

]

