from django.shortcuts import render
from .models import Student
from .studentForm import StudentForm
# Create your views here.


def showTables(request):

    studentTable = Student.objects.all()

    context = {
        'studentTable':studentTable
    }

    return render(request,'showTables.html',context)


def studentForm(request):
    student_from = StudentForm()
    message =""
    if request.method == "POST":
        message = "Invalid Input"
        student_from = StudentForm(request.POST)
        if student_from.is_valid():
            student_from.save()
            message = "Student Added"
            student_from = StudentForm()

    context ={
        'message':message,
        'student_form':student_from
        }
    return render(request,'Studnet/studentForm.html',context)