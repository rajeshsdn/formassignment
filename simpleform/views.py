from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
import os
from . import contactform
from simpleform.models import contact

# Create your views here.

def PAnalysisview(request):
    return render(request, 'PassageAnalysis.html')

def contactview(request):
    contactlist = contact.objects.all()
    contactform1 = contactform()
    context={'contactlist':contactlist,'contactform':contactform1}
    return render(request, 'contactdetails.html',context)