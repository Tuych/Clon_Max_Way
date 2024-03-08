from django.shortcuts import render

def home(request):
    return render(request,"index.html",{})

def order(request):
    return render(request,"order.html",{})
