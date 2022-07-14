
from django import forms
from . models import StudentData

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentData
        fields = ['student_name','Date_of_Birth','Marks_in_Physics','Marks_in_Chemistry','Marks_in_Math']
        widgets = {
            'student_name':forms.TextInput(attrs = {'class':'form-control','placeholder':'eg. Ram'}),
            'Date_of_Birth':forms.DateInput(attrs = {'class':'form-control','placeholder':'eg.Y-M-D'}),
            'Marks_in_Physics':forms.NumberInput(attrs = {'class':'form-control','placeholder':'eg. 88'}),
            'Marks_in_Chemistry':forms.NumberInput(attrs = {'class':'form-control','placeholder':'eg. 88'}),
            'Marks_in_Math':forms.NumberInput(attrs = {'class':'form-control','placeholder':'eg. 88'}),
        }