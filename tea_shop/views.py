from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Sum, Q
from django.utils import timezone
from datetime import timedelta
from .models import Product, Sale, Inventory
import json


def dashboard(request):
    """Main dashboard with sales stats."""
    today = timezone.now().date()
    week_ago = timezone.now() - timedelta(days=7)
    month_ago = timezone.now() - timedelta(days=30)

    daily_sales = Sale.objects.filter(timestamp__date=today).aggregate(Sum('total'))['total__sum'] or 0
    weekly_sales = Sale.objects.filter(timestamp__gte=week_ago).aggregate(Sum('total'))['total__sum'] or 0
    monthly_sales = Sale.objects.filter(timestamp__gte=month_ago).aggregate(Sum('total'))['total__sum'] or 0
    
    daily_count = Sale.objects.filter(timestamp__date=today).count()
    
    low_stock_products = Product.objects.filter(stock__lte=10)

    context = {
        'daily_sales': daily_sales,
        'daily_count': daily_count,
        'weekly_sales': weekly_sales,
        'monthly_sales': monthly_sales,
        'low_stock_products': low_stock_products,
    }
    return render(request, 'dashboard.html', context)


def sales_entry(request):
    """Sales entry form page."""
    products = Product.objects.all()
    categories = dict(Product.CATEGORY_CHOICES)
    
    grouped_products = {}
    for cat_key, cat_name in Product.CATEGORY_CHOICES:
        products_in_cat = Product.objects.filter(category=cat_key)
        if products_in_cat.exists():
            grouped_products[cat_name] = products_in_cat

    context = {
        'grouped_products': grouped_products,
        'products': products,
    }
    return render(request, 'sales_entry.html', context)


@require_POST
def add_sale(request):
    """Add a sale via AJAX - supports single item or multiple items."""
    try:
        data = json.loads(request.body)
        
        # Check if it's a single item or multiple items
        if 'items' in data:
            # Multiple items
            items = data['items']
            total_sale_amount = 0
            sale_records = []
            
            for item in items:
                product_id = item.get('product_id')
                size = item.get('size')
                quantity = int(item.get('quantity', 1))
                price = float(item.get('price'))

                product = get_object_or_404(Product, id=product_id)
                total = quantity * price

                # Deduct stock
                product.stock -= quantity
                if product.stock < 0:
                    product.stock = 0
                product.save()

                # Create sale record
                sale = Sale.objects.create(
                    product=product,
                    size=size,
                    quantity=quantity,
                    price=price,
                    total=total
                )
                
                sale_records.append(sale)
                total_sale_amount += total
            
            return JsonResponse({
                'success': True,
                'message': f'Order completed: {len(items)} items - ₱{total_sale_amount}',
                'sale_ids': [sale.id for sale in sale_records],
                'total_amount': total_sale_amount
            })
        else:
            # Single item (backward compatibility)
            product_id = data.get('product_id')
            size = data.get('size')
            quantity = int(data.get('quantity', 1))
            price = float(data.get('price'))

            product = get_object_or_404(Product, id=product_id)
            total = quantity * price

            # Deduct stock
            product.stock -= quantity
            if product.stock < 0:
                product.stock = 0
            product.save()

            # Create sale record
            sale = Sale.objects.create(
                product=product,
                size=size,
                quantity=quantity,
                price=price,
                total=total
            )

            return JsonResponse({
                'success': True,
                'message': f'Sale added: {product.name} x{quantity} - ₱{total}',
                'sale_id': sale.id,
                'remaining_stock': product.stock
            })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


def get_product_price(request, product_id, size=None):
    """Get product price based on size."""
    try:
        product = get_object_or_404(Product, id=product_id)
        price = None

        if size == '12oz':
            price = product.price_12oz
        elif size == '16oz':
            price = product.price_16oz
        elif size == '22oz':
            price = product.price_22oz
        else:
            price = product.price_single

        return JsonResponse({
            'success': True,
            'price': float(price) if price else 0,
            'stock': product.stock
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


def inventory(request):
    """Inventory management page."""
    products = Product.objects.all()
    low_stock = products.filter(stock__lte=10)
    
    context = {
        'products': products,
        'low_stock_count': low_stock.count(),
    }
    return render(request, 'inventory.html', context)


@require_POST
def restock(request):
    """Restock inventory."""
    try:
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = int(data.get('quantity', 0))

        product = get_object_or_404(Product, id=product_id)
        product.stock += quantity
        product.save()

        return JsonResponse({
            'success': True,
            'message': f'Restocked {product.name} +{quantity}',
            'new_stock': product.stock
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


def sales_history(request):
    """View sales history."""
    sales = Sale.objects.all().order_by('-timestamp')[:100]
    
    context = {
        'sales': sales,
    }
    return render(request, 'sales_history.html', context)
