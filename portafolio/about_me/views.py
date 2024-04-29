from django.shortcuts import render
from .models import AboutMe, Knowledge

# Create your views here.
def about(request):
    aboutme = AboutMe.objects.all()
    knowledge = Knowledge.objects.all()
    return render(request,'about-me/about-me.html',{'aboutme':aboutme,'knowledge':knowledge})
