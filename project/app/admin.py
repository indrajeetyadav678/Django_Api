from django.contrib import admin
from .models import StudentModel

# Register your models here.

# admin.site.register(StudentModel)

@admin.register(StudentModel)
class Loginadmin(admin.ModelAdmin):
    list_display=['id', 'Name','Userid']
