from django.shortcuts import render
from django.http import HttpResponse


def ai_chat(request):
    return render(request, 'app/ai_chat.html')


def home_page(request):
    return render(request, 'app/home_page.html')