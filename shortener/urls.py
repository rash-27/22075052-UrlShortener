from django.contrib import admin
from django.urls import path ,include
from . import views
urlpatterns = [
    path('',views.shortener,name='shortner'),
    path('api/all_urls/',views.display,name='display'),
    # path('<short_url>/',views.sender,name="redirector")

]
