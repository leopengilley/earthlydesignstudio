from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('classes', views.classes, name='classes'),
    path('about_me', views.about_me, name='about_me'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
]
