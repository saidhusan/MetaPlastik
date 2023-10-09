from django.db import models

types = ["Glass","Plastic","Other"]

class Bottle(models.Model):

    name = models.CharField(max_length=200)
    details = models.CharField(max_length=200,null=True)
    category = models.CharField(max_length=200)
    sub_category = models.CharField(max_length=200)
    volume = models.IntegerField()
    top_diameter = models.IntegerField()
    weight = models.IntegerField(null=True)
    shape = models.CharField(max_length=200)
