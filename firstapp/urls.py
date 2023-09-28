
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    # path('admin/', admin.site.urls),
    path('itemlist', views.ItemList, name='Itemlist'),
    path('success', views.success_page, name='success'),
    path('Displaylist', views.display_ItemList, name='Displaylist'),
    # path('view/',views.view_item, name='view page')
    path('view_item/<int:item_id>/', views.view_item, name='view_item'),
    path('order_place/<int:item_id>/', views.Order_place, name='order_place'),
]
