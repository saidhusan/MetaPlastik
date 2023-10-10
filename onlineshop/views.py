from django.shortcuts import render
from .models import *
def index(request):
    return render(request, "onlineshop/main.html")

def addBottle(request):
    return render(request, "onlineshop/add_bottle.html")

def thank_you(request):
    return render(request, "onlineshop/thank_you.html")

def get_product_list(request):
    product_list = Bottle.objects.all()
    context = {"product_list":product_list}
    return render(request, "onlineshop/Products.html",context)


#create Bottle objects
def createBottle(request):
    bottle_code = request.POST["bottle_code"]
    main_type = request.POST["main_type"]
    sub_type1 = request.POST["sub_type1"]
    weigth = request.POST["weigth"]
    width = request.POST["width"]
    height = request.POST["height"]
    neck_size = request.POST["neck_size"]
    volume = request.POST["volume"]


    bottle = Bottle(name=bottle_code,category=main_type,sub_category=sub_type1,volume=volume,neck_size=neck_size,
                    weight = weigth,height = height,width=width)
    bottle.save()

    return thank_you(request)