from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user-list'),  # root URL of users app
]
