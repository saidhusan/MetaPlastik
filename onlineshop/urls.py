from django.urls import path

from . import views
app_name = "onlineshop"

urlpatterns = [

    path("", views.index, name="main_page"),
    path("add_bottle", views.addBottle, name="add_bottle"),
    path("create_bottle/", views.createBottle, name="create_bottle"),
    path("all_products/", views.get_product_list, name="all_products"),

]