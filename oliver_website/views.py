from django.shortcuts import render
from django.http import HttpResponse
from dotenv import load_dotenv
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI

load_dotenv()


def ai_chat(request):
    return render(request, 'app/ai_chat.html')


def home_page(request):
    return render(request, 'app/home_page.html')


def ai_handle_input(request):
    print(request.body)

    chat = ChatOpenAI()
    ai_output = chat([HumanMessage(content=request.body)])
    print(ai_output)

    return HttpResponse(ai_output.content, status=201)
def conversational_ai_chat(request):
    return render(request, 'app/conversational_ai_chat.html')
