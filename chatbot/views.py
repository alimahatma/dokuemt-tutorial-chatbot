from django.shortcuts import render

#!Function to get chatbot page
def chatbot(request):
    return render(request, 'chatbot.html')
