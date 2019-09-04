from django.urls import path
from . import views

urlpatterns = [
    path('', views.pages, name='home'),
    path('<slug:slug>/', views.pages, name='page'),
    path('news/<slug:slug>/', views.news, name='news')
]
