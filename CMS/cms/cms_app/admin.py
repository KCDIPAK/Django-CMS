from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(HOD)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Subject)
