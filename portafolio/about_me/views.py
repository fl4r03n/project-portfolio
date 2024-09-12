from django.shortcuts import render
from .models import AboutMe

# Create your views here.
def about(request):
    aboutme = AboutMe.objects.all()
    return render(request,'about-me/about-me.html',{'aboutme':aboutme})
