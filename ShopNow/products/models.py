from django.db import models

class Product(models.Model):
    pname = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    details = models.TextField()
    Price_A=models.IntegerField(null=True)
    image = models.CharField(max_length=1000,null=True)
    
    def __str__(self):
        return self.pname
