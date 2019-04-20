from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    m=2*2
    return HttpResponse('<h1>View Home</h1>')

def about(request):
    return HttpResponse('<h1>View about</h1>')