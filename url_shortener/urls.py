from django.urls import path
from url_shortener.views import HomeView, redirect_view


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("<slug:slug>/", redirect_view, name="home"),
]
