from django import forms

class signUpForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Age = forms.IntegerField()
    Address = forms.CharField(max_length=200, widget=forms.Textarea)
    Contact = forms.CharField(max_length=15)
    Gender = forms.CharField(max_length=10)
    State = forms.CharField(max_length=25)
    PinCode = forms.IntegerField()
    Country = forms.CharField(max_length=20)
    Email = forms.EmailField(max_length=50)
    Password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    Confirm_Password =forms.CharField(max_length=50, widget=forms.PasswordInput)

class loginForm(forms.Form):
    Email = forms.EmailField(max_length=50)
    Password = forms.CharField(max_length=50, widget=forms.PasswordInput)
   
