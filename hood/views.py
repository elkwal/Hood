from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Neighbourhood
from django.contrib.auth.decorators import login_required
# from .forms import *

# Create your views here.

@login_required(login_url='/accounts/login/') 
def index(request):
    
    # update= Post.objects.all()

    return render(request,'temps/index.html')
    