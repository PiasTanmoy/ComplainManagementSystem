from django.shortcuts import render
from .models import Student
from .studentForm import StudentForm
from Complain.models import Complain,Comment
from InfoNContact.models import Info,FAQ
# Create your views here.


def showTables(request):

    studentTable = Student.objects.all()
    complainTable = Complain.objects.all()
    commentTable = Comment.objects.all()
    infoTable = Info.objects.all()
    faqTable = FAQ.objects.all()

    context = {
        'studentTable': studentTable,
        'complainTable': complainTable,
        'commentTable': commentTable,
        'infoTable':infoTable,
        'faqTable' :faqTable
    }

    return render(request, 'showTables.html', context)


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