from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
import uuid

# Create your views here.

def shortener(request):
    if request.method == 'POST':
        data = request.POST
        long_url = data.get('long_url')
        if UrlShortner.objects.filter(long_url=long_url):
            messages.info(request,"This URL is already Shortened . ")
            return redirect('/')
        else :
            short_url = uuid.uuid4()
            while not UrlShortner.objects.filter(short_url=short_url):
                short_url = uuid.uuid4()
            UrlShortner.objects.create(
                long_url =long_url,
                short_url="http://127.0.0.1:8000/"+short_url
            )
            messages.info(request,f"Your URL is Successfully Shortened to http://127.0.0.1:8000/{short_url}.")
            return redirect('/')

              
    return render(request,'index.html')