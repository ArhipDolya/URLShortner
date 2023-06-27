from django.shortcuts import render, redirect
import uuid
from .models import URL
from django.http import HttpResponse


def main(request):
    return render(request, 'mainpage.html')

def save_in_db(request):
    if request.method == 'POST':
        url = request.POST['link']
        unique_id = str(uuid.uuid4())[:5]
        url_to_save = URL(url=url, unique_id=unique_id)
        url_to_save.save()

        return HttpResponse(unique_id)

def generate_webpage_link(request, link):
    url_webpage = URL.objects.get(unique_id=link)
    return redirect(url_webpage.url)