from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('sales/', views.sales_entry, name='sales_entry'),
    path('api/add-sale/', views.add_sale, name='add_sale'),
    path('api/product-price/<int:product_id>/', views.get_product_price, name='get_product_price'),
    path('api/restock/', views.restock, name='restock'),
    path('inventory/', views.inventory, name='inventory'),
    path('history/', views.sales_history, name='sales_history'),
]
