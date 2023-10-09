from django.shortcuts import render

def index(request):
    return render(request, "packages/server_main.html")
