from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Post

# Create your views here.
def index(request):
  print(Post)
  return HttpResponse("Hello Elliot")

def posts(request):
  if request.method == "POST":
    return HttpResponse("posts api create")
  return HttpResponse("posts api")
