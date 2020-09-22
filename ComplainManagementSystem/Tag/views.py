from django.shortcuts import render
from .tagForms import TagForm
from .complainTagForms import ComplainTagForm

# Create your views here.

def insertTag(request):
    tag_form = TagForm()
    message = ""

    if request.method == "POST":
        message = "Invalid Input!"
        tag_form = TagForm(request.POST)
        if tag_form.is_valid():
            tag_form.save()
            message = "Successfully added!"
            tag_form = TagForm()

    context={
        'tag_form': tag_form,
        'message': message
    }
    return render(request, 'Tag/tagForm.html', context)

def insertComplainTag(request):
    complainTag_form = ComplainTagForm()
    message = ""

    if request.method == "POST":
        message = "Invalid input. Please try again!"
        complainTag_form = ComplainTagForm(request.POST)
        if complainTag_form.is_valid():
            complainTag_form.save()
            message = "Successfully added!"
            complainTag_form = ComplainTagForm()

    context ={
        'complainTagForm' : ComplainTagForm,
        'message': message
    }
    return render(request, 'Tag/complainTagForm.html', context)
