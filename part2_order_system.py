# Part 2: Data Structures
# Theme  : Restaurant Menu & Order Management System

# ============================================================
# PROVIDED DATA — Do not modify
# ============================================================

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}


# ============================================================
# TASK 1 — Explore the Menu 
# ============================================================

print("\n" + "=" * 50)
print("        TASK 1 — EXPLORE THE MENU")
print("=" * 50)

# --- Task 1.1: Print menu grouped by category ---
# Required format:
#   ===== Starters =====
#   Paneer Tikka        ₹180.00   [Available]
#   Chicken Wings       ₹220.00   [Unavailable]

# Get all unique categories from menu, sorted alphabetically
categories = sorted(set(details["category"] for details in menu.values()))

# Loop through each category first, then filter items belonging to it
for category in categories:
    print(f"\n===== {category} =====")
    for item_name, details in menu.items():
        if details["category"] == category:
            # Show [Available] or [Unavailable] based on the boolean flag
            status = "[Available]" if details["available"] else "[Unavailable]"
            print(f"{item_name:<20} ₹{details['price']:.2f}   {status}")

# --- Task 1.2: Menu statistics using dictionary methods ---

print("\n--- Menu Statistics ---")

# Total items = number of keys in menu dictionary
total_items = len(menu)
print(f"Total number of items on the menu : {total_items}")

# Available items = count only those where available is True
available_count = sum(1 for d in menu.values() if d["available"] == True)
print(f"Total number of available items   : {available_count}")

# Most expensive item using max() with price as key
most_expensive = max(menu, key=lambda item: menu[item]["price"])
print(f"Most expensive item               : {most_expensive} — ₹{menu[most_expensive]['price']:.2f}")

# All items priced under 150
print("Items priced under ₹150:")
for name, details in menu.items():
    if details["price"] < 150:
        print(f"   {name} — ₹{details['price']:.2f}")


# ============================================================
# TASK 2 — Cart Operations 
# ============================================================

print("\n" + "=" * 50)
print("        TASK 2 — CART OPERATIONS")
print("=" * 50)

# Cart starts as an empty list
# Each entry format: {"item": "Paneer Tikka", "quantity": 2, "price": 180.0}
cart = []


def add_to_cart(item_name, quantity):
    """
    Adds item to cart safely:
    - Check 1: item must exist in menu
    - Check 2: item must be available
    - Check 3: if already in cart, increase quantity (no duplicate entry)
    """
    if item_name not in menu:
        print(f"  '{item_name}' does not exist in the menu. Cannot add.")
        return
    if menu[item_name]["available"] == False:
        print(f"  '{item_name}' is currently unavailable. Cannot add.")
        return
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] += quantity
            print(f"  '{item_name}' already in cart. Quantity updated to {entry['quantity']}.")
            return
    cart.append({"item": item_name, "quantity": quantity, "price": menu[item_name]["price"]})
    print(f"  '{item_name}' x{quantity} added to cart.")


def remove_from_cart(item_name):
    """Removes item from cart by name. Prints message if not found."""
    for entry in cart:
        if entry["item"] == item_name:
            cart.remove(entry)
            print(f"  '{item_name}' removed from cart.")
            return
    print(f"  '{item_name}' is not in the cart. Nothing to remove.")


def update_quantity(item_name, new_quantity):
    """Updates quantity of an existing cart item."""
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] = new_quantity
            print(f"  '{item_name}' quantity updated to {new_quantity}.")
            return
    print(f"  '{item_name}' is not in the cart. Cannot update.")


def print_cart():
    """Prints current cart state after each operation."""
    if len(cart) == 0:
        print("  Cart is empty.")
    else:
        print("  Current Cart:")
        for entry in cart:
            line_total = entry["quantity"] * entry["price"]
            print(f"    {entry['item']:<20} x{entry['quantity']}   ₹{line_total:.2f}")


# --- Task 2.4: Simulate the exact sequence from the question ---

print("\n--- Simulating Cart Operations ---\n")

print("Step 1: Add 'Paneer Tikka' x 2")
add_to_cart("Paneer Tikka", 2)
print_cart()

print("\nStep 2: Add 'Gulab Jamun' x 1")
add_to_cart("Gulab Jamun", 1)
print_cart()

print("\nStep 3: Add 'Paneer Tikka' x 1  (already in cart — quantity becomes 3)")
add_to_cart("Paneer Tikka", 1)
print_cart()

print("\nStep 4: Try to add 'Mystery Burger'  — does not exist in menu")
add_to_cart("Mystery Burger", 1)
print_cart()

print("\nStep 5: Try to add 'Chicken Wings'  — exists but is unavailable")
add_to_cart("Chicken Wings", 1)
print_cart()

print("\nStep 6: Remove 'Gulab Jamun'")
remove_from_cart("Gulab Jamun")
print_cart()

# --- Task 2.5: Final Order Summary (exact format from question) ---

print("\n========== Order Summary ==========")
subtotal = 0
for entry in cart:
    line_total = entry["quantity"] * entry["price"]
    subtotal += line_total
    print(f"  {entry['item']:<20} x{entry['quantity']}   ₹{line_total:.2f}")
print("------------------------------------")
gst = subtotal * 0.05
total_payable = subtotal + gst
print(f"  {'Subtotal:':<20} ₹{subtotal:.2f}")
print(f"  {'GST (5%):':<20} ₹{gst:.2f}")
print(f"  {'Total Payable:':<20} ₹{total_payable:.2f}")
print("====================================")


# ============================================================
# TASK 3 — Inventory Tracker with Deep Copy 
# ============================================================

import copy  # import copy module for deep copy functionality

print("\n" + "=" * 50)
print("   TASK 3 — INVENTORY TRACKER + DEEP COPY")
print("=" * 50)

# --- Task 3.1: Deep copy inventory BEFORE any changes ---
# copy.deepcopy() creates a fully independent copy
# Changes to 'inventory' will NOT affect 'inventory_backup'

inventory_backup = copy.deepcopy(inventory)

print("\nStep 1: Demonstrating that deep copy works correctly")
# Temporarily change a value in inventory to prove backup is unaffected
inventory["Paneer Tikka"]["stock"] = 99
print(f"  inventory['Paneer Tikka']['stock']        = {inventory['Paneer Tikka']['stock']}")
print(f"  inventory_backup['Paneer Tikka']['stock'] = {inventory_backup['Paneer Tikka']['stock']}")
print("  Backup is unaffected — deep copy is working correctly!")

# Restore inventory to original state before doing real deductions
inventory["Paneer Tikka"]["stock"] = 10
print("  Inventory restored to original (stock = 10).")

# --- Task 3.2: Deduct cart quantities from inventory ---
# Use the final cart from Task 2 (Paneer Tikka x3)

print("\nStep 2: Deducting cart quantities from inventory...")
for entry in cart:
    item_name = entry["item"]
    qty_needed = entry["quantity"]
    if item_name in inventory:
        available_stock = inventory[item_name]["stock"]
        if available_stock >= qty_needed:
            # Sufficient stock — deduct normally
            inventory[item_name]["stock"] -= qty_needed
            print(f"  {item_name}: Deducted {qty_needed}. "
                  f"Stock remaining: {inventory[item_name]['stock']}")
        else:
            # Not enough stock — deduct only what is available, do not go below 0
            print(f"  WARNING: {item_name} — Only {available_stock} in stock, "
                  f"needed {qty_needed}. Deducting {available_stock}.")
            inventory[item_name]["stock"] = 0

# --- Task 3.3: Reorder Alerts ---
# Print alert for every item whose stock is AT or BELOW its reorder_level

print("\nStep 3: Checking Reorder Alerts...")
print("-" * 55)
reorder_found = False
for item_name, details in inventory.items():
    if details["stock"] <= details["reorder_level"]:
        print(f"  Reorder Alert: {item_name} — Only {details['stock']} unit(s) left "
              f"(reorder level: {details['reorder_level']})")
        reorder_found = True
if not reorder_found:
    print("  All items have sufficient stock. No reorder alerts.")
print("-" * 55)

# --- Task 3.4: Print both inventory and inventory_backup side by side ---
# Differences prove the deep copy successfully protected the original backup

print("\nStep 4: Inventory vs Backup Comparison")
print(f"  {'Item':<20} {'Current Stock':>14} {'Backup Stock':>14}")
print("  " + "-" * 50)
for item in inventory:
    curr = inventory[item]["stock"]
    bkp  = inventory_backup[item]["stock"]
    flag = "  <- changed" if curr != bkp else ""
    print(f"  {item:<20} {curr:>14} {bkp:>14}{flag}")
print("\n  Differences confirm deep copy protected the original backup!")


# ============================================================
# TASK 4 — Daily Sales Log Analysis 
# ============================================================

print("\n" + "=" * 50)
print("    TASK 4 — DAILY SALES LOG ANALYSIS")
print("=" * 50)

# --- Task 4.1: Print total revenue per day ---

print("\n--- Revenue Per Day ---")
for date, orders in sales_log.items():
    daily_revenue = sum(order["total"] for order in orders)
    print(f"  {date}  ->  ₹{daily_revenue:.2f}")

# --- Task 4.2: Best-selling day (highest total revenue) ---

best_day = max(sales_log, key=lambda date: sum(o["total"] for o in sales_log[date]))
best_day_revenue = sum(o["total"] for o in sales_log[best_day])
print(f"\n  Best-Selling Day: {best_day}  (₹{best_day_revenue:.2f})")

# --- Task 4.3: Most ordered item ---
# Count how many orders each item appears in across all days

item_order_count = {}
for date, orders in sales_log.items():
    for order in orders:
        for item in order["items"]:
            if item in item_order_count:
                item_order_count[item] += 1
            else:
                item_order_count[item] = 1

most_ordered_item = max(item_order_count, key=lambda x: item_order_count[x])
print(f"  Most Ordered Item: {most_ordered_item} "
      f"(appeared in {item_order_count[most_ordered_item]} orders)")

# --- Task 4.4: Add new day exactly as given in question and reprint table ---
# Order 11 total: Butter Chicken(320) + Gulab Jamun(90) + Garlic Naan(40) = 450
# Order 12 total: Paneer Tikka(180) + Rasgulla(80) = 260

sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]
print("\n  New day '2025-01-05' added to sales_log.")

# Reprint updated revenue per day
print("\n--- Updated Revenue Per Day ---")
for date, orders in sales_log.items():
    daily_revenue = sum(order["total"] for order in orders)
    print(f"  {date}  ->  ₹{daily_revenue:.2f}")

# Recompute best-selling day after new data
best_day_new = max(sales_log, key=lambda date: sum(o["total"] for o in sales_log[date]))
best_day_new_revenue = sum(o["total"] for o in sales_log[best_day_new])
print(f"\n  Updated Best-Selling Day: {best_day_new}  (₹{best_day_new_revenue:.2f})")

# --- Task 4.5: Numbered list of all orders using enumerate ---
# Includes all days including the newly added day

print("\n--- Numbered List of All Orders ---")
order_number = 1
for date, orders in sales_log.items():
    for order in orders:
        items_str = ", ".join(order["items"])
        print(f"  {order_number}. [{date}] Order #{order['order_id']} "
              f"— ₹{order['total']:.2f} — Items: {items_str}")
        order_number += 1

print("\n" + "=" * 50)
print("      ALL TASKS COMPLETED SUCCESSFULLY")
print("=" * 50)
