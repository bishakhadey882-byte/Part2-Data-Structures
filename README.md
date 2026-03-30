# Part2-Data-Structures
## Theme: Restaurant Menu & Order Management System

---

## 📌 Overview

This project implements a **Restaurant Order Management System** entirely using Python's core data structures — lists, dictionaries, and nested combinations of both. The system covers menu exploration, cart operations, inventory tracking with deep copy, and daily sales log analysis.

**File:** `part2_order_system.py`  
**Language:** Python 3  

---

## 🗂️ Project Structure

```
part2_order_system.py   ← Single Python script containing all 4 tasks
README.md               ← This file
```

---

## 📦 Provided Data (Not Modified)

Three data structures are provided and used across all tasks:

| Variable | Type | Description |
|---|---|---|
| `menu` | `dict` of `dict` | 10 items with category, price, and availability |
| `inventory` | `dict` of `dict` | Stock count and reorder level for each item |
| `sales_log` | `dict` of `list` of `dict` | Daily orders with order ID, items, and totals |

---

## ✅ Task 1 — Explore the Menu 

### What it does:

**Task 1.1 — Print menu grouped by category**

- Extracts all unique categories from the menu using a `set` comprehension
- Sorts categories alphabetically using `sorted()`
- Loops through each category first, then filters and prints matching items
- Displays availability as `[Available]` or `[Unavailable]` based on the boolean flag

**Sample Output:**
```
===== Desserts =====
Gulab Jamun          ₹90.00   [Available]
Ice Cream            ₹110.00  [Unavailable]
Rasgulla             ₹80.00   [Available]

===== Mains =====
Butter Chicken       ₹320.00  [Available]
...
```

**Task 1.2 — Menu Statistics using dictionary methods**

| Statistic | Method Used |
|---|---|
| Total items | `len(menu)` |
| Available items | `sum()` with generator expression filtering `available == True` |
| Most expensive item | `max()` with `lambda` key on price |
| Items priced under ₹150 | Loop with conditional `price < 150` check |

---

## ✅ Task 2 — Cart Operations 

### Cart Structure

Each cart entry is a dictionary:
```python
{"item": "Paneer Tikka", "quantity": 2, "price": 180.0}
```

### Functions Implemented

| Function | Behaviour |
|---|---|
| `add_to_cart(item_name, quantity)` | Validates existence → validates availability → checks for duplicates → appends or updates quantity |
| `remove_from_cart(item_name)` | Finds item by name and removes it; prints message if not found |
| `update_quantity(item_name, new_quantity)` | Finds item and updates its quantity; prints message if not found |
| `print_cart()` | Prints all cart entries with line totals, or "Cart is empty" |

### Validation Checks in `add_to_cart`

1. **Item must exist in menu** → prints `'X' does not exist in the menu.`
2. **Item must be available** → prints `'X' is currently unavailable.`
3. **If already in cart** → increases quantity (no duplicate entry created)

### Simulated Cart Sequence (Task 2.4)

| Step | Action | Outcome |
|---|---|---|
| 1 | Add `Paneer Tikka` × 2 | Added successfully |
| 2 | Add `Gulab Jamun` × 1 | Added successfully |
| 3 | Add `Paneer Tikka` × 1 | Duplicate detected → quantity updated to 3 |
| 4 | Add `Mystery Burger` × 1 | Does not exist in menu → rejected |
| 5 | Add `Chicken Wings` × 1 | Exists but unavailable → rejected |
| 6 | Remove `Gulab Jamun` | Removed successfully |

### Final Order Summary (Task 2.5)

```
========== Order Summary ==========
Paneer Tikka         x3   ₹540.00
------------------------------------
Subtotal:            ₹540.00
GST (5%):            ₹27.00
Total Payable:       ₹567.00
====================================
```

GST is calculated as `subtotal × 0.05` and added to get the total payable.

---

## ✅ Task 3 — Inventory Tracker with Deep Copy 

### Step-by-step Logic

**Task 3.1 — Deep Copy**
- `import copy` is used to deep copy the inventory **before** any modifications
- `copy.deepcopy(inventory)` creates a fully independent copy — changes to `inventory` do **not** affect `inventory_backup`
- This is demonstrated by temporarily changing a stock value and printing both dictionaries to prove independence, then restoring the original value

**Task 3.2 — Deduct Cart Quantities**
- Iterates through the final cart from Task 2 (Paneer Tikka × 3)
- Checks available stock before deducting:
  - If `stock >= quantity_needed` → deducts normally
  - If `stock < quantity_needed` → prints a warning and sets stock to 0 (never goes negative)

**Task 3.3 — Reorder Alerts**
- After deductions, loops through `inventory`
- Prints a reorder alert for every item whose `stock <= reorder_level`
- Format: `Reorder Alert: <item> — Only <n> unit(s) left (reorder level: <n>)`

**Task 3.4 — Side-by-side Comparison**
- Prints `inventory` and `inventory_backup` side by side
- Marks changed entries with `← changed` to clearly demonstrate that the backup is unaffected

---

## ✅ Task 4 — Daily Sales Log Analysis 

**Task 4.1 — Revenue Per Day**
- Loops through `sales_log` and sums `order["total"]` for each date using `sum()` with a generator

**Task 4.2 — Best-Selling Day**
- Uses `max()` with a `lambda` key that computes daily revenue inline
- Identifies the date with the highest total revenue

**Task 4.3 — Most Ordered Item**
- Builds a frequency dictionary `item_order_count` by iterating through all orders and all items per order
- Uses `max()` with a `lambda` key to find the most frequently appearing item across all orders

**Task 4.4 — Add New Day and Reprint**
- Adds `"2025-01-05"` with two new orders to `sales_log`
- Reprints the revenue-per-day table and recalculates the best-selling day

```python
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]
```

**Task 4.5 — Numbered List of All Orders using `enumerate`**
- Iterates through all dates and all orders (including the newly added day)
- Prints a global numbered list:
  ```
  1. [2025-01-01] Order #1 — ₹220.00 — Items: Paneer Tikka, Garlic Naan
  2. [2025-01-01] Order #2 — ₹210.00 — Items: Gulab Jamun, Veg Soup
  ...
  ```

---

## 🧠 Key Concepts Demonstrated

| Concept | Where Used |
|---|---|
| Dictionary traversal (`.items()`, `.values()`, `.keys()`) | Tasks 1, 3, 4 |
| Nested dictionary access | All tasks |
| List of dictionaries (cart, orders) | Tasks 2, 4 |
| `max()` with `lambda` key | Tasks 1, 4 |
| `sum()` with generator expression | Tasks 1, 2, 4 |
| `set()` for unique values | Task 1 |
| `copy.deepcopy()` | Task 3 |
| Conditional cart logic (add/remove/update) | Task 2 |
| Frequency counting with dictionary | Task 4 |
| `enumerate` for numbered output | Task 4 |
| f-strings with formatting (`:<20`, `:.2f`) | All tasks |

---

## ▶️ How to Run

```bash
python part2_order_system.py
```

No external libraries required. Only the built-in `copy` module is imported (standard library).

**Python version:** 3.x (tested on Python 3.8+)

---

## 📝 Notes

- The provided `menu`, `inventory`, and `sales_log` data are **not modified** — all tasks operate on this data as instructed.
- All comments in the code explain the logic step by step.
- Cart operations handle all edge cases: non-existent items, unavailable items, duplicate additions, and removing items not in the cart.
- Inventory deduction never allows stock to go below 0.
- The deep copy is proven to work correctly by a live demonstration within the script output.
