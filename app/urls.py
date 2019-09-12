from django.urls import path, re_path
from . import views
from .templatetags.page_tags import slug_by_layout

urlpatterns = [
    path('', views.pages, name='home'),
    path(slug_by_layout('news')+'/<slug:slug>/', views.news, name='news'),
    re_path('^(?P<url>.*)$', views.pages, name='page'),
]
