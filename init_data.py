"""
Script to populate database with all milk tea shop products.
Run after: python manage.py migrate
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from tea_shop.models import Product, Inventory, Sale

# Clear existing data
Sale.objects.all().delete()  # Delete sales first due to foreign key protection
Product.objects.all().delete()

products_data = [
    # Classic Milk Tea (16oz/22oz)
    ('Taro', 'classic_milk_tea', None, 29, 39),
    ('Wintermelon', 'classic_milk_tea', None, 29, 39),
    ('Cookies & Cream', 'classic_milk_tea', None, 29, 39),
    ('Okinawa', 'classic_milk_tea', None, 29, 39),
    ('Mango Cheesecake', 'classic_milk_tea', None, 29, 39),
    
    # Premium Milk Tea (16oz/22oz)
    ('Red Velvet', 'premium_milk_tea', None, 35, 45),
    ('Caramel Sugar', 'premium_milk_tea', None, 35, 45),
    ('Matcha', 'premium_milk_tea', None, 35, 45),
    ('Chocolate', 'premium_milk_tea', None, 35, 45),
    
    # Milkshakes (16oz/22oz)
    ('Mango', 'milkshakes', None, 35, 45),
    ('Strawberry', 'milkshakes', None, 35, 45),
    ('Avocado', 'milkshakes', None, 35, 45),
    ('Rocky Road', 'milkshakes', None, 35, 45),
    
    # Special Milkshakes (16oz/22oz)
    ('Mango Graham Shake', 'special_milkshakes', None, 50, 65),
    ('Avocado Oreo', 'special_milkshakes', None, 50, 65),
    
    # Sundaes (single prices)
    ('Blueberry Sundae', 'sundaes', None, None, None, 35),
    ('Chocolate Sundae', 'sundaes', None, None, None, 35),
    ('Caramel Sundae', 'sundaes', None, None, None, 35),
    ('Strawberry Sundae', 'sundaes', None, None, None, 35),
    
    # Floats (single prices)
    ('Choco Float', 'floats', None, None, None, 49),
    ('Milo Float', 'floats', None, None, None, 49),
    ('Coffee Float', 'floats', None, None, None, 49),
    ('Coke Float', 'floats', None, None, None, 49),
    ('Chuckie Float', 'floats', None, None, None, 55),

    # Combo Meals (single prices)
    ('Combo 1 - Classic Milk Tea with Siopao', 'combo_meals', None, None, None, 65),
    ('Combo 2 - Coke Float with Siopao', 'combo_meals', None, None, None, 75),
    ('Combo 3 - Classic Milk Tea with Burger', 'combo_meals', None, None, None, 65),
    ('Combo 4 - Coke Float with Burger', 'combo_meals', None, None, None, 75),
    ('Combo 5 - Milk Tea with Fries', 'combo_meals', None, None, None, 79),
    ('Combo 6 - Coke Float with Fries', 'combo_meals', None, None, None, 89),
    
    # Fruit Soda with Nata (12oz/16oz/22oz)
    ('Lychee Fruit Soda with Nata', 'fruit_soda', 29, 39, 49),
    ('Strawberry Fruit Soda with Nata', 'fruit_soda', 29, 39, 49),
    ('Green Apple Fruit Soda with Nata', 'fruit_soda', 29, 39, 49),
    ('Blueberry Fruit Soda with Nata', 'fruit_soda', 29, 39, 49),
    
    # Fruit Soda Floats (16oz)
    ('Lychee Fruit Soda Float', 'fruit_soda_floats', None, 49, None),
    ('Strawberry Fruit Soda Float', 'fruit_soda_floats', None, 49, None),
    ('Green Apple Fruit Soda Float', 'fruit_soda_floats', None, 49, None),
    ('Blueberry Fruit Soda Float', 'fruit_soda_floats', None, 49, None),
    
    # Ice Cream (single prices)
    ('Ice Cream Small', 'ice_cream', None, None, None, 15),
    ('Ice Cream Large', 'ice_cream', None, None, None, 25),
    
    # Iced Coffee (keeping existing)
    ('Iced Coffee', 'iced_coffee', 29, 39, 49),
    
    # Burgers (keeping existing)
    ('Burger Plain', 'burgers', None, None, None, 25),
    ('Burger w/ Cheese', 'burgers', None, None, None, 35),
    ('Chicken Burger', 'burgers', None, None, None, 45),
    
    # Fries (keeping existing)
    ('Fries Solo', 'fries', None, None, None, 25),
    ('Fries Duo', 'fries', None, None, None, 49),
    ('Fries Group', 'fries', None, None, None, 99),
    
    # Rice Meals (keeping existing)
    ('Hungarian Sausage 65', 'rice_meals', None, None, None, 65),
    ('Burger Steak 1pc', 'rice_meals', None, None, None, 45),
    ('Burger Steak 2pcs', 'rice_meals', None, None, None, 65),
    ('Chicken Fillet(1pc)', 'rice_meals', None, None, None, 45),
    ('Chicken Fillet(2pcs)', 'rice_meals', None, None, None, 75),
    ('Siomai Rice', 'rice_meals', None, None, None, 45),
    ('Shanghai Rice', 'rice_meals', None, None, None, 45),
    ('Chicken Pops', 'rice_meals', None, None, None, 45),
    
    # Siopao (keeping existing)
    ('Siopao Small', 'siopao', None, None, None, 15),
    ('Siopao Big', 'siopao', None, None, None, 30),
]

# Create products with proper pricing
for item in products_data:
    name = item[0]
    category = item[1]
    
    # Handle different price structures
    if category in ['classic_milk_tea', 'premium_milk_tea', 'milkshakes', 'special_milkshakes']:
        # 16oz/22oz format: (name, category, None, price_16oz, price_22oz)
        price_12oz = None
        price_16oz = item[3]
        price_22oz = item[4]
        price_single = None
    elif category == 'fruit_soda':
        # 12oz/16oz/22oz format: (name, category, price_12oz, price_16oz, price_22oz)
        price_12oz = item[2]
        price_16oz = item[3]
        price_22oz = item[4]
        price_single = None
    elif category == 'fruit_soda_floats':
        # 16oz only: (name, category, None, price_16oz, None)
        price_12oz = None
        price_16oz = item[3]
        price_22oz = None
        price_single = None
    elif category in ['sundaes', 'floats', 'combo_meals', 'ice_cream', 'burgers', 'fries', 'rice_meals', 'siopao']:
        # Single price: (name, category, None, None, None, price_single)
        price_12oz = None
        price_16oz = None
        price_22oz = None
        price_single = item[5]
    else:
        # Default for iced_coffee: 12oz/16oz/22oz
        price_12oz = item[2]
        price_16oz = item[3]
        price_22oz = item[4]
        price_single = None
    
    product = Product.objects.create(
        name=name,
        category=category,
        price_16oz=price_16oz,
        price_22oz=price_22oz,
        price_12oz=price_12oz,
        price_single=price_single,
        stock=999,
        low_stock_alert=10
    )
    
    # Create inventory record
    Inventory.objects.create(
        product=product,
        current_stock=999
    )
    
    print(f'✓ Created: {name}')

print('\n✓ All products imported successfully!')
print(f'Total products: {Product.objects.count()}')
