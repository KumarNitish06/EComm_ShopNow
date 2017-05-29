from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from .forms import signUpForm, loginForm
from .models import Customer
from django.template.response import TemplateResponse

def signUp(request):

    if request.method == 'POST':
        form = signUpForm(data = request.POST)

        if form.is_valid():
            print ("form is fine")
            name = form.cleaned_data['Name']
            age = form.cleaned_data['Age']
            address = form.cleaned_data['Address']
            contact = form.cleaned_data['Contact']
            gender = form.cleaned_data['Gender']
            state = form.cleaned_data['State']
            pincode = form.cleaned_data['PinCode']
            country = form.cleaned_data['Country']
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']
            cpassword = form.cleaned_data['Confirm_Password']
            
            if password != cpassword:
                return HttpResponse("<h1>Password not matched</h1>")

            new_user = Customer(Name=name, Age=age, Address=address, Contact=contact, Gender=gender, State=state, PinCode=pincode, Country=country, Email=email, Password=password)
            new_user.save()

            return HttpResponse("<h1>Thank you for signing up</h1>")

        else:
            return HttpResponse("<h1>Invalid Form</h1>")
    else:
        form = signUpForm()

    return render(request, 'products/contact.html', {'form': form})
        
def login(request):

    if request.method == 'POST':
        form = loginForm(data = request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']
            data = Customer.objects.get(Email=email)
            print (email)

            if password == data.Password:
                return render(request, 'products/home.html', {'Email' : email, 'Name' : data.Name, 'Address' : data.Address, 'Contact' : data.Contact, 'PinCode' : data.PinCode, 'State' : data.State })  # Redirect to new page, email which is needed to be passed to new page is stored in 'email' variable.
            else:
                return HttpResponse("<h3>Invalid Login Attempt</h3>")
        
    else:
        form = loginForm()

    return render(request, 'products/login.html', {'form': form})
