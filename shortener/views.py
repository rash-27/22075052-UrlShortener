from django.shortcuts import render,redirect
from django.contrib import messages
from .models import UrlShortner
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
            short_code = uuid.uuid4().hex[:10]
            while UrlShortner.objects.filter(short_code=short_code):
                print(short_code)
                short_code = uuid.uuid4().hex[:10]
            UrlShortner.objects.create(
                long_url =long_url,
                short_code=short_code
            )
            messages.info(request,"Your URL is Successfully Shortened.")
            return redirect('/')

              
    return render(request,'index.html')

def display(request):
    data = UrlShortner.objects.all()
    context ={ 'urls':data }
    return render(request,'display.html',context)



def delete_url(request,short_code):
    querySet = UrlShortner.objects.get(short_code = short_code)
    querySet.delete()
    return redirect('/api/all_urls')

def sender(request,short_code):
    querySet = UrlShortner.objects.get(short_code = short_code)
    return redirect(querySet.long_url)
