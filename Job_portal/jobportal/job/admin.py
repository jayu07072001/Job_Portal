from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
class AccountInLine(admin.StackedInline):
    model=acc
    can_delete=False
    verbose_name_plural= 'accs'


class customizeduseradmin(UserAdmin):
    inlines=(AccountInLine, )

admin.site.unregister(User)
admin.site.register(User,customizeduseradmin)
admin.site.register(job_seeker)
admin.site.register(recruiter)
admin.site.register(jobs)
admin.site.register(Apply)
admin.site.register(acc)
admin.site.register(quiz)