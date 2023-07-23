from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('ai_chat', views.ai_chat, name='ai_chat')
]