from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('css/main_style', views.main_style, name='main_style'),
    path('css/gallery_style', views.gallery_style, name='gallery_style'),
    path('images/simple_picture.png', views.simple_picture, name='simple_picture_small'),
]
