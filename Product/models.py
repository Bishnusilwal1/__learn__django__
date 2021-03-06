from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    stock = models.IntegerField(null=True)
    image_url = models.CharField(max_length=2000)

    def __str__(self):
        return self.name

class Person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()

class Student(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    batch=models.CharField(max_length=200)
    image_url=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)

