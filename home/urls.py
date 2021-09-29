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
    path('images/simple_picture_<int:width>x<int:height>.png', views.simple_picture, name='simple_picture'),
    path('images/lorenz_pict_<int:width>x<int:height>.png', views.lorenz_pict, name='lorenz_pict'),
    path('images/customers_<int:width>x<int:height>.png', views.customers, name='customers'),
]
