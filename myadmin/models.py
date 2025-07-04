from django.db import models

class Category(models.Model):
    catgid=models.AutoField(primary_key=True)
    catname=models.CharField(max_length=50,unique=True)
    caticonname=models.CharField(max_length=100)   

class SubCategory(models.Model):
    subcatgid=models.AutoField(primary_key=True)
    catname=models.CharField(max_length=50)
    subcatname=models.CharField(max_length=50,unique=True)
    subcaticonname=models.CharField(max_length=100)    