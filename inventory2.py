# This project displays and manages a product inventory for a small electronics business


# Inventory dictionary

inventory = {
    "laptop": {"price": 999.99, "quantity": 15},
    "mouse": {"price": 29.99, "quantity": 50},
    "keyboard": {"price": 59.99, "quantity": 35},
    "display": {"price": 99.99, "quantity": 25},
}

low_stock_products = set()


# Display the full inventory in a formatted table

def display_inventory():
    total_quantity = 0
    grand_total_value = 0

    print("\n" + "=" * 70)
    print("                     Product Inventory")
    print("=" * 70)
    print(f"{'Product':<15}{'Price':>12}{'Quantity':>12}{'Total Value':>18}")
    print("-" * 70)

    for product, details in inventory.items():
        price = details["price"]
        quantity = details["quantity"]
        total_value = price * quantity

        total_quantity += quantity
        grand_total_value += total_value

        price_display = f"${price:,.2f}"
        value_display = f"${total_value:,.2f}"

        print(
            f"{product.capitalize():<15}"
            f"{price_display:>12}"
            f"{quantity:>12}"
            f"{value_display:>18}"
        )

    print("-" * 70)

    grand_total_display = f"${grand_total_value:,.2f}"

    print(
        f"{'TOTALS':<15}"
        f"{'':>12}"
        f"{total_quantity:>12}"
        f"{grand_total_display:>18}"
    )

    print("=" * 70)


# Update the low-stock set based on current quantities

def update_low_stock():
    low_stock_products.clear()

    for product, details in inventory.items():
        if details["quantity"] < 10:
            low_stock_products.add(product)


# Let the user look up a product

def look_up_product():
    product_name = input("\nEnter the product name to look up: ").lower()

    product_details = inventory.get(product_name)

    if product_details is None:
        print("\nProduct not found.")
    else:
        price = product_details["price"]
        quantity = product_details["quantity"]
        total_value = price * quantity

        print("\nProduct Details")
        print("-" * 30)
        print(f"Product: {product_name.capitalize()}")
        print(f"Price: ${price:,.2f}")
        print(f"Quantity: {quantity}")
        print(f"Total Value: ${total_value:,.2f}")


# Let the user simulate a sale or restock

def update_product_quantity():
    product_name = input("\nEnter the product name to update: ").lower()

    product_details = inventory.get(product_name)

    if product_details is None:
        print("\nProduct not found.")
        return

    print("\nWhat type of update would you like to make?")
    print("1. Sale")
    print("2. Restock")

    update_choice = input("Enter your choice (1 or 2): ")

    try:
        amount = int(input("Enter the quantity: "))

        if amount <= 0:
            print("\nQuantity must be greater than zero.")
            return

        if update_choice == "1":
            if amount > product_details["quantity"]:
                print("\nNot enough inventory available for that sale.")
                return

            product_details["quantity"] -= amount
            print(
                f"\nSale recorded. "
                f"{product_name.capitalize()} quantity is now "
                f"{product_details['quantity']}."
            )

        elif update_choice == "2":
            product_details["quantity"] += amount
            print(
                f"\nRestock recorded. "
                f"{product_name.capitalize()} quantity is now "
                f"{product_details['quantity']}."
            )

        else:
            print("\nInvalid choice. Please enter 1 or 2.")
            return

        update_low_stock()

    except ValueError:
        print("\nInvalid quantity. Please enter a whole number.")


update_low_stock()

display_inventory()

# Main menu

print("\nWhat would you like to do?")
print("1. Look up a product")
print("2. Update a product quantity")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    look_up_product()

elif choice == "2":
    update_product_quantity()
    display_inventory()

else:
    print("\nInvalid choice. Please enter 1 or 2.")

# Display low-stock products

print("\nLow-Stock Products:")

if low_stock_products:
    for product in sorted(low_stock_products):
        print(f"- {product.capitalize()}")
else:
    print("No products are currently low stock.")