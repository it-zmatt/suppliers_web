from django.shortcuts import render

def homePage(request):
    return render(request, 'home.html')

def loginPage(request):
    return render(request, 'login.html')