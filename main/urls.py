from django.urls import path, include
from . import views


# app_name='main'


urlpatterns = [
    path('<str:page>/', views.other_page, name='other'),
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('reviews', views.reviews_list, name='reviews'),
    path('contacts', views.contacts, name='contacts'),
    path('base', views.base_page, name='base'),
    path('feedback', views.feedback, name='feedback'),
    path('sale', views.sale, name='sale'),
    path('masters', views.masters, name='master'),
    path('masters_1', views.masters_1, name='masters_1'),
    path('masters_2', views.masters_2, name='masters_2'),
    path('examples', views.examples, name='examples'),

]
