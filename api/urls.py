from django.urls import path
from .views import get_messages, add_message

urlpatterns = [
    path('messages/', get_messages),
    path('messages/add/', add_message),
]
