from django.db import models

class category_Db(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    description=models.CharField(max_length=20,null=True,blank=True)
    image=models.ImageField(upload_to="Images",null=True,blank=True)
class product_Db(models.Model):
    category=models.CharField(max_length=30,null=True,blank=True)
    name=models.CharField(max_length=20,null=True,blank=True)
    price=models.IntegerField(not True,blank=True)
    description=models.CharField(max_length=20,null=True,blank=True)
    image=models.ImageField(upload_to="Images",null=True,blank=True)
