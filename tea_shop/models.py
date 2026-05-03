from django.db import models
from django.utils import timezone
from datetime import timedelta


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('classic_milk_tea', '🧊 Classic Milk Tea'),
        ('premium_milk_tea', '⭐ Premium Milk Tea'),
        ('milkshakes', '🥤 Milkshakes'),
        ('special_milkshakes', '🌟 Special Milkshakes'),
        ('sundaes', '🍨 Sundaes'),
        ('floats', '🥤 Floats'),
        ('combo_meals', '🍱 Combo Meals'),
        ('fruit_soda', '🍹 Fruit Soda with Nata'),
        ('fruit_soda_floats', '🍹 Fruit Soda Floats'),
        ('ice_cream', '🍦 Ice Cream'),
        ('iced_coffee', '☕ Iced Coffee'),
        ('burgers', '🍔 Burgers'),
        ('fries', '🍟 Fries'),
        ('rice_meals', '🍚 Rice Meals'),
        ('siopao', '🥟 Siopao'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price_16oz = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price_22oz = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price_12oz = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price_single = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(default=999)
    low_stock_alert = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    size = models.CharField(max_length=10, choices=[
        ('12oz', '12oz'),
        ('16oz', '16oz'),
        ('22oz', '22oz'),
        ('solo', 'Solo'),
        ('duo', 'Duo'),
        ('group', 'Group'),
        ('small', 'Small'),
        ('big', 'Big'),
        ('regular', 'Regular'),
        ('special', 'Special'),
        ('premium', 'Premium'),
        ('single', 'Single'),
    ], null=True, blank=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} x{self.quantity} - ₱{self.total}"


class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='inventory')
    current_stock = models.IntegerField()
    last_restock = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Inventories'

    def __str__(self):
        return f"{self.product.name} - Stock: {self.current_stock}"
