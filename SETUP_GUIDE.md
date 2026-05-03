# Tea Shop Manager - Setup & Deployment Guide

## STEP-BY-STEP SETUP

### Prerequisites
- Python 3.8 or higher installed
- Internet connection (first time setup)

### Step 1: Install Python Dependencies
```bash
cd milk_tea_shop
pip install -r requirements.txt
```

### Step 2: Setup Django
```bash
python manage.py migrate
```
This creates `db.sqlite3` with empty tables.

### Step 3: Load Product Data
```bash
python init_data.py
```
This populates the database with all your products, prices, and sizes.

### Step 4: Create Admin Account (Optional)
```bash
python manage.py createsuperuser
```
Follow prompts to set username, email, password.

### Step 5: Start Server
```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
```

### Step 6: Access the App
- **Main App:** Open browser → http://localhost:8000
- **Admin Panel:** http://localhost:8000/admin (if created)

---

## RUNNING ON DIFFERENT PORTS

If port 8000 is already in use:
```bash
python manage.py runserver 8001
# Then access: http://localhost:8001
```

---

## ACCESSING FROM OTHER DEVICES

### On Local WiFi (Phone, Tablet, Another Computer)

1. Find your computer's IP address:
   ```bash
   ipconfig
   # Look for "IPv4 Address" (e.g., 192.168.1.5)
   ```

2. Start server with IP binding:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

3. On other device:
   ```
   http://192.168.1.5:8000
   ```

---

## DAILY USAGE

### Opening the App
```bash
cd milk_tea_shop
python manage.py runserver
```
Then go to http://localhost:8000

### Closing the App
Press `Ctrl+C` in terminal

### The App is Always Running
- Data saves to `db.sqlite3`
- All sales, stock changes persist
- Restart server anytime, data stays

---

## PROJECT FILES EXPLAINED

```
├── manage.py              → Django command tool. Run: python manage.py <command>
├── db.sqlite3             → YOUR DATABASE. Contains all sales, stock, products
├── requirements.txt       → Python packages needed. Run: pip install -r requirements.txt
├── README.md              → Quick reference guide
├── init_data.py           → Script to add all products. Run: python init_data.py
│
├── config/
│   └── settings.py        → Configuration file. Edit ports, setup here
│
└── tea_shop/
    ├── models.py          → Database structure (Product, Sale, Inventory)
    ├── views.py           → Page logic (what happens when you click buttons)
    ├── urls.py            → Routes (maps URLs to pages)
    ├── templates/         → HTML pages (what you see)
    └── static/
        ├── css/           → Styling (mobile layout, colors, buttons)
        └── js/            → JavaScript (calculations, AJAX clicks)
```

---

## DATABASE LOCATIONS

**Database File:** `milk_tea_shop/db.sqlite3`

This single file contains:
- All products, prices, sizes
- All sales transactions
- Stock levels
- User accounts (if created)

### To Backup:
```bash
copy db.sqlite3 db_backup_%DATE%.sqlite3
```

### To Restore:
```bash
copy db_backup_2024-05-03.sqlite3 db.sqlite3
python manage.py runserver
```

### To Reset (DELETE ALL DATA):
```bash
del db.sqlite3
python manage.py migrate
python init_data.py
```
⚠️ This erases all sales history!

---

## COMMON ISSUES & FIXES

### "ModuleNotFoundError: No module named 'django'"
**Fix:**
```bash
pip install -r requirements.txt
```

### "Address already in use"
**Fix:**
```bash
python manage.py runserver 8001
```

### "Port 8000 refused connection"
Check if server is running:
```bash
python manage.py runserver
```

### "No products in dropdown"
**Fix:**
```bash
python init_data.py
```

### "Can't access from phone"
**Fix:**
```bash
python manage.py runserver 0.0.0.0:8000
# Then use computer's IP: http://192.168.1.5:8000
```

### "Database is locked"
**Cause:** Multiple instances running

**Fix:**
1. Close all terminals
2. Wait 30 seconds
3. Start fresh: `python manage.py runserver`

### "Page shows blank/error"
**Fix:**
1. Close browser tab
2. Stop server (Ctrl+C)
3. Restart: `python manage.py runserver`

---

## PERFORMANCE TIPS

1. **Clear Old Sales (Optional)**
   - After 6 months, sales history gets very large
   - Go to Admin → Sales → delete old records
   - Or run fresh by resetting database

2. **Browser Cache**
   - If styles look wrong, refresh: `Ctrl+Shift+R`
   - Or open in Incognito mode

3. **Close Unused Tabs**
   - Less memory = faster

4. **Mobile WiFi**
   - Use 2.4GHz if available (better range)

---

## UPGRADES & CUSTOMIZATION

### Changing a Product Price
1. Go to admin: http://localhost:8000/admin
2. Click "Products"
3. Find product → Edit → Change price
4. Click Save

### Adding a New Product
1. Admin → Products → Add Product
2. Fill in Name, Category, Prices, Stock
3. Click Save

### Changing Low Stock Alert
1. Admin → Products → Find product → Edit
2. Set "Low stock alert" to your desired number
3. Click Save

### View All Sales
1. Admin → Sales
2. Sort by Date
3. Filter by Product Category

---

## SECURITY NOTES

**For Personal Use Only:**
- This is designed for single operator (you)
- No login required on main interface
- Admin area is password protected

**Protect Your Data:**
- Regular backups: `copy db.sqlite3 db_backup.sqlite3`
- Store backups in cloud or external drive
- Don't share admin password

---

## UPDATING THE APP

All files are bundled. To update:
1. Backup `db.sqlite3`
2. Replace all files except `db.sqlite3`
3. Run migrations: `python manage.py migrate`
4. Check admin: `python manage.py runserver`

---

## MOVING TO NEW COMPUTER

1. Copy entire `milk_tea_shop/` folder
2. Copy `db.sqlite3` file
3. Ensure Python 3.8+ installed
4. Run: `pip install -r requirements.txt`
5. Run: `python manage.py runserver`

**ALL YOUR DATA IS IN db.sqlite3!**

---

## INTEGRATION WITH EXISTING SYSTEMS

### Export Sales (from Admin)
- Visit Admin → Sales
- Select records → Export (may need plugin)
- Use for accounting/reporting

### Manual Export
1. Admin → Sales
2. Right-click → Inspect → Console
3. Copy all sale records
4. Paste in Excel/Google Sheets

### Sync with Accounting
- Keep monthly backups
- Use Sales History page for manual recording
- Or integrate via API (advanced)

---

## SUPPORT & HELP

### Common Questions

**Q: How much data can it store?**
A: Millions of transactions. SQLite is robust.

**Q: Can multiple people use it?**
A: Not at same time currently. Only you should operate it.

**Q: Can I use this online?**
A: Not with default setup. Requires separate hosting.

**Q: How do I backup automatically?**
A: Use Windows Task Scheduler or cron (Linux/Mac)

**Q: Can I add a login screen?**
A: Yes, modify views.py to require login decorator.

**Q: How do I deploy online?**
A: Use services like: Heroku, PythonAnywhere, AWS

---

## KEYBOARD SHORTCUTS

- **Quick Sales:** Click "💰 Sales" tab
- **Quick Restock:** Click "📦 Inventory" tab
- **View Dashboard:** Click "📊 Dashboard" tab
- **See History:** Click "📋 History" tab

---

**Version:** 1.0  
**Last Updated:** May 3, 2024  
**Framework:** Django 5.0.1  
**Database:** SQLite3

For detailed technical info, see `SYSTEM_DESIGN.md`
