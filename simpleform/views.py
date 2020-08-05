from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
import os
from . import contactform
from .contactform import createcontact
#from simpleform.models import contact

# Create your views here.

def PAnalysisview(request):
    return render(request, 'PassageAnalysis.html')

# def contactinput(request):
#     contactlist = contact.objects.all()
#     contactform1 = contactform()
#     context={'contactlist':contactlist,'contactform':contactform1}
#     return render(request, 'contactdetails.html',context)
#
# def contactvalidate(request):
#     if request.method == "POST"
#         form = contactform(request.POST)
#         if form.is_valid:
#             firstname = form.cleaned_data['firstname']
#             lastname = form.cleaned_data['lastname']
#     return render(request, 'index.html')

def create(response):
    form = createcontact()
    return render(response, 'create.html', {"form":form})

# def contactinputview(request):
#     context ={}
#     context['form']= contactform()
#     return render(request, "contactinputview.hmtl", context)

