from django.shortcuts import render
from .ComplainForm import ComplainForm
from .CommentForm import CommentForm
# Create your views here.

def complainForm(request):
    complain_form = ComplainForm()
    msg = ''

    if request.method == 'POST':
        complain_form = ComplainForm(request.POST)
        msg = 'Invalid input'

        if complain_form.is_valid():
            complain_form.save()
            msg = 'Insertion done!'
            complain_form = ComplainForm()

    context = {
        'complain_form': complain_form,
        'msg': msg
    }
    return render(request, 'Complain/ComplainForm.html', context)




def commentForm(request):
    comment_form = CommentForm()
    msg = ''

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        msg = 'Invalid input'

        if comment_form.is_valid():
            comment_form.save()
            msg = 'Insertion done!'
            comment_form = CommentForm()

    context = {
        'comment_form': comment_form,
        'msg': msg
    }
    return render(request, 'Complain/CommentForm.html', context)
