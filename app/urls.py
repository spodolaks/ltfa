from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('tournaments/', views.tournaments, name='tournaments'),
    path('events/', views.events, name='events'),
    path('documents/', views.documents, name='documents'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('eshop/', views.eshop, name='eshop'),
]
