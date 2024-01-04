from django.db import models

# Create your models here.
class contact_Db(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    email=models.EmailField(max_length=30,null=True,blank=True)
    subject=models.CharField(max_length=30,null=True,blank=True)
    message=models.CharField(max_length=30,null=True,blank=True)
class registration_Db(models.Model):
    NAME = models.CharField(max_length=30, null=True, blank=True)
    EMAIL = models.CharField(max_length=30, null=True, blank=True, unique=True)
    PASSWORD = models.CharField(max_length=30, null=True, blank=True)
    CPASSWORD = models.CharField(max_length=30, null=True, blank=True)
class cart_Db(models.Model):
    username=models.CharField(max_length=20,null=True,blank=True,unique=True)
    productname=models.CharField(max_length=20,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    totalprice=models.IntegerField(null=True,blank=True)

class CheckoutDB(models.Model):
    firstnm = models.CharField(max_length=100, null=True, blank=True)
    lastnm = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)