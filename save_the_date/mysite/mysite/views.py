from django.shortcuts import render, redirect
# from .forms import SaveTheDateForm
from django.http import HttpResponse, Http404

from django.shortcuts import get_object_or_404, render

def default_view(request):
    return render(request, 'main.html')
