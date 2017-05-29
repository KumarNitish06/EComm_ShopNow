
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

from products.models import Product

from .models import Cart, CartItem

def view(request):
	'''try:
		the_id = request.session['cart_id']'''
	cart = CartItem.objects.all()
	'''except:
		the_id = None'''


		
	'''if the_id:'''
	new_total = 0.00
	for item in cart :
		line_total = float(item.product.Price_A)
		new_total += line_total
	
	cart.total = new_total
	'''cart.save()'''
	context = {"cart": cart}
	'''else:
	empty_message = "Your Cart is Empty, please keep shopping."
	context = {"empty": True, "empty_message": empty_message}'''
	
	template = "products/view.html"
	return render(request, template, context)


def remove_from_cart(request, id):
       
	cartitem = CartItem.objects.get(id=id)
	cartitem.delete()
	'''cartitem.cart = None
	cartitem.save()'''
	return HttpResponseRedirect(reverse("cart"))
		



def add_to_cart(request, id):
	product=Product.objects.get(id=id)
	cart_item = CartItem.objects.create( product=product,price=product.Price_A)
	
	cart_item.save()
	return HttpResponseRedirect(reverse("cart"))
