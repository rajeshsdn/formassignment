from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
import os

# Create your views here.

def PAnalysisview(request):
    return render(request, 'PassageAnalysis.html')