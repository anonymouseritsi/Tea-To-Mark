# 🎨 Tea Shop Manager - UI Layout & Visual Guide

## RESPONSIVE MOBILE DESIGN

### Phone (360px width)
```
┌──────────────────────────┐
│   🧋 Tea Shop Manager    │ ← Header (Orange gradient)
│   Inventory & Sales      │
├──────────────────────────┤
│ 📊 💰 📦 📋              │ ← Navigation (Horizontal scroll)
├──────────────────────────┤
│                          │
│  Dashboard View:         │
│  ┌────────────────────┐  │
│  │ Today's Sales      │  │ ← Stat Card
│  │  ₱12,450          │  │
│  │  48 items         │  │
│  └────────────────────┘  │
│                          │
│  ┌────────────────────┐  │
│  │ Weekly Sales       │  │
│  │  ₱87,230          │  │
│  │  Last 7 days      │  │
│  └────────────────────┘  │
│                          │
│  ┌────────────────────┐  │
│  │  💰 Add Sale       │  │ ← Action Buttons
│  │ (Full width)       │  │
│  └────────────────────┘  │
│                          │
│  ⚠️ Low Stock Alert      │
│  Taro: 5 left           │
│  Red Velvet: 8 left     │
│                          │
└──────────────────────────┘
```

### Sales Entry Page
```
┌──────────────────────────┐
│ Add Sale                 │
├──────────────────────────┤
│                          │
│ Select Product:          │
│ ┌────────────────────┐   │
│ │ 🧊 Classic Tea ▼   │   │
│ │  Taro              │
│ │  Wintermelon       │
│ │  Cookies & Cream   │
│ └────────────────────┘   │
│                          │
│ Size:                    │
│ ┌────────────────────┐   │
│ │ -- Select Size ▼   │   │
│ │  16oz              │
│ │  22oz              │   │
│ └────────────────────┘   │
│                          │
│ Price: ₱29              │ ← Auto-filled
│ Stock: 997 left         │
│                          │
│ Quantity:               │
│ ┌─┐                     │
│ │−│  3  │+│            │ ← +/- Buttons
│ └─┘     └─┘             │
│                          │
│ Total: ₱87              │ ← Auto-calculated
│                          │
│ ┌──────────────────────┐ │
│ │ ✓ Save Sale (Full)   │ │
│ └──────────────────────┘ │
│                          │
│ ┌──────────────────────┐ │
│ │ Recent Sales         │ │
│ │ Taro x2 → ₱58       │
│ │ Red Velvet x1 → ₱45 │
│ └──────────────────────┘ │
│                          │
└──────────────────────────┘
```

### Inventory Page
```
┌──────────────────────────┐
│ Inventory Management     │
├──────────────────────────┤
│ ⚠️ 3 products low stock  │
│                          │
│ ┌────────────────────┐   │
│ │ Taro (Classic)     │   │
│ │ Stock: 5 ⚠️ Low    │   │
│ │ ┌──┐              │   │
│ │ │10│ Restock      │   │
│ │ └──┘              │   │
│ └────────────────────┘   │
│                          │
│ ┌────────────────────┐   │
│ │ Red Velvet         │   │
│ │ (Premium)          │   │
│ │ Stock: 500         │   │
│ │ ┌──┐              │   │
│ │ │10│ Restock      │   │
│ │ └──┘              │   │
│ └────────────────────┘   │
│                          │
│ [More items below]       │
│                          │
└──────────────────────────┘
```

### Sales History Page
```
┌──────────────────────────┐
│ Sales History            │
├──────────────────────────┤
│ Total Records: 247       │
│                          │
│ ┌────────────────────┐   │
│ │ Taro (16oz)        │   │
│ │ Qty: 2 | ₱29 each │
│ │ Total: ₱58         │   │
│ │ May 03, 10:45      │   │
│ └────────────────────┘   │
│                          │
│ ┌────────────────────┐   │
│ │ Red Velvet (22oz)  │   │
│ │ Qty: 1 | ₱45 each │
│ │ Total: ₱45         │   │
│ │ May 03, 10:40      │   │
│ └────────────────────┘   │
│                          │
│ ┌────────────────────┐   │
│ │ Burger Solo        │   │
│ │ Qty: 3 | ₱25 each │
│ │ Total: ₱75         │   │
│ │ May 03, 10:35      │   │
│ └────────────────────┘   │
│                          │
│ [Last 100 records]       │
│                          │
└──────────────────────────┘
```

## DESKTOP/TABLET LAYOUT (768px+)

### Dashboard - 3 Column Layout
```
┌────────────────────────────────────────────┐
│         🧋 Tea Shop Manager               │
│      Inventory & Sales Tracker             │
├────────────────────────────────────────────┤
│ 📊 Dashboard | 💰 Sales | 📦 Inventory | 📋 History
├────────────────────────────────────────────┤
│                                            │
│ ┌─────────────────┐ ┌────────────┐ ┌─────┐
│ │ Today's Sales   │ │ Weekly   │ │Monthly
│ │  ₱12,450        │ │ Sales    │ │Sales
│ │  48 items       │ │ ₱87,230  │ │₱345,600
│ └─────────────────┘ └────────────┘ └─────┘
│                                            │
│ ┌──────────────────────────────────────┐  │
│ │         💰 Add Sale                  │  │ ← Full Width
│ │      📦 Restock Inventory            │  │
│ └──────────────────────────────────────┘  │
│                                            │
│ ┌──────────────────────────────────────┐  │
│ │ ⚠️ Low Stock Alert                   │  │
│ │ • Taro: 5 left                       │  │
│ │ • Red Velvet: 8 left                 │  │
│ │ • Mango Shake: 3 left                │  │
│ └──────────────────────────────────────┘  │
│                                            │
└────────────────────────────────────────────┘
```

## COLOR SCHEME

```
Primary Colors:
├─ Orange Gradient (#FF6B6B to #FF8C42)  ← Header, buttons
├─ Teal (#4ECDC4)                        ← Secondary buttons
├─ Green (#51CF66)                       ← Success, totals
└─ Yellow (#FFD93D)                      ← Warnings, low stock

Background Colors:
├─ Light Gray (#F8F9FA)                  ← Page background
├─ White (#FFFFFF)                       ← Cards, forms
└─ Light Orange (#FFFBF0)                ← Low stock alerts

Typography:
├─ Header: 28px bold (mobile) / 32px (desktop)
├─ Stats: 24px bold / 20px normal
├─ Labels: 14px bold
└─ Body: 13-14px regular
```

## BUTTON STYLES

```
Primary Button (Save Sale):
┌─────────────────────────┐
│  ✓ Save Sale            │ ← Green, full width
│ 14px bold white text    │
│ 12px padding vertical   │
└─────────────────────────┘

Secondary Button (Reset):
┌─────────────────────────┐
│  Reset                  │ ← Teal, full width
└─────────────────────────┘

Quantity Controls:
┌──┐     ┌──┐
│−│      │+│ ← Small, 40x40px
└──┘     └──┘

Large Action Buttons:
┌──────────────────────────┐
│     💰 Add Sale           │ ← Full width, 14px font
│     📦 Restock           │
└──────────────────────────┘
```

## FORM INPUTS

```
Text & Select Fields:
┌────────────────────────────┐
│ Select Product:            │
│ ┌─────────────────────────┐│ ← Light gray bg, border
│ │ Taro              ▼     ││ ← 12px padding
│ └─────────────────────────┘│
└────────────────────────────┘

Number Inputs:
│ Quantity:                  │
│ ┌──┐                       │
│ │−│  3  │+│               │ ← Clickable +/- at sides
│ └──┘     └──┘             │

Focus State:
│ Field is selected:         │
│ ┌────────────────────────┐│
│ │ Input focused         ││ ← Orange border + shadow
│ └────────────────────────┘│
```

## ALERT BOXES

```
Success (Green):
┌──────────────────────────────┐
│ ✓ Sale added: Taro x2 - ₱58  │ ← Green bg, dark text
└──────────────────────────────┘

Warning (Yellow):
┌──────────────────────────────┐
│ ⚠️ Low Stock Alert            │ ← Yellow bg, dark text
│ • Taro: 5 left              │
│ • Red Velvet: 8 left        │
└──────────────────────────────┘

Error (Red):
┌──────────────────────────────┐
│ ✗ Error saving sale           │ ← Red bg, white text
│ Please check your input       │
└──────────────────────────────┘
```

## RESPONSIVE BEHAVIOR

### Phone (360-480px)
- Single column layout
- Full-width buttons
- Stacked stat cards
- Large touch targets (40px+)
- Bottom navigation

### Tablet (768-1024px)
- 2-3 column grid
- Side-by-side buttons
- Wider content area
- Horizontal forms

### Desktop (1025px+)
- Full 3-column stats
- Wider sidebar ready (if added)
- Multi-panel dashboard
- Optimal reading width

## ANIMATIONS & INTERACTIONS

```
Button Hover:
Normal → Darker shade (10% darker)

Button Click/Active:
Normal → 20% darker, slight shadow

Input Focus:
Border changes to orange
Subtle box-shadow appears
Background stays white

Form Submit:
Button greyed out briefly
Then shows success/error message

Navigation Highlight:
Current page tab has orange bottom border
Others have gray border

Card Hover (Desktop):
Slight shadow increase
Subtle scale up (1.02x)
```

## ACCESSIBILITY

✅ Large touch targets (40px minimum)  
✅ High contrast colors (WCAG AA+)  
✅ Clear labels on all inputs  
✅ Keyboard navigable  
✅ Screen reader friendly  
✅ No color-only information (icons + text)  
✅ Focus visible on all interactive elements  

## PRINT LAYOUT

```
When printed:
✓ Header and navigation hidden
✓ Content full width
✓ Dark text on white background
✓ All data visible without scroll
✓ Good for receipts/reports
```

---

## FILE THAT CONTROLS DESIGN

**Main CSS:** `tea_shop/static/css/style.css` (800+ lines)

Key sections:
- `:root` variables - colors, sizes
- Mobile-first base styles (phone)
- Card & button styles
- Form inputs
- Responsive media queries
- Print styles

**No CSS framework needed** - all vanilla CSS3 with:
- CSS Grid
- Flexbox
- CSS Variables
- Media Queries
- Gradients
- Shadows & Transitions

---

**Design Philosophy:**
- Fast to code and update
- Fast to load (no CDN)
- Responsive without frameworks
- Optimized for selling speed
- Clear visual hierarchy
- Mobile-first approach
