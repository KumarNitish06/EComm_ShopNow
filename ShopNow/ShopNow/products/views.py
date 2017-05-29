from django.shortcuts import render, HttpResponse
from .models import Product
from Userform.models import Customer, Order
# Create your views here.
def index(request):
    return render(request, 'products/home.html', {'Name' : 'Login/SignUp', 'Email' : 'NaN', 'Contact' : 'Nan', 'Address' : 'Nan' })

def index2(request):
    return render(request, 'products/home2.html',)

def mobile(request):
    products = Product.objects.filter(category='Mobiles')
    context = {'products': products}
    template = 'products/mobile.html'	
    return render(request, template, context)
def laptops(request):
    products = Product.objects.filter(category='Laptops')
    context = {'products': products}
    template = 'products/laptops.html'	
    return render(request, template, context)
def sports(request):
    products = Product.objects.filter(category='Sports')
    context = {'products': products}
    template = 'products/sports.html'	
    return render(request, template, context)
def fashion(request):
    products = Product.objects.filter(category='Fashion')
    context = {'products': products}
    template = 'products/fashion.html'	
    return render(request, template, context)
def electronics(request):
    products = Product.objects.filter(category='Electronics')
    context = {'products': products}
    template = 'products/electronics.html'	
    return render(request, template, context)
def search(request):
	
     q= request.GET['q']
	
     products = Product.objects.filter(pname=q)
     context = {'query': q, 'products': products}
     template = 'products/results.html'	
	
     return render(request, template, context)

def detail(request):
    q= request.GET['p']

    products = Product.objects.filter(pname=q)
    context = {'query': q, 'products': products}
    template = 'products/results.html'	
	
    return render(request, template, context)

def buynow(request):
    q= request.GET['p']
    email = request.GET.get('r','')
    print(email)
    data = Customer.objects.get(Email=email)
    name = data.Name
    address = data.Address
    contact = data.Contact
    state = data.State
    pincode = data.PinCode
    print(q)
    products = Product.objects.get(pname=q)
    print(products)
    pname = products.pname

    new_order = Order(ProductName=pname, Name=name, Email=email, Address=address, State=state, PinCode=pincode)
    new_order.save()

    return HttpResponse("<h1>Order placed Successfully</h1>")
    
