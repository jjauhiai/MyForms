from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return render(request, 'hello.html', {})
def index(request):
    return render(request, 'index.html', {})
def Page1(request):
    return render(request, 'Page1.html', {})
