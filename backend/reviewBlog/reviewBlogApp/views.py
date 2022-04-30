from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Post

# Create your views here.
def index(request):
  return HttpResponse("Hello Elliot")

def posts(request):
  return HttpResponse("posts api")

def posts_create(request):
  pass
