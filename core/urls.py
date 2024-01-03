from django.urls import path
from .views import *

urlpatterns = [
    path('welcome/', front_page, name="home"),
    path('about/', about_us, name="about")
]