from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .forms import productForm
from .models import Product
# Create your views here.
@csrf_exempt
def index(request):
    val=request.GET.get('val')
    if not val:
        product=Product.objects.all()
    else:
        product=Product.objects.filter(name=val)
    template=loader.get_template('index.html')
    form=productForm()
    forms={
        'form':form,
        'prd':product
    }
    return HttpResponse(template.render(forms))

@csrf_exempt
def create(request):
    name=request.POST.get('name')
    color=request.POST.get('color')
    price=request.POST.get('price')
    qty=request.POST.get('qty')
    tax=request.POST.get('tax')
    total=request.POST.get('total')
    net=request.POST.get('net')
    notes=request.POST.get('notes')
    prod=Product(name=name,color=color,price=price,qty=qty,tax=tax,total=total,net=net,notes=notes)
    prod.save()
    return redirect('/')

def delete(request,id):
    prd=Product.objects.get(id=id)
    prd.delete()
    return redirect('/')

def edit(request,id):
     template=loader.get_template('edit.html')
     prd=Product.objects.get(id=id)
     items={
         'produc':prd
     }
     return HttpResponse(template.render(items))
@csrf_exempt
def update(request):
    id=request.POST.get('id')
    name=request.POST.get('name')
    color=request.POST.get('color')
    price=request.POST.get('price')
    qty=request.POST.get('qty')
    tax=request.POST.get('tax')
    total=request.POST.get('total')
    net=request.POST.get('net')
    notes=request.POST.get('notes')

    prd=Product.objects.get(id=id)

    prd.name=name 
    prd.color=color
    prd.price=price 
    prd.qty=qty 
    prd.tax=tax
    prd.total=total
    prd.net=net
    prd.notes=notes

    prd.save()

    return redirect('/')








