from django.shortcuts import render
from .models import *
def index(request):
    return render(request, "onlineshop/main.html")
def addBottle(request):
    return render(request, "onlineshop/add_bottle.html")


#create package objects and send you to "you have successfuly created package" page
def createBottle(request):
    package_name = request.POST["name"]

    bottle = Bottle(name=,category=,sub_category,volume,neck_size,weight,height,width)
    return render(request, "packages/package_added.html",{"id":bottle})