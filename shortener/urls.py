from django.contrib import admin
from django.urls import path ,include
from . import views
urlpatterns = [
    path('',views.shortener,name='shortner'),
    path('api/all_urls/',views.display,name='display'),
    path('api/delete_url/<short_code>',views.delete_url,name='delete'),
    path('<short_code>/',views.sender,name="redirector")

]
