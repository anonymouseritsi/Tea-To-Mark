# Tea Shop Manager - Milk Tea Inventory & Sales Tracker

## Quick Start Guide

### System Requirements
- Python 3.8+
- Windows, Mac, or Linux

### Installation

1. **Extract the project** to your desired location

2. **Install Python packages:**
   ```
   pip install -r requirements.txt
   ```

3. **Initialize the database:**
   ```
   python manage.py migrate
   ```

4. **Load product data:**
   ```
   python init_data.py
   ```

5. **Create admin account (optional, for data management):**
   ```
   python manage.py createsuperuser
   ```

6. **Start the server:**
   ```
   python manage.py runserver
   ```

7. **Open in browser:**
   - Main app: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

### Usage

#### Dashboard (Home)
- View today's, weekly, and monthly sales totals
- See number of items sold today
- Get low stock alerts
- Quick access to Sales and Restock buttons

#### Add Sale (💰 Sales)
- Select product from categorized dropdown
- Choose size if applicable
- Quantity adjusts with +/- buttons
- Price auto-calculates
- Total shows before saving
- Stock auto-deducts after sale
- View recent sales on same page

#### Inventory (📦 Inventory)
- View all products and current stock levels
- Low stock items highlighted in yellow
- Quick restock with input field and button
- See low stock count at top

#### Sales History (📋 History)
- View last 100 sales transactions
- See product name, size, quantity, and price
- Timestamp for each sale

#### Admin Panel
- Full product management
- Sales record viewing
- Inventory management
- Create backup of data

### Product Categories
- 🧊 Classic Milk Tea (16oz/22oz)
- ⭐ Premium Milk Tea (16oz/22oz)
- 🥤 Milkshakes (16oz/22oz)
- 🌟 Special Milkshakes (16oz/22oz)
- 🍨 Sundaes (Regular/Special/Premium)
- 🥤 Floats (all sizes)
- 🍹 Fruit Soda with Nata (12oz/16oz/22oz)
- ☕ Iced Coffee (12oz/16oz/22oz)
- 🍔 Burgers (Solo/Cheese/Egg)
- 🍟 Fries (Solo/Duo/Group)
- 🍚 Rice Meals (4 options)
- 🥟 Siopao (Small/Big)

### Database Structure

**Products Table:**
- ID, Name, Category, Price (multiple sizes), Stock, Low Stock Alert

**Sales Table:**
- ID, Product ID, Size, Quantity, Price, Total, Timestamp

**Inventory Table:**
- ID, Product ID, Current Stock, Last Restock Date

### Features

✓ Mobile-friendly interface optimized for phone use
✓ Auto price calculation based on product & size
✓ Real-time stock deduction after each sale
✓ Daily, weekly, monthly sales tracking
✓ Low stock alerts
✓ Sales history with timestamps
✓ Quick restock interface
✓ All data persists in SQLite database
✓ Responsive design works on tablets too

### Tips
- Load the page on your phone browser for best experience
- Use the Dashboard for quick sales overview
- Always check low stock alerts before running out
- Sales History shows recent 100 transactions
- Admin panel at /admin for detailed management

### Troubleshooting

**Port already in use:**
```
python manage.py runserver 8001
```

**Database issues:**
```
rm db.sqlite3
python manage.py migrate
python init_data.py
```

**Missing products:**
Run `python init_data.py` again

For support, check that all files are in correct folders as shown in the project structure.
