from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "database/home.html")

def query(request):
    return render(request, "database/query.html")

def about(request):
    return render(request, "database/about.html")

def contact(request):
    return render(request, "database/contact.html")