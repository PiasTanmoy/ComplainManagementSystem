from django.shortcuts import render
from .infoForm import InfoForm
from .faqForm import FaqForm

def infoForm(request):
    info_from = InfoForm()
    message = ""
    if request.method == "POST":
        message = "Invalid Input"
        info_from = InfoForm(request.POST)
        if info_from.is_valid():
            info_from.save()
            message = "Information Added"
            info_from = InfoForm()

    context ={
        'message': message,
        'info_form': info_from
        }
    return render(request,'InfoNContact/infoForm.html', context)


def faqForm(request):
    faq_form = FaqForm()
    msg = ''

    if request.method == 'POST':
        faq_form = FaqForm(request.POST)
        msg = 'Invalid input'

        if faq_form.is_valid():
            faq_form.save()
            msg = 'Insertion done!'
            faq_form = FaqForm()

    context = {
        'faq_form': faq_form,
        'msg': msg
    }
    return render(request, 'InfoNContact/faqForm.html', context)
