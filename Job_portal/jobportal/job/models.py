from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class acc(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    type=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.user.first_name



class job_seeker(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=10)
    gender=models.CharField(max_length=20,null=True)
    experience=models.CharField(max_length=20,null=True)
    experience_cmp=models.CharField(max_length=20,null=True)
    type=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.user.first_name

class recruiter(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=10)
    company=models.CharField(max_length=50)
    type=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.user.username

class jobs(models.Model):
    recruiter1 = models.ForeignKey(recruiter,on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField()
    title=models.CharField(max_length=20)
    salary=models.FloatField(max_length=20)
    description=models.CharField(max_length=100)
    image=models.FileField()
    experience=models.CharField(max_length=100)
    location=models.CharField(max_length=20)
    skills=models.CharField(max_length=100)
    creation_date=models.DateField()

    def __str__(self):
        return self.title
    

class Apply(models.Model):
    job = models.ForeignKey(jobs,on_delete=models.CASCADE)
    student=models.ForeignKey(job_seeker,on_delete=models.CASCADE)
    resume=models.FileField(null=True)
    applied_date=models.DateField()
    def __str__(self):
        return self.student.user.first_name

class Rating(models.Model):
    recruiter1 = models.ForeignKey(recruiter,on_delete=models.CASCADE)
    student=models.ForeignKey(job_seeker,on_delete=models.CASCADE)
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

    def __str__(self):
        return self.student.user.first_name