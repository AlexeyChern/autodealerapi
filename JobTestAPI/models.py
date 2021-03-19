from django.db import models


class Cars(models.Model):
    id = models.AutoField(primary_key=True)
    ModelName = models.CharField(max_length=50 ,default="Unknown model")
    BrandName = models.CharField(max_length=50,default="Unknown brand")


class Dealer(models.Model):
    id = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=50, default="Unknown company")


class Comparing(models.Model):
    id = models.AutoField(primary_key=True)
    DealerId = models.IntegerField(null=False)
    CarId = models.IntegerField(null=False)
    Price = models.FloatField(null=False)
    Quantity = models.IntegerField(null=False)
    IsNew = models.BooleanField(default=True)
