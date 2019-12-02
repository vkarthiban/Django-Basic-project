from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index.html',views.index,name='index'),
    path('about.html',views.about,name='about'),
    path('contact.html',views.contact,name='contact'),
    path('destinations.html',views.destinations,name='destination'),
    path('elemnts.html',views.elements,name='elemnts'),
    path('news.html',views.newses,name='news'),
    path('subscribe',views.subscribing,name='subscribe'),
    path('message',views.messaging,name='message'),
    path('search',views.search,name='search')
]
