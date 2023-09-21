from django.urls import path
from .views import HomePageView, AboutPageView, HelloPageView

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    path("hello/", HelloPageView.as_view(), name="hello"),
]
