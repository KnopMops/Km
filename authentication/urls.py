from django.urls import path
from .views import *

urlpatterns = [
    path('register/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout_from_account, name='logout')
]