from django.shortcuts import render
def index(request):  #this is a function
    return render(request, 'index.html')