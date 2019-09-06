from django.urls import path
from . import views
from .templatetags.page_tags import slug_by_layout

urlpatterns = [
    path('', views.pages, name='home'),
    path('<slug:slug>/', views.pages, name='page'),
    path(slug_by_layout('news')+'/<slug:slug>/', views.news, name='news')
]
