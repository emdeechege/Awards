from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import *
# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):

    message ='See me?'
    return render(request,"home.html",{"message":message})
