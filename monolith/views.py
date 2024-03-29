from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def buttons(request):
    return render(request, 'buttons.html')

def cards(request):
    return render(request, 'cards.html')

def utilities_colors(request):
    return render(request, 'utilities-color.html')

def utilities_border(request):
    return render(request, 'utilities-border.html')

def utilities_animation(request):
    return render(request, 'utilities-animation.html')

def utilities_other(request):
    return render(request, 'utilities-other.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def forgot_password(request):
    return render(request, 'forgot-password.html')

def not_found(request):
    return render(request, '404.html')

def blank(request):
    return render(request, 'blank.html')

def charts(request):
    return render(request, 'charts.html')

def tables(request):
    return render(request, 'tables.html')