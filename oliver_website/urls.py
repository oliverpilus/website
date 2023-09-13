from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('ai_chat', views.ai_chat, name='ai_chat'),
    path('ai_handle_input',views.ai_handle_input, name="ai_handle_input"),
    path('conversational_ai_handle_input',views.conversational_ai_handle_input, name="ai_handle_input"),
    path('conversational_ai_chat',views.conversational_ai_chat, name="conversational_ai_chat"),
    path('custom_chat_selection', views.custom_chat_selection, name="custom_chat_selection"),
    path('nice_conversational_ai_chat',views.nice_conversational_ai_chat, name="nice_conversational_ai_chat"),
    path('rude_conversational_ai_chat',views.rude_conversational_ai_chat, name="rude_conversational_ai_chat")
]