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

def adminPage(request):
#    if request.session["user"] > 0:
#        currentUser = get_object_or_404(user, user_id = request.session["user"])
#        context = {
#            'currentUser': currentUser,
#        }
#        
#        addingUser = user(last_name = request.POST.get('last_name', False), first_name = request.POST.get('first_name', False), middle_initial =request.POST.get('middle_initial', False), email = request.POST.get('email', False), user_name = request.POST.get('user_name', False), password = request.POST.get('password1', False), role_type=request.POST.get('role_type.value', False))
#        addingUser.save()
#        return render(request, 'aionApp/adminpage.html', context)
#    else:
    return render(request, 'aionApp/adminpage.html')

def homeLogIn(request):
    userList = user.objects.all()
    error = False
    try:
        for userTry in userList:
            if userTry.user_name == str(request.POST['userName']):
                if userTry.password == str(request.POST['userPassword']):
                    request.session["user"] = userTry.user_id
                    choice= userTry.role_type
        if request.session["user"] >= 0:
            currentUser = get_object_or_404(user, user_id = request.session["user"])
            context = {
                'currentUser': currentUser,
            }
            
            if choice == "0":
                return shopPage(request)
            elif choice == "2":
                return adminPage(request)
            else:
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
                    choice= userTry.role_type
        if request.session["user"] >= 0:
            currentUser = get_object_or_404(user, user_id = request.session["user"])
            addedProducts = watche.objects.all()
            context = {
                'currentUser': currentUser,
                'addedProducts': addedProducts,
            }
            
            if choice == "2":
                return adminPage(request)
            else:
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
        addedProducts = watche.objects.all()
        context = {
            'currentUser': currentUser,
            'addedProducts': addedProducts,
        }
        return render(request, 'aionApp/shop.html', context)
    
    else:
        addedProducts = watche.objects.all()
        context = {
            'addedProducts': addedProducts,
        }
        return render(request, 'aionApp/shop.html', context)
    
def addProduct(request):
    currentUser = get_object_or_404(user, user_id=request.session["user"])
    addedProducts = watche.objects.all()
    context = {
        'currentUser': currentUser,
        'addedProducts': addedProducts
    }
    addingProduct = watche(name = request.POST['productName'], description = request.POST['productDescription'], stock = request.POST['productStock'], price = request.POST['productPrice'], watch_type = request.POST['watchType'], picture = "watchPictures/" + request.POST['productPicture'], user_id = request.session["user"])
    addingProduct.save()
    return render(request, 'aionApp/shop.html', context)
    
def addToCart(request):
    currentUser = get_object_or_404(user, user_id=request.session["user"])
    addedProducts = watche.objects.all()
    context = {
        'currentUser': currentUser,
        'addedProducts': addedProducts,
    }
    addingWatch = watche(quantity = request.POST['productQuantity'], user_id = request.session["user"])
    addingWatch.save()
    return render(request, 'aionApp/shop.html', context)
    
def signingUp(request):
    addingUser = user(last_name = request.POST['last_name'], first_name = request.POST['first_name'], middle_initial = request.POST['middle_initial'], email = request.POST['email'], user_name = request.POST['user_name'], password = request.POST['password1'])
    
    addingBAddress = billing_addres(house_number = request.POST['bHouseNum'], street = request.POST['bStreet'], subdivision = request.POST['bSubdivision'], city = request.POST['bCity'], postal_code = request.POST['bPostal'], country = request.POST['bCountry'])
    
    addingSAddress = shipping_addres(house_number = request.POST['sHouseNum'], street = request.POST['sStreet'], subdivision = request.POST['sSubdivision'], city = request.POST['sCity'], postal_code = request.POST['sPostal'], country = request.POST['sCountry'])
    
    addingUser.save()
    addingBAddress.save()
    addingSAddress.save()
    
    currentUser = get_object_or_404(user, user_id = request.session["user"])
    context = {
        'currentUser': currentUser,
    }
    return render(request, 'aionApp/home.html', context)
    
def addingAdmin(request):
    addingAdmin = user(last_name = request.POST['last_name'], first_name = request.POST['first_name'], middle_initial = request.POST['middle_initial'], email = request.POST['email'], role_type = request.POST['role_type'], user_name = request.POST['user_name'], password = request.POST['password1'])
    addingAdmin.save()
    return render(request, 'aionApp/adminpage.html')