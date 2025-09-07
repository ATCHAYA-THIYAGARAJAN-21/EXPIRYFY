from django.shortcuts import render

def home(request):
    return render(request, 'efy/index.html')


def dashboard(request):
    return render(request, 'efy/home.html')

