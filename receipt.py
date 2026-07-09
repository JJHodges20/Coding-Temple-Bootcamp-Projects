# In this project I will be working with data types and how to manipulate them. I will be using the print function to display the data types and their values.

# This section was a little reduntant, but I wanted to get reps in by actually adding the "str" function to each rather than just ""

item1_name = str("Notebook")
item1_price = str("4.99")
item1_quantity = str("2")

item2_name = str("Pen Pack")
item2_price = str("7.50")
item2_quantity = str("1")

item3_name = str("Backpack")
item3_price = str("34.99")
item3_quantity = str("1")

tax_rate = str("0.075")    # 7.5% sales tax

# In this section I converted the above strings to their appropriate data types for calculations. I also calculated the total for each item, the subtotal, tax amount, and grand total.

item1_price_float = float(item1_price)
item2_price_float = float(item2_price)
item3_price_float = float(item3_price)

item1_quantity_int = int(item1_quantity)
item2_quantity_int = int(item2_quantity)
item3_quantity_int = int(item3_quantity)

tax_rate_float = float(tax_rate)

item1_total = item1_price_float * item1_quantity_int
item2_total = item2_price_float * item2_quantity_int
item3_total = item3_price_float * item3_quantity_int

Total_before_tax = item1_total + item2_total + item3_total
Tax_amount = Total_before_tax * tax_rate_float

Grand_total = Total_before_tax + Tax_amount

# This is where I printed out the receipt in a readable format. I used f-strings to format the output and display the values with two decimal places for currency.

print("=" * 40)
print("Receipt Summary")
print("=" * 40)

print(f"Item 1: {item1_name}")
print(f"  Price: ${item1_price_float:.2f}")
print(f"  Quantity: {item1_quantity_int}")
print(f"  Total: ${item1_total:.2f}")
print()

print(f"Item 2: {item2_name}")
print(f"  Price: ${item2_price_float:.2f}")
print(f"  Quantity: {item2_quantity_int}")
print(f"  Total: ${item2_total:.2f}")
print()

print(f"Item 3: {item3_name}")
print(f"  Price: ${item3_price_float:.2f}")
print(f"  Quantity: {item3_quantity_int}")
print(f"  Total: ${item3_total:.2f}")
print()

print("-" * 40)
print(f"Subtotal:       ${Total_before_tax:.2f}")
print(f"Tax Amount:     ${Tax_amount:.2f}")
print(f"Grand Total:    ${Grand_total:.2f}")
print("=" * 40)