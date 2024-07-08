from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
   path('', hello_world),
   path('user_data/', get_user, name='get_user'),
   path('update_user/<id>',update_user, name ='update_user'),
   path('delete_user/<id>', delete_user, name="delete_user")
]