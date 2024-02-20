from django.shortcuts import render

# Create your views here.

def home(request):
    num = 555+5
    context = {'show': num}
    print(type(context))
    return render(request,"home.html",context)

def about(requset):
    return render(requset,"about.html")

def contact(requset):
    return render(requset,"contact.html")