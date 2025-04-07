from django.forms import ModelForm
from .models import Product
from django import forms

class productForm(ModelForm):
    class  Meta:
       model=Product
       fields=('name','color','price','qty','tax','total','net','notes')


widgets={
'name':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
'color':forms.TextInput(attrs={'class':'form-control'}),
'price':forms.TextInput(attrs={'class':'form-control'}),
'qty':forms.TextInput(attrs={'class':'form-control'}),
'tax':forms.TextInput(attrs={'class':'form-control'}),
'total':forms.TextInput(attrs={'class':'form-control'}),
}
