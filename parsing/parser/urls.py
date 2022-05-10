
from django.urls import path, include
from .views import HomePageView, UrlCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), 
    path('search/', UrlCreateView.as_view(), name='url_create'),
]

