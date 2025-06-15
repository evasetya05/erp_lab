from django.shortcuts import render

def post_media_home_page(request):
    return render(request, 'media_home.html')
