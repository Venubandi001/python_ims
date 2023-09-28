from django import forms
from .models import Item,Order



class ItemForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    cost = forms.DecimalField(max_digits=10, decimal_places=2)
    quantity = forms.IntegerField()
    quantity_sold = forms.IntegerField()
    selling_price = forms.DecimalField(max_digits=10, decimal_places=2)
    profit_earned = forms.DecimalField(max_digits=10, decimal_places=2)
    revenue = forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Item
        fields = ['name', 'cost', 'selling_price']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'item', 'quantity', 'cost', 'orderdttm', 'is_received', 'is_cancel']