from django.db import models
from django.contrib.auth.models import User

class job_seeker(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.IntegerField(max_length=10)
    file=models.FileField()
    gender=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.user.username