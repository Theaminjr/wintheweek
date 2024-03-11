from django.contrib import admin
from taskmanager import Task,RepeatinTask
# Register your models here.

admin.site.register(Task)
admin.site.register(RepeatingTask)

