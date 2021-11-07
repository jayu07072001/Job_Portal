from django.contrib.auth.models import User
from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'job/home.html')

def contact(request):
    return render(request,'job/contact.html')
    
def about(request):
    return render(request,'job/about.html')

def user_login(request):
    return render(request,'job/user_login.html')

def recruiter_login(request):
    return render(request,'job/recruiter_login.html')

def signup_jobseeker(request):
    error=""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        con=request.POST['cont']
        p=request.POST['pwd1']
        gen=request.POST['gender']
        try:
           user= User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
           job_seeker.objects.create(user=user,mobile=con,gender=gen)
           error="no"
        except:
            error="yes"
        
    d={'error':error}
    
    return render(request,'job/signup_jobseeker.html',d)

def signup_recruiter(request):
    return render(request,'job/signup_recruiter.html')