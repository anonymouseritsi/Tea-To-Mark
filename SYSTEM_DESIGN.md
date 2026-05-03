# Tea Shop Manager - Complete System Documentation

## PROJECT STRUCTURE

```
milk_tea_shop/
├── manage.py                          # Django management script
├── db.sqlite3                         # Database (created after migrate)
├── requirements.txt                   # Python dependencies
├── README.md                          # Quick start guide
├── init_data.py                       # Product data initialization
├── SYSTEM_DESIGN.md                   # This file
│
├── config/                            # Django project settings
│   ├── __init__.py
│   ├── settings.py                    # Configuration, allowed apps
│   ├── urls.py                        # Main URL routing
│   └── wsgi.py                        # WSGI application
│
└── tea_shop/                          # Main Django app
    ├── migrations/                    # Database migrations (auto-generated)
    ├── __init__.py
    ├── apps.py                        # App configuration
    ├── models.py                      # Database models
    ├── views.py                       # View logic (handles requests)
    ├── urls.py                        # App URL routing
    ├── admin.py                       # Django admin configuration
    │
    ├── static/                        # Static files (CSS, JS)
    │   ├── css/
    │   │   └── style.css              # Mobile-first responsive styling
    │   └── js/
    │       └── app.js                 # JavaScript utilities
    │
    └── templates/                     # HTML templates
        ├── base.html                  # Base template with header/nav
        ├── dashboard.html             # Main dashboard with stats
        ├── sales_entry.html           # Sales form (MOST IMPORTANT)
        ├── inventory.html             # Inventory management
        └── sales_history.html         # Sales records view
```

---

## DATABASE DESIGN

### ER Diagram
```
┌─────────────┐         1:N         ┌────────────┐
│  Product    │──────────────────────│   Sale     │
│             │                      │            │
├─────────────┤                      ├────────────┤
│ id (PK)     │                      │ id (PK)    │
│ name        │                      │ product_id │
│ category    │◄───────────────────┤ (FK)       │
│ price_16oz  │       1:1            │ size       │
│ price_22oz  │     ┌──────────────┤ quantity   │
│ price_12oz  │─────│────────┐     │ price      │
│ price_single│     │        │     │ total      │
│ stock       │     │    ┌────────┤ timestamp  │
│ low_stock..│     │    │  └─────┤            │
│ created_at  │     │    │        │            │
└─────────────┘     │    │        └────────────┘
                    │    │
                    │ ┌──┴──────────┐
                    │ │  Inventory  │
                    │ │             │
                    │ ├─────────────┤
                    │ │ id (PK)     │
                    └─┤ product_id  │
                      │ (FK)        │
                      │ current_..  │
                      │ last_..     │
                      └─────────────┘
```

### Table Details

#### PRODUCT Table
```sql
CREATE TABLE tea_shop_product (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(20) NOT NULL,
    price_16oz DECIMAL(6,2) NULL,
    price_22oz DECIMAL(6,2) NULL,
    price_12oz DECIMAL(6,2) NULL,
    price_single DECIMAL(6,2) NULL,
    stock INTEGER DEFAULT 999,
    low_stock_alert INTEGER DEFAULT 10,
    created_at DATETIME AUTO_NOW_ADD
);

-- Sample Data:
| id | name          | category          | price_16oz | price_22oz |
|----|---------------|-------------------|------------|------------|
| 1  | Taro          | classic_milk_tea  | 29         | 39         |
| 2  | Red Velvet    | premium_milk_tea  | 35         | 45         |
| 16 | Regular Sundae| sundaes           | NULL       | NULL       |
```

#### SALE Table
```sql
CREATE TABLE tea_shop_sale (
    id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL (FK),
    size VARCHAR(10),
    quantity INTEGER DEFAULT 1,
    price DECIMAL(6,2) NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    timestamp DATETIME AUTO_NOW_ADD
);

-- Sample Data:
| id | product_id | size  | quantity | price | total | timestamp           |
|----|------------|-------|----------|-------|-------|---------------------|
| 1  | 1          | 16oz  | 2        | 29    | 58    | 2024-05-03 10:15:00 |
| 2  | 6          | 22oz  | 1        | 45    | 45    | 2024-05-03 10:20:00 |
| 3  | 16         | NULL  | 1        | 35    | 35    | 2024-05-03 10:25:00 |
```

#### INVENTORY Table
```sql
CREATE TABLE tea_shop_inventory (
    id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL UNIQUE (FK),
    current_stock INTEGER,
    last_restock DATETIME NULL
);

-- Sample Data:
| id | product_id | current_stock | last_restock        |
|----|------------|---------------|---------------------|
| 1  | 1          | 997           | 2024-05-03 09:00:00 |
| 2  | 2          | 1000          | NULL                |
```

---

## WORKFLOW LOGIC

### 1. Adding a Sale (MOST CRITICAL)
```
User clicks "💰 Sales"
    ↓
Page loads with product categories
    ↓
User selects product
    ↓
JavaScript fetches price from /api/product-price/<id>/
    ↓
User selects size (if applicable)
    ↓
Auto price update based on size
    ↓
User sets quantity (with +/- buttons)
    ↓
Total = Price × Quantity (auto-calculated)
    ↓
User clicks "✓ Save Sale"
    ↓
AJAX POST to /api/add-sale/
    ↓
Backend:
  - Creates Sale record
  - Deducts from Product.stock
  - Returns success/error
    ↓
Frontend:
  - Shows success message
  - Adds to "Recent Sales" list
  - Clears form for next sale
    ↓
Database updated
```

### 2. Stock Management
```
Initial Stock = 999 (set in init_data.py)
    ↓
Customer buys 2 items
    ↓
Product.stock -= 2 → 997
    ↓
If stock <= 10 → Low stock alert shown
    ↓
Manager goes to 📦 Inventory
    ↓
Enters quantity to restock
    ↓
Clicks "Restock" → POST to /api/restock/
    ↓
Backend adds to Product.stock
    ↓
Alert clears (stock now > 10)
```

### 3. Dashboard Calculations
```
Daily Sales: SUM(total) WHERE DATE(timestamp) = TODAY
Weekly Sales: SUM(total) WHERE timestamp >= NOW - 7 DAYS
Monthly Sales: SUM(total) WHERE timestamp >= NOW - 30 DAYS
Daily Count: COUNT(*) WHERE DATE(timestamp) = TODAY
Low Stock: Product WHERE stock <= low_stock_alert
```

---

## API ENDPOINTS

### Views/URLs
```
GET  /                           → dashboard (stats & overview)
GET  /sales/                     → sales_entry (sales form page)
POST /api/add-sale/              → add_sale (create new sale)
GET  /api/product-price/<id>/    → get_product_price (fetch price by size)
POST /api/restock/               → restock (increase stock)
GET  /inventory/                 → inventory (restock page)
GET  /history/                   → sales_history (sales records)
GET  /admin/                     → Django admin panel
```

---

## KEY DESIGN DECISIONS

1. **Mobile-First CSS**
   - Optimized for phone screens
   - Touch-friendly buttons (40px minimum)
   - Horizontal scrolling for small screens
   - Responsive grid for larger devices

2. **Fast "Add Sale" Interface**
   - Dropdown product selection (no search needed for small catalog)
   - Auto price calculation (no manual entry)
   - +/- buttons instead of keyboard entry
   - Instant visual feedback

3. **Local Database (SQLite)**
   - No external server required
   - Single file database (db.sqlite3)
   - Persists across restarts
   - Suitable for solo shop owner

4. **Auto-Deducting Stock**
   - Stock decreases immediately after sale
   - No manual inventory adjustment needed
   - Prevents overselling

5. **Simple Categorization**
   - Products grouped by category in dropdown
   - Category icons for visual recognition
   - Makes selection faster during rush

6. **Low Stock Alerts**
   - Configurable per product (default: 10)
   - Dashboard warning badge
   - Yellow highlight on inventory page

---

## FEATURE BREAKDOWN

### ✓ Sales Entry (PRIORITY 1)
- [x] Categorized product dropdown
- [x] Size selection (16oz/22oz/12oz/solo/regular/etc)
- [x] Auto price based on product+size
- [x] Quantity with +/- buttons
- [x] Auto total calculation
- [x] Save sale button
- [x] Recent sales display
- [x] Auto stock deduction

### ✓ Inventory (PRIORITY 2)
- [x] View all products & stock levels
- [x] Low stock visual indicator
- [x] Manual restock input+button
- [x] Stock count updates

### ✓ Dashboard (PRIORITY 3)
- [x] Daily sales total
- [x] Weekly sales total
- [x] Monthly sales total
- [x] Item count today
- [x] Low stock alerts
- [x] Quick action buttons

### ✓ Sales History (PRIORITY 4)
- [x] View all transactions
- [x] Product name, size, quantity
- [x] Price per item & total
- [x] Timestamp
- [x] Last 100 records

### ✓ Admin Panel
- [x] Edit products
- [x] View/filter sales
- [x] Manage inventory
- [x] Backup database

---

## PERFORMANCE CONSIDERATIONS

1. **Database Queries**
   - All queries indexed on important fields
   - Sales aggregation uses database SUM (fast)
   - Pagination not needed for small catalog

2. **Frontend**
   - All JavaScript < 200 lines
   - No heavy frameworks
   - CSS uses native flexbox (no preprocessor)
   - Images: emoji only (no HTTP requests)

3. **Scalability**
   - Can handle 50+ products
   - SQLite supports thousands of daily sales
   - No external APIs or dependencies

---

## DATA BACKUP

### Manual Backup
```bash
# Copy database file
copy db.sqlite3 db_backup_2024-05-03.sqlite3
```

### Automatic via Admin
1. Go to http://localhost:8000/admin
2. Click "Sales" or "Products"
3. Use Django's export features

---

## FUTURE ENHANCEMENTS

- Monthly reports PDF
- Employee login tracking
- Expense tracking
- Product edit interface
- Cloud backup integration
- Multi-user support
- Receipt printer integration

---

## TROUBLESHOOTING

### No products showing
→ Run `python init_data.py`

### Stock not deducting
→ Check sales_entry.html JavaScript for POST errors

### Page slow
→ Check db.sqlite3 size (backup and clear old sales)

### Can't access admin
→ Run `python manage.py createsuperuser` and set credentials
