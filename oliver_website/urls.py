from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('ai_chat', views.ai_chat, name='ai_chat'),
    path('ai_handle_input',views.ai_handle_input, name="ai_handle_input")
]