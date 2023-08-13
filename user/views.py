from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from user.models import Profile

# Create your views here.
def index(request):
    users = User.objects.all()
    profiles = Profile.objects.filter(id=1)
    
    return HttpResponse(users)