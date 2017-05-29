from django.db import models

class Customer(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Address = models.TextField(max_length=200)
    Contact = models.CharField(max_length=15)
    Gender = models.CharField(max_length=10)
    State = models.CharField(max_length=25)
    PinCode = models.IntegerField()
    Country = models.CharField(max_length=20)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=50)
    Joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.Name

class Order(models.Model):
    ProductName = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Address = models.TextField(max_length=200)
    State = models.CharField(max_length=25)
    PinCode = models.IntegerField()

    def __str__(self):
            return self.ProductName
