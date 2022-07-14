from django.contrib import admin

# Register your models here.
from . models import StudentData

@admin.register(StudentData)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','student_name','Date_of_Birth','Marks_in_Physics','Marks_in_Chemistry','Marks_in_Math','percent')