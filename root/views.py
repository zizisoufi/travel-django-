from django.shortcuts import render
from root.forms import NameForms, ContactForm, NewsletterForm
from django.http import HttpResponse, JsonResponse
from root.forms import Contact
from django.http.response import HttpResponseRedirect
from django.contrib import messages


def index(request):
    return render(request, "home/index.html")


def about(request):
    return render(request, "home/about.html")



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
        else:
             messages.add_message(request,messages.ERROR,'your ticket didnt submited')
                   
    form = ContactForm()
    return render(request, "home/contact.html",{'form':form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else :
        return HttpResponseRedirect('/')
            
    
