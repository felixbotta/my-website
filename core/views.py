from django.shortcuts import render, redirect

from .models import Skill

# Email Form
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def about(request):
    template_name = 'about.html'
    return render(request, template_name)


def skills(request):
    skills = Skill.objects.all()
    template_name = 'skills.html'
    context = {
        'skills': skills
    }
    return render(request, template_name, context)


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['felix.botta@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('core:success')
    return render(request, "contact.html", {'form': form})


def success(request):
    template_name = 'success.html'
    return render(request, template_name)



