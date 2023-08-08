from django.shortcuts import render
from django.http import HttpResponse


def ai_chat(request):
    return render(request, 'app/ai_chat.html')


def home_page(request):
    return render(request, 'app/home_page.html')


def ai_handle_input(request):
    print(request.body)
    return HttpResponse("Oliver was here", status=201)

