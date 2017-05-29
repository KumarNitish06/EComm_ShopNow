from django.db import models

# Create your models here.
from products.models import Product

class CartItem(models.Model):
	cart = models.ForeignKey('Cart', null=True, blank=True)
	product = models.ForeignKey(Product)
	total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	quantity = models.IntegerField(default=1)
	price = models.IntegerField(default=1)
	line_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
	def __unicode__(self):
		try:
			return str(self.cart.id)
		except:
			return self.product.title
class Cart(models.Model):
	
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	

	def __unicode__(self):
		return "Cart id: %s" %(self.id)
