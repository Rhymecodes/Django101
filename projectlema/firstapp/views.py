from django.shortcuts import render
from django.http import HttpResponse

"""
Views can be:
    - Functions that take a web request and return a web response
    - Class-based views
"""
# Create your views here.
# Function based view
def hello(request):
    return HttpResponse("Hello, world!")