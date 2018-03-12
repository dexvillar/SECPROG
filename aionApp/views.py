# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import user, watche, review, billing_addres, shipping_addres, checkout, sale, buy_watche

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
    return render(request, 'aionApp/adminpage.html')

def profilePage(request):
    if request.session["user"] > 0:
        currentUser = get_object_or_404(user, user_id = request.session["user"])
    context = {
            'currentUser': currentUser,
        }
    return render(request, 'aionApp/profile.html', context)

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
    addingProduct = watche(name = request.POST['productName'], description = request.POST['productDescription'], stock = request.POST['productStock'], price = request.POST['productPrice'], watch_type = request.POST['watchType'], picture = "watchPictures/" + request.POST['productPicture'], watch_id = request.session["user"], user_id = request.session["user"])
    addingProduct.save()
    return render(request, 'aionApp/shop.html', context)
    
def signingUp(request):
    
    
    addingBAddress = billing_addres(house_number = request.POST['bHouseNum'], street = request.POST['bStreet'], subdivision = request.POST['bSubdivision'], city = request.POST['bCity'], postal_code = request.POST['bPostal'], country = request.POST['bCountry'])
    
    addingSAddress = shipping_addres(house_number = request.POST['sHouseNum'], street = request.POST['sStreet'], subdivision = request.POST['sSubdivision'], city = request.POST['sCity'], postal_code = request.POST['sPostal'], country = request.POST['sCountry'])
    
    addingBAddress.save()
    addingSAddress.save()
    
    addingUser = user(last_name = request.POST['last_name'], first_name = request.POST['first_name'], middle_initial = request.POST['middle_initial'], email = request.POST['email'], user_name = request.POST['user_name'], password = request.POST['password1'], billing_add=addingBAddress, shipping_add=addingSAddress )
    addingUser.save()
    
    currentUser = get_object_or_404(user, user_id = request.session["user"])
    context = {
        'currentUser': currentUser,
    }
    return render(request, 'aionApp/home.html', context)
    
def addAdmin(request):
    
    addingBAddress = billing_addres.objects.first()
    
    addingSAddress = shipping_addres.objects.first()
        
    addingAdmin = user(last_name = request.POST['last_name'], first_name = request.POST['first_name'], middle_initial = request.POST['middle_initial'], email = request.POST['email'], role_type = request.POST['role_type'], user_name = request.POST['user_name'], password = request.POST['password1'], billing_add=addingBAddress, shipping_add=addingSAddress)
    
    addingAdmin.save()
    return render(request, 'aionApp/adminpage.html')

def deleteProduct(request, id):
    selectedProducts = get_object_or_404(watche, id=id)
    selectedProducts.delete()

    currentUser = get_object_or_404(user, user_id=request.session["user"])
    addedProducts = watche.objects.all()
    context = {
        'currentUser': currentUser,
        'addedProducts': addedProducts,
    }
    return render(request, 'aionApp/shop.html', context)

def editProduct(request, id):
    selectedProducts = get_object_or_404(watche, id=id)
    selectedProducts.delete()

    currentUser = get_object_or_404(user, user_id=request.session["user"])
    addedProducts = watche.objects.all()
    context = {
        'currentUser': currentUser,
        'addedProducts': addedProducts,
    }
    addingProduct = watche(name = request.POST['productName'], description = request.POST['productDescription'], stock = request.POST['productStock'], price = request.POST['productPrice'], watch_type = request.POST['watchType'], picture = "watchPictures/" + request.POST['productPicture'], watch_id = request.session["user"], user_id = request.session["user"])
    addingProduct.save()
    return render(request, 'aionApp/shop.html', context)

def buyProduct(request, id):
    currentUser = get_object_or_404(user, user_id=request.session["user"])
    addedProducts = watche.objects.all()
    
    getName = get_object_or_404(watche, id=id).name
    getPrice = get_object_or_404(watche, id=id).price
    getPicture = get_object_or_404(watche, id=id).picture
    mediaPicture = "/media/" + str(getPicture)
    getQuantity = request.POST['productQuantity']
    total = float(getPrice) * float(getQuantity)
    
    context = {
        'currentUser': currentUser,
        'addedProducts': addedProducts,
        'getName': getName,
        'getPrice': getPrice,
        'mediaPicture': mediaPicture,
        'getQuantity': getQuantity,
        'total': total,
    }
    
    addingWatch = buy_watche(name = str(getName), price = str(getPrice), picture = getPicture, quantity = request.POST['productQuantity'], watch_id = request.session["user"], user_id = request.session["user"])
    addingWatch.save()

    return render(request, 'aionApp/checkout.html', context)

def checkOutProduct(request):
    currentUser = get_object_or_404(user, user_id=request.session["user"])
    addedProducts = watche.objects.all()
    context = {
        'currentUser': currentUser,
        'addedProducts': addedProducts,
    }
    
    buyingProduct = checkout(card_number = request.POST['card_number'], security_number = request.POST['security_number'], month = request.POST['month'], year = request.POST['year'], watch_id = request.session["user"], user_id = request.session["user"])
    buyingProduct.save()
    
    return render(request, 'aionApp/shop.html', context)
    

def checkoutPage(request):
    return render(request, 'aionApp/checkout.html')

def purchasePage(request):
    return render(request, 'aionApp/purchasepage.html')

def editProfilePage(request):
    currentUser = get_object_or_404(user, user_id = request.session["user"])
    
    addingBAddress = billing_addres(house_number = request.POST.get('bHouseNum', True), street = request.POST.get('bStreet', True), subdivision = request.POST.get('bSubdivision', True), city = request.POST.get('bCity', True), postal_code = request.POST.get('bPostal', True), country = request.POST.get('bCountry', True))
    
    addingSAddress = shipping_addres(house_number = request.POST.get('sHouseNum', True), street = request.POST.get('sStreet', True), subdivision = request.POST.get('sSubdivision', True), city = request.POST.get('sCity', True), postal_code = request.POST.get('sPostal', True), country = request.POST.get('sCountry', True))
    
    addingBAddress.save()
    addingSAddress.save()
        
    addingUser=user.objects.get(user_id=currentUser.user_id)
    addingUser= user(last_name = request.POST.get('last_name', False), first_name = request.POST.get('first_name', False), middle_initial = request.POST.get('middle_initial', False), email = request.POST.get('email', False), user_name = request.POST.get('user_name', False), billing_add=addingBAddress, shipping_add=addingSAddress)
    addingUser.save()
    
    
    
    
    
        
    print(currentUser)
    context = {'currentUser': currentUser,}
    
    return render(request, 'aionApp/editprofile.html', context)
    
    
    