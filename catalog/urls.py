from django.urls import path, include
from . import views

urlpatterns = [
    path('catalog_man', views.catalog_man, name='catalog_man'),
    path('catalog_woman', views.catalog_woman, name='catalog_woman'),
    path('price', views.price, name='price'),
]
