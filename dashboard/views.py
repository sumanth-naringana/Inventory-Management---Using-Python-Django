from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages


@login_required
def index(request):
       orders=Order.objects.all()
       products=Product.objects.all()
       workers_count=User.objects.all().count()
       item_count=Product.objects.all().count()
       order_count=Order.objects.all().count()
       if request.method=='POST':
              form=OrderForm(request.POST)
              if form.is_valid():
                     instance=form.save(commit=False)
                     instance.staff=request.user
                     instance.save()
                     return redirect('dashboard-index')
       else:
              form=OrderForm()

       context={
              'orders':orders,
              'form':form,
              'products':products,
              'workers_count':workers_count,
              'item_count':item_count,
              'order_count':order_count
       }
       return render(request,"dashboard/index.html",context)

@login_required
def staff(request):
       workers=User.objects.all()
       workers_count=User.objects.all().count()
       item_count=Product.objects.all().count()
       order_count=Order.objects.all().count()
       context={
              'workers':workers,
              'workers_count':workers_count,
              'item_count':item_count,
              'order_count':order_count
       }
       return render(request,"dashboard/staff.html", context)

def staff_detail(request, pk):
       users=User.objects.get(id=pk)

       context={
              'users':users
       }
       return render(request,'dashboard/staff_detail.html',context)


@login_required
def product(request):
       items=Product.objects.all()  #ORM Method
       # items=Product.objects.raw('SELECT * FROM dashboard_product') #we can use raw method to work with sql
       
       workers_count=User.objects.all().count()
       item_count=Product.objects.all().count()
       order_count=Order.objects.all().count()
       if request.method=='POST':
              add_product=ProductForm(request.POST)
              if add_product.is_valid():
                     add_product.save()
                     product_name=add_product.cleaned_data.get('name')
                     messages.success(request, f'{product_name} has been added')
                     return redirect('dashboard-product')
       else:
              add_product=ProductForm()

       context={
              'items':items,
              'add_product':add_product,
              'item_count':item_count,
              'workers_count':workers_count,
              'order_count':order_count
       }

       return render(request,"dashboard/product.html",context )


def product_update(request,pk):
       item=Product.objects.get(id=pk)
       if request.method=='POST':
              
              form=ProductForm(request.POST,instance=item)
              if form.is_valid():
                     form.save()
                     return redirect('dashboard-product')
       else:
              form=ProductForm(instance=item)
       
       context={
              'form':form
       }
       return render(request,'dashboard/product_edit.html',context)


def product_delete(request,pk):
       item=Product.objects.get(id=pk)
       if request.method=='POST':

              item.delete()
              return redirect('dashboard-product')


       return render(request, 'dashboard/product_delete.html')

@login_required
def order(request):
       orders=Order.objects.all()
       workers_count=User.objects.all().count()
       item_count=Product.objects.all().count()
       order_count=Order.objects.all().count()
       context={
              'orders':orders,
              'order_count':order_count,
              'workers_count':workers_count,
              'item_count':item_count
       }
       return render(request,"dashboard/order.html",context)


