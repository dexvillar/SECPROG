# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import watche, review, user, billing_addres, shipping_addres, checkout, role, sale

# Create your views here.

def homePage(request):
    context = {
        
    }
    return render(request, 'aionApp/home.html', context)

def registerPage(request):
    return render(request, 'aionApp/register.html')

def logIn(request):
    userList = user.objects.all()
    error = False
    try:
        for userTry in userList:
            if userTry.user_name == str(request.POST['userName']):
                if userTry.password == str(request.POST['userPassword']):
                    request.session["user"] = userTry.user_id
        if request.session["user"] >= 0:
            currentUser = get_object_or_404(user, user_id = request.session["user"])
            context = {
                'currentUser': currentUser,
            }
            return render(request, 'aionApp/home.html', context)
        else:
            error = True
            request.session["user"] = -1
            return render(request, 'aionApp/login.html', {'error': error})
    except ValueError:
        error = True
        return render(request, 'aionApp/login.html', {'error': error})
    
    