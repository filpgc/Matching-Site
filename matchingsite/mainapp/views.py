from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext, loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.core import serializers
from .forms import RegistrationForm

def index(request):
    return render(request, "mainapp/index.html")

def registrationForm(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistrationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistrationForm()

    return render(request, 'mainapp/register.html', {'form': form})