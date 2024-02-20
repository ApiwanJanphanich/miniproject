from django.shortcuts import render ,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    person_qry = Person.objects.all()
    context = {'Person': person_qry}
    return render(request, 'base.html', context)

@login_required(login_url="/login") 
def list(request): #ชื่อฟังชั่น
    person_qry = Person.objects.all()
    context = {'person':person_qry}
    return render(request,'list.html',context) #ชื่อไฟล์ที่จะแสดง

def addemp(request): #ชื่อฟังชั่น
    if request.method == 'POST':
        f_name = request.POST['firstname']
        l_name = request.POST['lastname']

        address = request.POST['address']
        num = request.POST['number']
        pos = request.POST['position']
        job = request.POST['work']
        con = request.POST['contract']
        sal = request.POST['salary']

        pic = request.FILES['picture']
        person = Person(p_firstname=f_name, p_lastname=l_name, p_position=pos,  p_local=address, p_number=num, p_work=job, 
                  p_contract= con, p_salary=sal, p_picture=pic )
        person.save()
        return redirect('/list')
    return render(request,'addemp.html') #ชื่อไฟล์ที่จะแสดง
        


@login_required(login_url="/login")
def manage(request): #ชื่อฟังชั่น
    return render(request,'manage.html') #ชื่อไฟล์ที่จะแสดง

def custom_login(request): #ชื่อฟังชั่น
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pswd']
        user = authenticate(request, username=username, password=password)
        if user is not None: #ถ้าไม่เป็นค่าว่าง user password ถูก
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('/list')
        else:
            messages.error(request, 'Login failed. Please check your login.')
            pass
    return render(request,'login.html') #ชื่อไฟล์ที่จะแสดง

def logout_view(request):
    logout(request)
    return render(request,'login.html')