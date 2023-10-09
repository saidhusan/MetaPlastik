from django.db import models

types = ["Glass","Plastic","Other"]


class Bottle(models.Model):

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    sub_category = models.CharField(max_length=200)
    volume = models.IntegerField()
    neck_size = models.DecimalField(max_digits=5,decimal_places=2)
    weight = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    height = models.IntegerField(null=True)
    width = models.IntegerField(null=True)