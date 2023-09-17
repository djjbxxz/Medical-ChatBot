from django.shortcuts import render, redirect
from django.http import JsonResponse
from .client import ChatBotClient
from .models import Question

def home(request):
    
    if request.method == 'POST':
        content = request.POST.get('user_message')
        print(f"question:{content}")

        text, generated_text = ChatBotClient().infer(content)
        response = generated_text
        Question.objects.create(content=content, response=response)
        return JsonResponse({"bot_response": response})

    # questions = Question.objects.all()
    return render(request, 'home.html')
