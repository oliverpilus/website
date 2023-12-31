from django.shortcuts import render
from django.http import HttpResponse
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
import pickle


load_dotenv()

llm = ChatOpenAI()

conversation_map = {}

# Prompt
prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a nice chat bot having a conversation with a human."
        ),
        # The `variable_name` here is what must align with memory
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)

# Notice that we `return_messages=True` to fit into the MessagesPlaceholder
# Notice that `"chat_history"` aligns with the MessagesPlaceholder name
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
conversation = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=memory
)


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


def conversational_ai_handle_input(request):
    print(request.body)
    request.session["useConversation"] = True
    print(request.session.session_key)

    sessionConversation = None
    if 'user_conversation' in request.session:
        sessionConversation = request.session['user_conversation']
    else:
        sessionConversation = initUserConversation()
        # sessionConversation.save("llm_chain.json")
        # request.session['user_conversation'] =

    ai_output = sessionConversation({"question": request.body})
    print(ai_output)
    return HttpResponse(ai_output.get('text'), status=201)


def initUserConversation():
    prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(
                "You are a nice chat bot having a conversation with a human."
            ),
            # The `variable_name` here is what must align with memory
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{question}")
        ]
    )

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    return  LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
        memory=memory
    )

def conversational_ai_chat(request):
    return render(request, 'app/conversational_ai_chat.html')


def custom_chat_selection(request):
    return render(request, 'app/custom_chat_selection.html')


def nice_conversational_ai_chat(request):
    return render(request, 'app/nice_conversational_ai_chat.html')


def rude_conversational_ai_chat(request):
    return render(request, 'app/rude_conversational_ai_chat.html')
