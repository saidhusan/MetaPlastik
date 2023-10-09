from django.urls import path

from . import views
app_name = "packages"

urlpatterns = [

    path("", views.index, name="main_page"),

]