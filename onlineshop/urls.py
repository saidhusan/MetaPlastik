from django.urls import path

from . import views
app_name = "onlineshop"

urlpatterns = [

    path("", views.index, name="main_page"),
    path("add_bottle", views.addBottle, name="add_bottle"),
    path("create_bottle/", views.createBottle, name="create_bottle"),
    path("all_products/", views.get_product_list, name="all_products"),
    path("<str:bottle_code>/product_info/", views.product_info, name="product_info"),
    path("<str:sub_type>/get_list_by_sub_type/", views.get_list_by_sub_type, name="get_list_by_sub_type"),
    path("<str:main_type>/get_list_by_main_type/", views.get_list_by_main_type, name="get_list_by_main_type"),
    path("<str:page_name>/get_info_page/", views.get_page_by_name, name="get_page_by_name"),

]