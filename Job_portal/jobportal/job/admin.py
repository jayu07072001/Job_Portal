from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(job_seeker)
admin.site.register(recruiter)
admin.site.register(jobs)
admin.site.register(Apply)
admin.site.register(quiz)