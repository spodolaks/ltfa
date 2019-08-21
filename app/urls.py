from django.urls import path
from . import views

urlpatterns = [
    path('', views.pages, name='home'),
    path('<slug:slug>/', views.pages, name='page')
]
