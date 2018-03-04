# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, 'aionApp/home.html')

def registerPage(request):
    return render(request, 'aionApp/register.html')