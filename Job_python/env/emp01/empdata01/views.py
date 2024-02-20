from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,"home.html",)

def nav(request):
    return render(request,"nav.html",)

def about(requset):
    return render(requset,"about.html")

def contact(requset):
    return render(requset,"contact.html")