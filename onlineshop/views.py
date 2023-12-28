from django.shortcuts import render
from .models import *
from . import ImageManager

def index(request):
    return render(request, "onlineshop/main.html")

def addBottle(request):
    return render(request, "onlineshop/add_bottle.html")

def bottle_added(request):
    return render(request, "onlineshop/bottle_added.html")


def get_page_by_name(request,page_name):
    return render(request, "onlineshop/"+page_name+".html")

def get_product_list(request):
    product_list = Bottle.objects.all()
    context = {"product_list":product_list}
    return render(request, "onlineshop/Products.html",context)


def get_list_by_main_type(request,main_type):
    product_list = Bottle.objects.filter(category= main_type)
    context = {"product_list": product_list}
    return render(request, "onlineshop/Products.html", context)

def get_list_by_sub_type(request,sub_type):
    product_list = Bottle.objects.filter(sub_category= sub_type)
    context = {"product_list": product_list}
    return render(request, "onlineshop/Products.html", context)


def product_info(request,bottle_code):

    try:
        print(bottle_code)
        product = Bottle.objects.get(name = bottle_code)
        return render(request, "onlineshop/product_info.html",
                      {"product": product})

    except Bottle.DoesNotExist as error:
        return error_page(request,error)


#create Bottle objects
# Problems with weight and some other parameters
def createBottle(request):
    bottle_code = request.POST["bottle_code"]
    main_type = request.POST["main_type"]
    weight = request.POST["weight"]
    width = request.POST["width"]
    height = request.POST["height"]
    neck_size = request.POST["neck_size"]
    volume = request.POST["volume"]
    refer_code = request.POST['refer_code']
    image = request.FILES['image']

    sub_type = None
    if(main_type == "PET\PE\PP ÜRUNLER"):
        sub_type = request.POST["sub_type1"]
    elif(main_type == "CAM ÜRUNLER"):
        sub_type = request.POST["sub_type2"]
    elif (main_type == "PET\PE\PP ÜRUNLER"):
        sub_type = request.POST["sub_type3"]
    elif (main_type == "AKSESUARLAR"):
        sub_type = request.POST["sub_type4"]
    else:
        print("Not idetified")
        sub_type = request.POST["sub_type1"]

    url = ImageManager.UploadImage(image,bottle_code)

    if(not isBottleExist(bottle_code)):
        try:
             bottle = Bottle(name=bottle_code,refer_code=refer_code,category=main_type,sub_category=sub_type,volume=volume,neck_size=neck_size,
                    weight = weight,height = height,width=width,img_url=url)
             bottle.save()
             return render(request, "onlineshop/bottle_added.html")

        except Exception as exp:
            context = {"error_message": str(exp)}
            return render(request, "onlineshop/bottle_added.html",context)

    else:
        context = {"error_message": "Bu Ürün Kodu zaten mevcut! Ürün Kodunu Değiştir"}
        return render(request,"onlineshop/bottle_added.html",context)

def error_page(request,error_message):
    context = {"error_message": str(error_message)}
    return render(request, "onlineshop/error_page.html", context)


def isBottleExist(bottle_code):
    try:
        product = Bottle.objects.get(name = bottle_code)
        return True

    except Bottle.DoesNotExist:
        return False