from django.db import models


class Product1(models.Model):
    image = models.ImageField(upload_to='/media')
    text = models.TextField()
    cost = models.CharField()


class Product2(models.Model):
    image = models.ImageField(upload_to='/media')
    text = models.TextField()
    cost = models.CharField()


class Product3(models.Model):
    image = models.ImageField(upload_to='/media')
    text = models.TextField()
    cost = models.CharField()


class Product4(models.Model):
    image = models.ImageField(upload_to='/media')
    text = models.TextField()
    cost = models.CharField()


