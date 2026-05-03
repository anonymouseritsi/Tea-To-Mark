# Tea Shop Manager - Complete Package Documentation

## 📋 QUICK REFERENCE

### What You Have
A **complete mobile-friendly web app** for inventory and sales tracking at your milk tea shop.

### What It Does
✅ Tracks sales in real-time  
✅ Deducts stock automatically  
✅ Shows daily/weekly/monthly totals  
✅ Alerts when stock is low  
✅ Responsive on phone, tablet, computer  

### What You Need
- Python 3.8+ installed
- Internet (first setup only)
- Any web browser

### To Get Started
```bash
cd milk_tea_shop
pip install -r requirements.txt
python manage.py migrate
python init_data.py
python manage.py runserver
# Open browser: http://localhost:8000
```

---

## 📁 FILE STRUCTURE & PURPOSES

```
milk_tea_shop/
│
├── 🚀 START HERE →
│   ├── README.md               Quick start (5 min read)
│   ├── SETUP_GUIDE.md          Detailed setup instructions
│   └── SYSTEM_DESIGN.md        Technical documentation
│
├── 💾 DATABASE
│   └── db.sqlite3              All your data (created after migrate)
│
├── ⚙️ CONFIGURATION
│   ├── manage.py               Django command tool
│   ├── requirements.txt        Python packages
│   ├── init_data.py            Product data loader
│   │
│   └── config/
│       ├── settings.py         Main settings
│       ├── urls.py             URL routing
│       └── wsgi.py             Server interface
│
├── 🎨 USER INTERFACE
│   ├── tea_shop/templates/
│   │   ├── base.html           Master layout (header, nav)
│   │   ├── dashboard.html      Stats & overview
│   │   ├── sales_entry.html    SALES FORM (most important!)
│   │   ├── inventory.html      Stock management
│   │   └── sales_history.html  Transaction records
│   │
│   └── tea_shop/static/
│       ├── css/style.css       Mobile-first styling (800+ lines)
│       └── js/app.js           JavaScript utilities
│
└── 🔧 APPLICATION LOGIC
    └── tea_shop/
        ├── models.py           Database structure (Product, Sale, Inventory)
        ├── views.py            Page logic (dashboards, forms, APIs)
        ├── urls.py             Routes to pages
        └── admin.py            Django admin interface
```

---

## 📊 DATABASE SCHEMA

### Product Table
```
Taro Milk Tea (Classic)
├── 16oz: ₱29
├── 22oz: ₱39
└── Stock: 999 (auto-updates)

Red Velvet (Premium)
├── 16oz: ₱35
├── 22oz: ₱45
└── Stock: 999

Regular Sundae
├── Price: ₱35
└── Stock: 999

[All 33 products follow this pattern]
```

### Sale Table
```
Each sale records:
✓ Which product was sold
✓ What size (if applicable)
✓ How many units
✓ Price per unit
✓ Total amount
✓ Exact timestamp
```

### Inventory Table
```
Linked to each Product:
✓ Current stock count
✓ Last restock time
✓ Auto-updated on each sale
```

---

## 🎯 MAIN FEATURES DETAILED

### 1. ADD SALE (Most Important)
```
Dashboard → 💰 SALES
    ↓
Choose product from dropdown (categorized)
    ↓
Select size (if applicable)
    ↓
Price auto-fills based on product + size
    ↓
Adjust quantity with +/- buttons
    ↓
Total shows: Price × Quantity
    ↓
Click "✓ Save Sale"
    ↓
✓ Stock deducts automatically
✓ Sale saved with timestamp
✓ Recent sales shown below
✓ Reset for next customer
```

### 2. INVENTORY MANAGEMENT
```
Dashboard → 📦 INVENTORY
    ↓
See all products + current stock
    ↓
Low stock items highlighted (≤10 units)
    ↓
Enter restock quantity
    ↓
Click "Restock"
    ↓
✓ Stock updated
✓ Alert clears if stock > 10
```

### 3. DASHBOARD
```
Navigate to 📊 DASHBOARD
    ↓
See:
- Today's total sales (₱)
- Items sold today (count)
- Weekly total (last 7 days)
- Monthly total (last 30 days)
- Low stock alerts (if any)
    ↓
Quick buttons:
💰 Add Sale
📦 Restock
```

### 4. SALES HISTORY
```
Click → 📋 HISTORY
    ↓
View last 100 transactions:
✓ Product name
✓ Size
✓ Quantity sold
✓ Price per unit
✓ Total amount
✓ Exact time
```

---

## 📱 MOBILE EXPERIENCE

The app is optimized for phone use during selling:

✅ **Large buttons** - Easy to tap with finger  
✅ **Categorized dropdown** - No scrolling through 100 items  
✅ **Auto calculations** - No manual math  
✅ **Vertical layout** - Fits phone screen  
✅ **Touch-friendly** - 40px+ tap targets  
✅ **Fast loading** - No server delays  
✅ **Works offline** - All data local (after first load)  

### Responsive Grid
- **Phone (360px):** Single column, stacked buttons
- **Tablet (768px):** 2-3 column layout
- **Desktop:** Full 3-column stats

---

## 💾 ALL PRODUCTS LOADED

**Total: 33 Products in 12 Categories**

### 🧊 Classic Milk Tea (5 flavors)
- Taro (16oz ₱29 | 22oz ₱39)
- Wintermelon (16oz ₱29 | 22oz ₱39)
- Cookies & Cream (16oz ₱29 | 22oz ₱39)
- Okinawa (16oz ₱29 | 22oz ₱39)
- Hokkaido (16oz ₱29 | 22oz ₱39)

### ⭐ Premium Milk Tea (4 flavors)
- Red Velvet (16oz ₱35 | 22oz ₱45)
- Brown Sugar (16oz ₱35 | 22oz ₱45)
- Matcha (16oz ₱35 | 22oz ₱45)
- Chocolate (16oz ₱35 | 22oz ₱45)

### 🥤 Milkshakes (4 flavors)
- Mango (16oz ₱35 | 22oz ₱45)
- Strawberry (16oz ₱35 | 22oz ₱45)
- Avocado (16oz ₱35 | 22oz ₱45)
- Chocolate (16oz ₱35 | 22oz ₱45)

### 🌟 Special Milkshakes (2 flavors)
- Oreo (16oz ₱50 | 22oz ₱65)
- Avocado Oreo (16oz ₱50 | 22oz ₱65)

### 🍨 Sundaes (3 types)
- Regular (₱35)
- Special (₱40)
- Premium (₱50)

### 🥤 Floats (1 item)
- All Floats (₱49)

### 🍹 Fruit Soda with Nata (Multiple Sizes)
- 12oz (₱29)
- 16oz (₱39)
- 22oz (₱49)

### ☕ Iced Coffee (Multiple Sizes)
- 12oz (₱29)
- 16oz (₱39)
- 22oz (₱49)

### 🍔 Burgers (3 types)
- Solo (₱25)
- w/ Cheese (₱35)
- w/ Egg (₱45)

### 🍟 Fries (3 sizes)
- Solo (₱25)
- Duo (₱49)
- Group (₱99)

### 🍚 Rice Meals (4 types)
- Hungarian Sausage (₱45)
- Pork Steak (₱45)
- Chicken Fillet Small (₱45)
- Chicken Fillet Large (₱75)

### 🥟 Siopao (2 sizes)
- Small (₱15)
- Big (₱30)

---

## 🔐 DATA SECURITY & BACKUP

### Your Database
- Single file: `db.sqlite3`
- Contains ALL your data
- About 50KB when new, grows with use

### Backup (Every Week)
```bash
copy db.sqlite3 db_backup_2024-05-03.sqlite3
```

### Restore
```bash
copy db_backup_2024-05-03.sqlite3 db.sqlite3
python manage.py runserver
```

### Emergency Reset
```bash
del db.sqlite3
python manage.py migrate
python init_data.py
```
⚠️ This erases all sales history!

---

## 🛠️ TECHNICAL STACK

| Component | Technology | Why |
|-----------|-----------|-----|
| Backend | Django 5.0.1 | Fast, secure, built-in admin |
| Database | SQLite3 | Local, single file, no setup |
| Frontend | HTML5 + CSS3 | Fast, no build tools needed |
| JavaScript | Vanilla (no framework) | Lightweight, no dependencies |
| Styling | CSS Grid + Flexbox | Responsive, modern browsers |

### No External Dependencies
- ✅ No JavaScript libraries (no jQuery, React, Vue)
- ✅ No CSS framework (no Bootstrap)
- ✅ No external API calls
- ✅ All processing local

---

## 📊 USAGE STATISTICS TRACKED

### Real-Time Tracking
✓ Sales count per transaction  
✓ Amount per transaction  
✓ Timestamp of sale  
✓ Stock before/after  
✓ Product category  

### Auto Calculations
- Daily total: SUM of all sales today
- Weekly total: SUM of sales last 7 days
- Monthly total: SUM of sales last 30 days
- Low stock: Products with stock ≤ 10
- Daily count: Number of transactions today

### Reports Available
- Last 100 transactions (Sales History)
- Stock levels by product (Inventory)
- Sales by time period (Dashboard)
- Category breakdown (Admin panel)

---

## 🌐 ACCESSING FROM PHONE

### On Same WiFi Network

1. **Get computer IP:**
   ```bash
   ipconfig
   # Look for IPv4 Address like: 192.168.1.5
   ```

2. **Start app with network binding:**
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

3. **On phone browser, type:**
   ```
   http://192.168.1.5:8000
   ```

4. **Bookmarks on phone** for quick access during selling

---

## 🚨 TROUBLESHOOTING MATRIX

| Problem | Cause | Solution |
|---------|-------|----------|
| No products visible | Data not loaded | `python init_data.py` |
| Can't add sale | JavaScript error | Refresh page (Ctrl+Shift+R) |
| Stock not deducting | Server error | Check browser console (F12) |
| Can't see from phone | Network issue | Use correct IP address |
| Slow page load | Too many sales | Backup & reset database |
| Page looks broken | Browser cache | Clear cache or use Incognito |
| "Port in use" | Server already running | Stop server or use `runserver 8001` |

---

## 📞 FILE LOCATIONS

### Windows
```
C:\Users\admin\Desktop\Tea To Mark\milk_tea_shop\
├── db.sqlite3              ← YOUR DATA
├── manage.py               ← RUN COMMANDS
└── tea_shop\ folders...
```

### Backup Location
```
C:\Users\admin\Desktop\Tea To Mark\milk_tea_shop\
└── db_backup_2024-05-03.sqlite3
```

---

## 🎓 LEARNING THE CODEBASE

### If You Want to Modify:

1. **Add New Fields to Products**
   - Edit: `tea_shop/models.py` → `Product` class
   - Run: `python manage.py makemigrations`
   - Run: `python manage.py migrate`

2. **Change Colors/Fonts**
   - Edit: `tea_shop/static/css/style.css`
   - No server restart needed, just refresh browser

3. **Add New Page**
   - Create template: `tea_shop/templates/newpage.html`
   - Add view: `tea_shop/views.py` → new function
   - Add route: `tea_shop/urls.py` → new path
   - Add nav link: `base.html`

4. **Change Admin Settings**
   - Edit: `config/settings.py`
   - Restart server

---

## 🎉 YOU'RE READY!

Your tea shop manager is fully built and ready to use.

### Next Steps:
1. Follow `README.md` for quick start
2. Run the initial setup commands
3. Open http://localhost:8000
4. Start tracking sales!

### Remember:
- Your data is in `db.sqlite3`
- Backup regularly
- Admin panel at `/admin` for deep edits
- All sales history is permanent

### Support:
- Check `SYSTEM_DESIGN.md` for technical details
- Check `SETUP_GUIDE.md` for troubleshooting
- All code is commented and readable

---

**🧋 Happy Selling!**

For questions, refer to appropriate guide:
- **Quick Start:** README.md
- **Setup Issues:** SETUP_GUIDE.md  
- **How It Works:** SYSTEM_DESIGN.md
- **Code Details:** Check comments in `tea_shop/*.py` and `templates/*.html`

**Version:** 1.0 Complete  
**Date:** May 3, 2024  
**Status:** Production Ready ✅

---

## CHECKLIST BEFORE USING

- [ ] Python 3.8+ installed and working
- [ ] `pip install -r requirements.txt` completed
- [ ] `python manage.py migrate` completed
- [ ] `python init_data.py` completed (33 products loaded)
- [ ] Server starts with `python manage.py runserver`
- [ ] Browser opens to http://localhost:8000 without error
- [ ] All 4 navigation tabs visible (Dashboard, Sales, Inventory, History)
- [ ] Product dropdown shows 33 items
- [ ] Data saves after adding a sale

Once all ✅, you're ready to start tracking sales!
