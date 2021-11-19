from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate,login,logout
from datetime import date

def home(request):
    return render(request, 'job/home.html')

def contact(request):
    return render(request,'job/contact.html')
    
def about(request):
    return render(request,'job/about.html')

def user_about(request):
    return render(request,'job/user_about.html')

def user_contact(request):
    return render(request,'job/user_contact.html')

def recruiter_about(request):
    return render(request,'job/recruiter_about.html')

def recruiter_contact(request):
    return render(request,'job/recruiter_contact.html')

def user_login(request):
    error=""
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pwd3']
        user=authenticate(username=u,password=p)
        if user:
            try:
                user1 = job_seeker.objects.get(user=user)
                if user1.type == "jobseeker":
                    login(request,user)
                    error="no"
                else:
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"
        
    d={'error':error}



    return render(request,'job/user_login.html',d)


def signup_jobseeker(request):
    error=""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        con=request.POST['cont']
        p=request.POST['pwd1']
        gen=request.POST['gender']
        type="jobseeker"
        try:
           user= User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
           job_seeker.objects.create(user=user,mobile=con,gender=gen,type=type)
           error="no"
        except:
            error="yes"
        
    d={'error':error}
    
    return render(request,'job/signup_jobseeker.html',d)

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')

    return render(request,'job/user_home.html')

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')

    return render(request,'job/recruiter_home.html')



def Logout(request):
    logout(request)
    return redirect('home')


def signup_recruiter(request):
    error=""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        c=request.POST['company']
        con=request.POST['cont']
        p=request.POST['pwd1']
        try:
           user= User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
           recruiter.objects.create(user=user,mobile=con,type="recruiter",company=c)
           error="no"
        except:
            error="yes"
        
    d={'error':error}
    return render(request,'job/signup_recruiter.html',d)

def recruiter_login(request):
    error=""
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        if user:
            try:
                user1 = recruiter.objects.get(user=user)
                if user1.type == "recruiter":
                    login(request,user)
                    error="no"
            except:
                error="yes"
        else:
            error="yes"
        
    d={'error':error}
    return render(request,'job/recruiter_login.html',d)


def add_job(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    
    error=""
    if request.method=='POST':
        j=request.POST['jobtitle']
        sd=request.POST['start_date']
        ed=request.POST['end_date']
        s=request.POST['salery']
        loc=request.POST['location']
        lg=request.FILES['logo']
        exp=request.POST['experience']
        sk=request.POST['skills']
        des=request.POST['description']
        user= request.user
        recruiter2=recruiter.objects.get(user=user)
        try:
           jobs.objects.create(recruiter1=recruiter2,start_date=sd,end_date=ed,title=j,salary=s,description=des,image=lg,experience=exp,location=loc,skills=sk,creation_date=date.today())
           error="no"
        except:
            error="yes"
        
    d={'error':error}



    return render(request,'job/add_job.html',d)

def job_list(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')

    user=request.user
    recruiter2=recruiter.objects.get(user=user)
    job=jobs.objects.filter(recruiter1=recruiter2)
    d={'job':job}
    return render(request,'job/job_list.html',d)


def edit_jobdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    
    error=""
    job=jobs.objects.get(id=pid)
    if request.method=='POST':
        j=request.POST['jobtitle']
        sd=request.POST['start_date']
        ed=request.POST['end_date']
        s=request.POST['salery']
        loc=request.POST['location']
        exp=request.POST['experience']
        sk=request.POST['skills']
        des=request.POST['description']        
        job.title=j
        job.salary=s
        job.location=loc
        job.experience=exp
        job.skills=sk
        job.description=des
        try:
            job.save()
            error="no"
        except:
            error="yes"
        
        if sd:
            try:
                job.start_date =sd
                job.save()
            except:
                pass
        else:
            pass

        if ed:
            try:
                job.end_date =sd
                job.save()
            except:
                pass
        else:
            pass

    d={'error':error,'job':job}
    return render(request,'job/edit_jobdetail.html',d)