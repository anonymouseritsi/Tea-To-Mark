#!/usr/bin/env python
import os
import sys

# Add the project directory to the path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Import Django and setup
import django
django.setup()

# Import your models and run the data initialization
from tea_shop.models import Product

def initialize_data():
    """Initialize the database with product data"""
    if Product.objects.count() == 0:
        # Import and run your init_data.py logic here
        from init_data import products_data

        for product_data in products_data:
            Product.objects.create(
                name=product_data[0],
                category=product_data[1],
                price_12oz=product_data[2],
                price_16oz=product_data[3],
                price_22oz=product_data[4],
                price_single=product_data[5]
            )
        print("Database initialized with product data")
    else:
        print("Database already contains data")

if __name__ == '__main__':
    initialize_data()