from django.db import models
# Create your models here.

    

class StudentData(models.Model):
    student_name = models.CharField(max_length=50)
    Date_of_Birth = models.DateField(max_length = 8)
    Marks_in_Physics= models.IntegerField()
    Marks_in_Chemistry=models.IntegerField()
    Marks_in_Math=models.IntegerField()
    percent = models.IntegerField()