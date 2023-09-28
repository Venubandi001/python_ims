from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import ItemForm,OrderForm
from .models import Item,Order
from django.template import loader
from django.utils import timezone
# Create your views here.

def homepage(request):
    return render(request,'homePage.html')

def ItemList(request):
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES)
        print(form.is_valid())
        form.instance.quantity = 0
        form.instance.quantity_sold = 0
        form.instance.profit_earned = 0
        form.instance.revenue = 0
        sellingprice = form.cleaned_data['selling_price']
        cost = form.cleaned_data['cost']
        if form.is_valid():
            if sellingprice < cost:
                messages.error(request, 'Selling price must be greater than the cost.')
                return render(request, "create_List.html", {'form': form})
            form.save()
            return HttpResponse('successfully inserted')
        else:
            print(form.errors)        
    else:
        form= ItemForm()
    return render(request,"create_List.html", {'form':form})

def display_ItemList(request):
    mydata = Item.objects.all().values()
    template = loader.get_template('Display_Itemlist.html')
    context = {'mydata':mydata}
    return HttpResponse(template.render(context, request))



def success_page(request):
    return render(request, 'success.html')


def view_item(request, item_id):
    
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        
        item = None

    return render(request, 'view_item.html', {'item': item})

def Order_place(request,item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            # quantity = form.cleaned_data['quantity']
            # new_order = form.save(commit=False)
            # new_order.name = item.name
            # new_order.item = item
            # new_order.cost = item.cost
            # new_order.orderdttm = timezone.now()
            # new_order.save()
            form.save()
            return redirect('success')
        else:
            print(form.errors)
    else:
        form = OrderForm()
    return render(request, 'order_item.html', {'form': form, 'item': item})

