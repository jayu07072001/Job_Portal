from django.shortcuts import render

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
    return render(request,'job/signup_jobseeker.html')

def signup_recruiter(request):
    return render(request,'job/signup_recruiter.html')