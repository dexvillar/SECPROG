# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import user, watche, review, billing_addres, shipping_addres, checkout, buy_watche, login_log, product_log, account_log
from django.db.models import Q, F, Sum
from django.contrib.auth import authenticate, login
from django_countries import countries
from passlib.hash import pbkdf2_sha256
import datetime, re
from django.contrib import messages

# Create your views here.

def homePage(request):
    if request.session["user"] > 0:
        currentUser = get_object_or_404(user, user_id = request.session["user"])
        context = {
            'currentUser': currentUser,
        }
    return render(request, 'aionApp/home.html', context)

def registerPage(request):
    getBCountry = (name for code, name in list(countries))
    getBCode = (code for code, name in list(countries))
    combined_bCountry = zip(getBCountry, getBCode)
    
    getSCountry = (name for code, name in list(countries))
    getSCode = (code for code, name in list(countries))
    combined_sCountry = zip(getSCountry, getSCode)
    context = {
        'getBCountry': getBCountry,
        'getBCode': getBCode,
        'combined_bCountry': combined_bCountry,
        'getSCountry': getSCountry,
        'getSCode': getSCode,
        'combined_sCountry': combined_sCountry,
    }
    return render(request, 'aionApp/register.html', context)

def adminPage(request):
    return render(request, 'aionApp/adminpage.html')

def accountingPage(request):
    addedProducts = watche.objects.all()
    totalSales = watche.objects.aggregate(total=Sum(F('price') * F('quantity')))['total']
    totalAnalog =  watche.objects.filter(watch_type=0).aggregate(total=Sum(F('price') * F('quantity')))['total']
    totalDigital =  watche.objects.filter(watch_type=1).aggregate(total=Sum(F('price') * F('quantity')))['total']
    totalSmart =  watche.objects.filter(watch_type=2).aggregate(total=Sum(F('price') * F('quantity')))['total']                     
    context = {
        'addedProducts': addedProducts,
        'totalSales': totalSales,
        'totalAnalog': totalAnalog,
        'totalDigital': totalDigital,
        'totalSmart': totalSmart,
    }
    return render(request, 'aionApp/accounting.html', context)

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
        password = request.POST['userPassword']
        encrypt_pass=pbkdf2_sha256.encrypt(password,rounds=12000,salt_size=32)
        for userTry in userList:
            if userTry.user_name == str(request.POST['userName']):
                if True == userTry.verify_pass(password):
                    request.session["user"] = userTry.user_id
                    choice= userTry.role_type
                    
        if request.session["user"] >= 0:
            
            
            
            currentUser = get_object_or_404(user, user_id = request.session["user"])
            context = {
                'currentUser': currentUser,
            }
            
            if choice == "0":
                logLogin=login_log(log=str(datetime.datetime.now())+" username= "+str(request.POST['userName'])+" aionApp/exitSession/"+" Log in= SUCCES ",username=str(request.POST['userName']), location="aionApp/exitSession/", action="Log in", result="SUCCES")
                logLogin.save()
                return shopPage(request)
            elif choice == "1":
                logLogin=login_log(log=str(datetime.datetime.now())+" username= "+str(request.POST['userName'])+" aionApp/exitSession/"+" Log in= SUCCES ",username=str(request.POST['userName']), location="aionApp/exitSession/", action="Log in", result="SUCCES")
                logLogin.save()
                return accountingPage(request)
            elif choice == "2":
                logLogin=login_log(log=str(datetime.datetime.now())+" username= "+str(request.POST['userName'])+" aionApp/exitSession/"+" Log in= SUCCES ",username=str(request.POST['userName']), location="aionApp/exitSession/", action="Log in", result="SUCCES")
                logLogin.save()
                return adminPage(request)
            else:
                logLogin=login_log(log=str(datetime.datetime.now())+" username= "+str(request.POST['userName'])+" aionApp/exitSession/"+" Log in= SUCCES ",username=str(request.POST['userName']), location="aionApp/exitSession/", action="Log in", result="SUCCES")
                logLogin.save()
                return render(request, 'aionApp/home.html', context)
                
        else:
                error = True
                
                request.session["user"] = -1
                logLogin=login_log(log=str(datetime.datetime.now())+" username= "+str(request.POST['userName'])+" aionApp/exitSession/"+" Log in= FAILED ATTEMPT ",username=str(request.POST['userName']), location="aionApp/exitSession/", action="Log in", result="FAILED ATTEMPT")
                logLogin.save()
                return render(request, 'aionApp/home.html', {'error': error})
    except ValueError:
        error = True
        return render(request, 'aionApp/home.html', {'error': error})
    
def shopLogIn(request):
    userList = user.objects.all()
    error = False
    try:
        password = request.POST['userPassword']
        encrypt_pass=pbkdf2_sha256.encrypt(password, rounds=12000,salt_size=32)
        for userTry in userList:
            if userTry.user_name == str(request.POST['userName']):
                if True == userTry.verify_pass(password):
                    request.session["user"] = userTry.user_id
                    choice= userTry.role_type
        if request.session["user"] >= 0:
            currentUser = get_object_or_404(user, user_id = request.session["user"])
            addedProducts = watche.objects.all()
            context = {
                'currentUser': currentUser,
                'addedProducts': addedProducts,
            }
            if choice == "1":
                logLogin=login_log(log=str(datetime.datetime.now())+" username= "+str(request.POST['userName'])+" aionApp/exitSession/"+" Log in= SUCCES ",username=str(request.POST['userName']), location="aionApp/exitSession/", action="Log in", result="SUCCES")
                logLogin.save()
                return accountingPage(request)
            elif choice == "2":
                logLogin=login_log(log=str(datetime.datetime.now())+" username= "+str(request.POST['userName'])+" aionApp/exitSession/"+" Log in= SUCCES ",username=str(request.POST['userName']), location="aionApp/exitSession/", action="Log in", result="SUCCES")
                logLogin.save()
                return adminPage(request)
            else:
                logLogin=login_log(log=str(datetime.datetime.now())+" username= "+str(request.POST['userName'])+" aionApp/exitSession/"+" Log in= SUCCES ",username=str(request.POST['userName']), location="aionApp/exitSession/", action="Log in", result="SUCCES")
                logLogin.save()
                return render(request, 'aionApp/shop.html', context)
            
        else:
                error = True
                request.session["user"] = -1
                logLogin=login_log(log=str(datetime.datetime.now())+" username= "+str(request.POST['userName'])+" aionApp/exitSession/"+" Log in= FAILED ATTEMPT ",username=str(request.POST['userName']), location="aionApp/exitSession/", action="Log in", result="FAILED ATTEMPT")
                logLogin.save()
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
    print(currentUser)
    addingProduct = watche(name = request.POST['productName'], description = request.POST['productDescription'], stock = request.POST['productStock'], price = request.POST['productPrice'], watch_type = request.POST['watchType'], picture = "watchPictures/" + request.POST['productPicture'], watch_id = request.session["user"], user_id = request.session["user"])
    addingProduct.save()
    productLog=product_log(log=str(datetime.datetime.now())+" username= "+str(currentUser)+" aionApp/shop.html"+" Added product: "+ str(request.POST['productName'])+" qty: "+ str(request.POST['productStock'])+" = SUCCES",username=str(currentUser), location="aionApp/shop.html", action="Added product: "+ str(request.POST['productName'])+" qty: "+ str(request.POST['productStock']), result="SUCCES")
    productLog.save()
    return render(request, 'aionApp/shop.html', context)
    
def signingUp(request):
    errorUsername = False
    errorPassword = False
    errorUPolicy = False
    errorPPolicy = False
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    username = request.POST['user_name']
    usernameList = user.objects.values_list('user_name', flat=True)
    usernameList = list(usernameList)
    
    getBCountry = (name for code, name in list(countries))
    getBCode = (code for code, name in list(countries))
    combined_bCountry = zip(getBCountry, getBCode)
    getSCountry = (name for code, name in list(countries))
    getSCode = (code for code, name in list(countries))
    combined_sCountry = zip(getSCountry, getSCode)
    
    for userTry in usernameList:
        if userTry != username:
            if password1 == password2:
                if re.match("^(?!admin|root|system|guest|operator|super|user|test|qa)[a-z0-9_\-.]*$", username):
                    if re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~])[^ ]{8,}$", password1):
                        addingBAddress = billing_addres(house_number = request.POST['bHouseNum'], street = request.POST['bStreet'], subdivision = request.POST['bSubdivision'], city = request.POST['bCity'], postal_code = request.POST['bPostal'], country = request.POST['bCountry'])

                        addingSAddress = shipping_addres(house_number = request.POST['sHouseNum'], street = request.POST['sStreet'], subdivision = request.POST['sSubdivision'], city = request.POST['sCity'], postal_code = request.POST['sPostal'], country = request.POST['sCountry'])

                        addingBAddress.save()
                        addingSAddress.save()

                        password = request.POST['password1']
                        encrypt_pass = pbkdf2_sha256.encrypt(password, rounds=12000,salt_size=32)

                        addingUser = user(last_name = request.POST['last_name'], first_name = request.POST['first_name'], middle_initial = request.POST['middle_initial'], email = request.POST['email'], user_name = request.POST['user_name'], password = encrypt_pass, billing_add=addingBAddress, shipping_add=addingSAddress )
                        addingUser.save()

                        logUser=account_log(log=str(datetime.datetime.now())+" username= guest aionApp/register.html"+" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email'])+" = SUCCES",username="guest", location="aionApp/register.html", action=" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email']), result="SUCCES")
                        logUser.save()
                        return render(request, 'aionApp/home.html')

                    else:
                        errorPPolicy = True
                        context = {
                            'getBCountry': getBCountry,
                            'getBCode': getBCode,
                            'combined_bCountry': combined_bCountry,
                            'getSCountry': getSCountry,
                            'getSCode': getSCode,
                            'combined_sCountry': combined_sCountry,
                            'errorPPolicy': errorPPolicy,
                        }
                        logUser=account_log(log=str(datetime.datetime.now())+" username= guest aionApp/register.html"+" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email'])+" = FAILED",username="guest", location="aionApp/register.html", action=" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email']), result="FAILED")
                        logUser.save()
                        return render(request, 'aionApp/register.html', context)
                else:
                    errorUPolicy = True
                    context = {
                        'getBCountry': getBCountry,
                        'getBCode': getBCode,
                        'combined_bCountry': combined_bCountry,
                        'getSCountry': getSCountry,
                        'getSCode': getSCode,
                        'combined_sCountry': combined_sCountry,
                        'errorUPolicy': errorUPolicy,
                    }
                    logUser=account_log(log=str(datetime.datetime.now())+" username= guest aionApp/register.html"+" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email'])+" = FAILED",username="guest", location="aionApp/register.html", action=" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email']), result="FAILED")
                    logUser.save()
                    return render(request, 'aionApp/register.html', context)
            else:
                errorPassword = True
                context = {
                    'getBCountry': getBCountry,
                    'getBCode': getBCode,
                    'combined_bCountry': combined_bCountry,
                    'getSCountry': getSCountry,
                    'getSCode': getSCode,
                    'combined_sCountry': combined_sCountry,
                    'errorPassword': errorPassword,
                }
                logUser=account_log(log=str(datetime.datetime.now())+" username= guest aionApp/register.html"+" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email'])+" = FAILED",username="guest", location="aionApp/register.html", action=" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email']), result="FAILED")
                logUser.save()
                return render(request, 'aionApp/register.html', context)
        else:
            errorUsername = True
            context = {
                'getBCountry': getBCountry,
                'getBCode': getBCode,
                'combined_bCountry': combined_bCountry,
                'getSCountry': getSCountry,
                'getSCode': getSCode,
                'combined_sCountry': combined_sCountry,
                'errorUsername': errorUsername,
            }
            logUser=account_log(log=str(datetime.datetime.now())+" username= guest aionApp/register.html"+" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email'])+" = FAILED",username="guest", location="aionApp/register.html", action=" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email']), result="FAILED")
            logUser.save()
            return render(request, 'aionApp/register.html', context)
    
    
def addAdmin(request):
    currentUser = get_object_or_404(user, user_id=request.session["user"])
    addingBAddress = billing_addres.objects.first()
    addingSAddress = shipping_addres.objects.first()
    
    errorUsername = False
    errorPassword = False
    errorUPolicy = False
    errorPPolicy = False
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    username = request.POST['user_name']
    usernameList = user.objects.values_list('user_name', flat=True)
    usernameList = list(usernameList)
    
    for userTry in usernameList:
        if userTry != username:
            if password1 == password2:
                if re.match("^(?!admin|root|system|guest|operator|super|user|test|qa)[a-z0-9_\-.]*$", username):
                    if re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~])[^ ]{8,}$", password1):
                        password = request.POST['password1']
                        encrypt_pass = pbkdf2_sha256.encrypt(password, rounds=12000,salt_size=32)

                        addingAdmin = user(last_name = request.POST['last_name'], first_name = request.POST['first_name'], middle_initial = request.POST['middle_initial'], email = request.POST['email'], role_type = request.POST['role_type'], user_name = request.POST['user_name'], password = encrypt_pass, billing_add=addingBAddress, shipping_add=addingSAddress)

                        addingAdmin.save()

                        logUser=account_log(log=str(datetime.datetime.now())+" username= "+str(currentUser)+ "aionApp/adminpage.html"+" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email'])+" = SUCCES",username=str(currentUser), location="aionApp/adminpage.html", action=" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email']), result="SUCCES")
                        logUser.save()
                        messages.add_message(request, messages.INFO, 'Successfully registered an account!')
                        return render(request, 'aionApp/adminpage.html')
                    
                    else:
                        errorPPolicy = True
                        context = {
                            'errorPPolicy': errorPPolicy,
                        }
                        logUser=account_log(log=str(datetime.datetime.now())+" username= guest aionApp/adminpage.html"+" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email'])+" = FAILED",username="guest", location="aionApp/adminpage.html", action=" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email']), result="FAILED")
                        logUser.save()
                        return render(request, 'aionApp/adminpage.html', context)
                else:
                    errorUPolicy = True
                    context = {
                        'errorUPolicy': errorUPolicy,
                    }
                    logUser=account_log(log=str(datetime.datetime.now())+" username= guest aionApp/adminpage.html"+" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email'])+" = FAILED",username="guest", location="aionApp/adminpage.html", action=" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email']), result="FAILED")
                    logUser.save()
                    return render(request, 'aionApp/adminpage.html', context)
            else:
                errorPassword = True
                context = {
                    'errorPassword': errorPassword,
                }
                logUser=account_log(log=str(datetime.datetime.now())+" username= guest aionApp/adminpage.html"+" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email'])+" = FAILED",username="guest", location="aionApp/adminpage.html", action=" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email']), result="FAILED")
                logUser.save()
                return render(request, 'aionApp/adminpage.html', context)
        else:
            errorUsername = True
            context = {
                'errorUsername': errorUsername,
            }
            logUser=account_log(log=str(datetime.datetime.now())+" username= guest aionApp/adminpage.html"+" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email'])+" = FAILED",username="guest", location="aionApp/adminpage.html", action=" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email']), result="FAILED")
            logUser.save()
            return render(request, 'aionApp/adminpage.html', context)

def deleteProduct(request, id):

    currentUser = get_object_or_404(user, user_id=request.session["user"])
    addedProducts = watche.objects.all()
    context = {
        'currentUser': currentUser,
        'addedProducts': addedProducts,
    }
    
    selectedProducts = get_object_or_404(watche, id=id)
    productLog=product_log(log=str(datetime.datetime.now())+" username= "+str(currentUser)+" aionApp/shop.html"+" Deleted product: "+ str(selectedProducts)+" qty: ALL"+" = SUCCES",username=str(currentUser), location="aionApp/shop.html", action="Deleted product: "+ str(selectedProducts)+" qty: ALL", result="SUCCES")
    productLog.save()
    selectedProducts.delete()
    
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
    productLog=product_log(log=str(datetime.datetime.now())+" username= "+str(currentUser)+" aionApp/shop.html"+" Edited product: "+ str(request.POST['productName'])+" qty: "+str(request.POST['productStock'])+" = SUCCES",username=str(currentUser), location="aionApp/shop.html", action="Deleted product: "+ str(request.POST['productName'])+" qty: "+str(request.POST['productStock']), result="SUCCES")
    productLog.save()
    return render(request, 'aionApp/shop.html', context)

def buyProduct(request, id):
    currentUser = get_object_or_404(user, user_id=request.session["user"])
    addedProducts = watche.objects.all()
    
    getName = get_object_or_404(watche, id=id).name
    getDescription = get_object_or_404(watche, id=id).description
    getPrice = get_object_or_404(watche, id=id).price
    getPicture = get_object_or_404(watche, id=id).picture
    mediaPicture = "/media/" + str(getPicture)
    getQuantity = request.POST['productQuantity']
    total = float(getPrice) * float(getQuantity)
    
    getStock = get_object_or_404(watche, id=id).stock
    updateStock = int(getStock) - int(getQuantity)
    
    getWatchType = get_object_or_404(watche, id=id).watch_type
    
    context = {
        'currentUser': currentUser,
        'addedProducts': addedProducts,
        'getName': getName,
        'getPrice': getPrice,
        'mediaPicture': mediaPicture,
        'getQuantity': getQuantity,
        'total': total,
    }
    
    selectedWatch = get_object_or_404(watche, id=id)
    selectedWatch.delete()
    
    updatingWatch = watche(name = str(getName), description = str(getDescription), stock = updateStock, price = str(getPrice), watch_type = str(getWatchType), quantity = getQuantity, picture = getPicture, watch_id = request.session["user"], user_id = request.session["user"])
    updatingWatch.save()
    
    buyingWatch = buy_watche(name = str(getName), description = str(getDescription), price = str(getPrice), picture = getPicture, quantity = request.POST['productQuantity'], watch_id = request.session["user"], user_id = request.session["user"])
    buyingWatch.save()

    return render(request, 'aionApp/checkout.html', context)

def checkOutProduct(request):
    currentUser = get_object_or_404(user, user_id=request.session["user"])
    addedProducts = watche.objects.all()
    error=True
    
    context = {
        'currentUser': currentUser,
        'addedProducts': addedProducts,
    }
    
    card_number = request.POST['card_number']
    if ccValidation(card_number):
        return render(request, 'aionApp/checkout.html', {'error':error})
        
    buyingProduct = checkout(card_number = request.POST['card_number'], security_number = request.POST['security_number'], month = request.POST['month'], year = request.POST['year'], watch_id = request.session["user"], user_id = request.session["user"])
    buyingProduct.save()
    
    return render(request, 'aionApp/shop.html', context)
    

def checkoutPage(request):
    return render(request, 'aionApp/checkout.html')

def purchasePage(request):
    currentUser = get_object_or_404(user, user_id=request.session["user"])
    userProducts = buy_watche.objects.filter(user_id=request.session["user"])
    context = {
        'currentUser': currentUser,
        'userProducts': userProducts,
    }
    return render(request, 'aionApp/purchasepage.html', context)

def addReview(request, id):
    currentUser = get_object_or_404(user, user_id=request.session["user"])
    userProducts = buy_watche.objects.filter(user_id=request.session["user"])
    getName = get_object_or_404(buy_watche, id=id).name
    context = {
        'currentUser': currentUser,
        'userProducts': userProducts,
    }
    addingReview = review(reviews = request.POST['review'], name = str(getName), watch_id = request.session["user"], user_id = request.session["user"])
    addingReview.save()
    return render(request, 'aionApp/purchasepage.html', context)

def reviewPage(request, id):
    if request.session["user"] > 0:
        currentUser = get_object_or_404(user, user_id=request.session["user"])
        addedProducts = watche.objects.all()

        getName = get_object_or_404(watche, id=id).name
        upperName = str(getName).upper()

        getDescription = get_object_or_404(watche, id=id).description
        getStock = get_object_or_404(watche, id=id).stock
        getPrice = get_object_or_404(watche, id=id).price
        getWatchType = get_object_or_404(watche, id=id).watch_type
        getPicture = get_object_or_404(watche, id=id).picture
        mediaPicture = "/media/" + str(getPicture)

        addedReviews = review.objects.filter(name=str(getName))
        context = {
            'currentUser': currentUser,
            'addedProducts': addedProducts,
            'getName': getName,
            'upperName': upperName,
            'getDescription': getDescription,
            'getStock': getStock,
            'getPrice': getPrice,
            'getWatchType': getWatchType,
            'mediaPicture': mediaPicture,
            'addedReviews': addedReviews,
        }
        return render(request, 'aionApp/review.html', context)
    else:
        addedProducts = watche.objects.all()
        getName = get_object_or_404(watche, id=id).name
        upperName = str(getName).upper()
        getDescription = get_object_or_404(watche, id=id).description
        getStock = get_object_or_404(watche, id=id).stock
        getPrice = get_object_or_404(watche, id=id).price
        getWatchType = get_object_or_404(watche, id=id).watch_type
        getPicture = get_object_or_404(watche, id=id).picture
        mediaPicture = "/media/" + str(getPicture)
        addedReviews = review.objects.filter(name=str(getName))
        context = {
            'addedProducts': addedProducts,
            'getName': getName,
            'upperName': upperName,
            'getDescription': getDescription,
            'getStock': getStock,
            'getPrice': getPrice,
            'getWatchType': getWatchType,
            'mediaPicture': mediaPicture,
            'addedReviews': addedReviews,
        }
        return render(request, 'aionApp/review.html', context)
        
def editProfilePage(request):
    currentUser = get_object_or_404(user, user_id = request.session["user"])
    getBCountry = (name for code, name in list(countries))
    getBCode = (code for code, name in list(countries))
    combined_bCountry = zip(getBCountry, getBCode)
    getSCountry = (name for code, name in list(countries))
    getSCode = (code for code, name in list(countries))
    combined_sCountry = zip(getSCountry, getSCode)
    context = {
        'currentUser': currentUser,
        'getBCountry': getBCountry,
        'getBCode': getBCode,
        'combined_bCountry': combined_bCountry,
        'getSCountry': getSCountry,
        'getSCode': getSCode,
        'combined_sCountry': combined_sCountry,
    }
    return render(request, 'aionApp/editprofile.html', context)

def editingProfile(request):
    currentUser = get_object_or_404(user, user_id = request.session["user"])
    addingUser=user.objects.get(user_id=currentUser.user_id)
    
    errorUsername = False
    errorPassword = False
    errorUPolicy = False
    errorPPolicy = False
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    username = request.POST['user_name']
    usernameList = user.objects.values_list('user_name', flat=True)
    usernameList = list(usernameList)
    
    getBCountry = (name for code, name in list(countries))
    getBCode = (code for code, name in list(countries))
    combined_bCountry = zip(getBCountry, getBCode)
    getSCountry = (name for code, name in list(countries))
    getSCode = (code for code, name in list(countries))
    combined_sCountry = zip(getSCountry, getSCode)
    
    for userTry in usernameList:
        if userTry != username:
            if password1 == password2:
                if re.match("^(?!admin|root|system|guest|operator|super|user|test|qa)[a-z0-9_\-.]*$", username):
                    if re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~])[^ ]{8,}$", password1):
                        addingBAddress = billing_addres(house_number =request.POST.get('bHouseNum', addingUser.billing_add.house_number), street = request.POST.get('bStreet', addingUser.billing_add.street), subdivision = request.POST.get('bSubdivision', addingUser.billing_add.subdivision), city = request.POST.get('bCity', addingUser.billing_add.city), postal_code = request.POST.get('bPostal', addingUser.billing_add.postal_code), country = request.POST.get('bCountry', addingUser.billing_add.country))

                        addingSAddress = shipping_addres(house_number = request.POST.get('sHouseNum', addingUser.shipping_add.house_number), street =request.POST.get('sStreet', addingUser.shipping_add.street), subdivision =request.POST.get('sSubdivision', addingUser.shipping_add.subdivision), city =request.POST.get('sCity', addingUser.shipping_add.city), postal_code = request.POST.get('sPostal', addingUser.shipping_add.postal_code), country = request.POST.get('sCountry', addingUser.shipping_add.country))

                        addingBAddress.save()
                        addingSAddress.save()

                        if request.POST.get('password1', addingUser.password)==addingUser.password:
                            encrypt_pass=addingUser.password
                        else:
                            password = request.POST['password1']
                            encrypt_pass = pbkdf2_sha256.encrypt(password, rounds=12000,salt_size=32)
                        addingUser.last_name=request.POST.get('last_name', addingUser.last_name)
                        addingUser.first_name = request.POST.get('first_name', addingUser.first_name)
                        addingUser.middle_initial = request.POST.get('middle_initial', addingUser.middle_initial)
                        addingUser.email = request.POST.get('email', addingUser.email)
                        addingUser.user_name = request.POST.get('user_name', addingUser.user_name)
                        addingUser.password=encrypt_pass
                        addingUser.billing_add=addingBAddress
                        addingUser.shipping_add=addingSAddress
                        addingUser.save()
                        logUser=account_log(log=str(datetime.datetime.now())+" username= "+str(currentUser)+" aionApp/editprofile.html"+" Editted profile: "+ str(request.POST.get('user_name', addingUser.user_name))+" "+ str(request.POST.get('email', addingUser.email))+" = SUCCES",username=str(currentUser), location="aionApp/editprofile.html", action=" Signed up: "+ str(request.POST.get('user_name', addingUser.user_name))+" "+ str(request.POST.get('email', addingUser.email)), result="SUCCES")
                        logUser.save()

                        context = {
                            'currentUser': currentUser,
                        }
                        return render(request, 'aionApp/profile.html', context)
                    else:
                        errorPPolicy = True
                        context = {
                            'currentUser': currentUser,
                            'getBCountry': getBCountry,
                            'getBCode': getBCode,
                            'combined_bCountry': combined_bCountry,
                            'getSCountry': getSCountry,
                            'getSCode': getSCode,
                            'combined_sCountry': combined_sCountry,
                            'errorPPolicy': errorPPolicy,
                        }
                        logUser=account_log(log=str(datetime.datetime.now())+" username= guest aionApp/editprofile.html"+" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email'])+" = FAILED",username="guest", location="aionApp/editprofile.html", action=" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email']), result="FAILED")
                        logUser.save()
                        return render(request, 'aionApp/profile.html', context)
                else:
                    errorUPolicy = True
                    context = {
                        'currentUser': currentUser,
                        'getBCountry': getBCountry,
                        'getBCode': getBCode,
                        'combined_bCountry': combined_bCountry,
                        'getSCountry': getSCountry,
                        'getSCode': getSCode,
                        'combined_sCountry': combined_sCountry,
                        'errorUPolicy': errorUPolicy,
                    }
                    logUser=account_log(log=str(datetime.datetime.now())+" username= guest aionApp/editprofile.html"+" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email'])+" = FAILED",username="guest", location="aionApp/editprofile.html", action=" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email']), result="FAILED")
                    logUser.save()
                    return render(request, 'aionApp/editprofile.html', context)
            else:
                errorPassword = True
                context = {
                    'currentUser': currentUser,
                    'getBCountry': getBCountry,
                    'getBCode': getBCode,
                    'combined_bCountry': combined_bCountry,
                    'getSCountry': getSCountry,
                    'getSCode': getSCode,
                    'combined_sCountry': combined_sCountry,
                    'errorPassword': errorPassword,
                }
                logUser=account_log(log=str(datetime.datetime.now())+" username= guest aionApp/editprofile.html"+" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email'])+" = FAILED",username="guest", location="aionApp/editprofile.html", action=" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email']), result="FAILED")
                logUser.save()
                return render(request, 'aionApp/editprofile.html', context)
        else:
            errorUsername = True
            context = {
                'currentUser': currentUser,
                'getBCountry': getBCountry,
                'getBCode': getBCode,
                'combined_bCountry': combined_bCountry,
                'getSCountry': getSCountry,
                'getSCode': getSCode,
                'combined_sCountry': combined_sCountry,
                'errorUsername': errorUsername,
            }
            logUser=account_log(log=str(datetime.datetime.now())+" username= guest aionApp/editprofile.html"+" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email'])+" = FAILED",username="guest", location="aionApp/editprofile.html", action=" Signed up: "+ str(request.POST['user_name'])+" "+ str(request.POST['email']), result="FAILED")
            logUser.save()
            return render(request, 'aionApp/editprofile.html', context)

def search(request):
    if request.session["user"] > 0:
        currentUser = get_object_or_404(user, user_id=request.session["user"])
        Swatches = watche.objects.all()
        query = request.GET.get("q")
        if query:
            Swatches = Swatches.filter(
                Q(name__icontains=query)
            ).distinct()
            context = {
                'currentUser': currentUser,
                'Swatches': Swatches,
            }
            return render(request, 'aionApp/search.html', context)
        else:
            return render(request, 'aionApp/home.html')
    else: 
        Swatches = watche.objects.all()
        query = request.GET.get("q")
        if query:
            Swatches = Swatches.filter(
                Q(name__icontains=query)
            ).distinct()
            context = {
                'Swatches': Swatches,
            }
            return render(request, 'aionApp/search.html',
                context)
        else:
            return render(request, 'aionApp/home.html')
             
def analog(request):
    if request.session["user"] > 0:
        currentUser = get_object_or_404(user, user_id=request.session["user"])
        Swatches = watche.objects.filter(watch_type=0)
        context = {
            'currentUser': currentUser,
            'Swatches': Swatches,
        }
        return render(request, 'aionApp/analog.html', context)
    else:
        Swatches = watche.objects.filter(watch_type=0)
        context = {
            'Swatches': Swatches,
        }
        return render(request, 'aionApp/analog.html', context)

def digital(request):
    if request.session["user"] > 0:
        currentUser = get_object_or_404(user, user_id=request.session["user"])
        Swatches = watche.objects.filter(watch_type=1)
        context = {
            'currentUser': currentUser,
            'Swatches': Swatches,
        }
        return render(request, 'aionApp/digital.html', context)
    else: 
        Swatches = watche.objects.filter(watch_type=1)
        context = {
            'Swatches': Swatches,
        }
        return render(request, 'aionApp/digital.html', context)

def smart(request):
    if request.session["user"] > 0:
        currentUser = get_object_or_404(user, user_id=request.session["user"])
        Swatches = watche.objects.filter(watch_type=2)
        context = {
            'currentUser': currentUser,
            'Swatches': Swatches,
        }
        return render(request, 'aionApp/smart.html', context)
    else:
        Swatches = watche.objects.filter(watch_type=2)
        context = {
            'Swatches': Swatches,
        }
        return render(request, 'aionApp/smart.html', context)
        
def ccValidation(card_number):
    sum=0
    temp=0
    checksum=0
    for i in range(16):
        temp=card_number %10
        card_number=card_number/10
        if(i == 0):
            checksum = temp
        elif not (i % 2 == 0):
            temp = temp * 2
            if temp > 9:
                temp= temp-9
                sum=sum+temp;	
    if checksum == sum % 9:
        return 1
    else:
        return 0