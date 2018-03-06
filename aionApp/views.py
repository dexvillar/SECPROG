# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import watche, review, user, billing_addres, shipping_addres, checkout, sale

# Create your views here.

def homePage(request):
    if request.session["user"] > 0:
        currentUser = get_object_or_404(user, user_id = request.session["user"])
        context = {
            'currentUser': currentUser,
        }
    return render(request, 'aionApp/home.html', context)

def registerPage(request):
    return render(request, 'aionApp/register.html')

def homeLogIn(request):
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
                return render(request, 'aionApp/home.html', {'error': error})
    except ValueError:
        error = True
        return render(request, 'aionApp/home.html', {'error': error})
    
def shopLogIn(request):
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
            return render(request, 'aionApp/shop.html', context)
        else:
                error = True
                request.session["user"] = -1
                return render(request, 'aionApp/shop.html', {'error': error})
    except ValueError:
        error = True
        return render(request, 'aionApp/shop.html', {'error': error})

def exitSession(request):
    request.session['user'] = -1
    return render(request, 'aionApp/home.html')

def shopPage(request):
    if request.session["user"] > 0:
        currentUser = get_object_or_404(user, user_id = request.session["user"])
        context = {
            'currentUser': currentUser,
        }
        return render(request, 'aionApp/shop.html', context)
    
    else:
        return render(request, 'aionApp/shop.html')
    
def addProduct(request):    
    addingProduct = watche(name = request.POST['productName'], description = request.POST['productDescription'], stock = request.POST['productStock'], price = request.POST['productPrice'], watch_type = request.POST['watchType'], picture = request.POST['productPicture'])
    addingProduct.save()
    return render(request, 'aionApp/shop.html')
    
    
    