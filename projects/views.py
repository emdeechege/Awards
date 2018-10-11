from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import *
# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    projects = Project.get_projects()
    reviews = Reviews.get_reviews()
    profile = Profile.get_profile()

    current_user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
        return redirect('home')

    else:
        form = ReviewForm()

    return render(request,"home.html",{"projects":projects, "reviews":reviews,"form": form,"profile":profile})
