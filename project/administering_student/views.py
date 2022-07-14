from django.shortcuts import render
from . forms import StudentForm
from . models import StudentData
from django.contrib import messages

# Create your views here.

# Function Based View for Adding Students in Database
def add_stu(request):
    if request.method == "POST":
        fm = StudentForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['student_name']
            dob = fm.cleaned_data['Date_of_Birth']
            mp = fm.cleaned_data['Marks_in_Physics']
            mc = fm.cleaned_data['Marks_in_Chemistry']
            mm = fm.cleaned_data['Marks_in_Math']
            pt = ((mc+mp+mm)/300)*100
            reg = StudentData(student_name = nm, Date_of_Birth = dob, Marks_in_Physics = mp, Marks_in_Chemistry = mc, Marks_in_Math = mm, percent=pt)
            reg.save()             
            fm= StudentForm()
            messages.success(request,'Student Data Added Successfully !!')
    else:
        fm = StudentForm()
    return render(request,'add_stu.html',{'form':fm})


# Function Based View for Retrieving the data of Students from Database to show in Tables.    
def show_stu(request):
    stud = StudentData.objects.all()
    return render(request,'show_stu_table.html',{'stu':stud})
    