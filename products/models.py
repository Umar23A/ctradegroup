from django.db import models


class Product1(models.Model):
    image = models.ImageField(upload_to='media/')
    text = models.TextField()
    cost = models.CharField(max_length=50)


class Product2(models.Model):
    image = models.ImageField(upload_to='media/')
    text = models.TextField()
    cost = models.CharField(max_length=50)


class Product3(models.Model):
    image = models.ImageField(upload_to='media/')
    text = models.TextField()
    cost = models.CharField(max_length=50)


class Product4(models.Model):
    image = models.ImageField(upload_to='media/')
    text = models.TextField()
    cost = models.CharField(max_length=50)


class ProductTop(models.Model):
    image = models.ImageField(upload_to='media/')
    text = models.TextField()
    cost = models.CharField(max_length=50)



