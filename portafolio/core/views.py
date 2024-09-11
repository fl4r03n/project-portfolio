from django.shortcuts import render, HttpResponse

# Create your views here.

from about_me.models import (PortfolioHeader)


def home(request):
    portfolio_header = PortfolioHeader.objects.last()
    return render(request,'core/home.html', {"portfolio_header": portfolio_header})

def contact(request):
    return render(request,'core/contact.html')