# sales_analyzer.py

import csv

# File names
input_file = "sales_data.csv"
report_file = "sales_report.txt"
summary_file = "product_summary.csv"

# Running totals
total_revenue = 0.0
revenue_per_product = {}
quantity_per_product = {}
revenue_per_day = {}

# Read the sales CSV file
with open(input_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        date = row["date"]
        product = row["product"]
        quantity = int(row["quantity"])
        price = float(row["price"])

        # Calculate the revenue for the current row
        row_revenue = quantity * price

        # Add to total revenue
        total_revenue += row_revenue

        # Add revenue to the correct product
        if product not in revenue_per_product:
            revenue_per_product[product] = 0.0

        revenue_per_product[product] += row_revenue

        # Add quantity to the correct product
        if product not in quantity_per_product:
            quantity_per_product[product] = 0

        quantity_per_product[product] += quantity

        # Add revenue to the correct date
        if date not in revenue_per_day:
            revenue_per_day[date] = 0.0

        revenue_per_day[date] += row_revenue

# Find the day with the highest total revenue
highest_revenue_day = None
highest_daily_revenue = 0.0

for date, revenue in revenue_per_day.items():
    if highest_revenue_day is None or revenue > highest_daily_revenue:
        highest_revenue_day = date
        highest_daily_revenue = revenue

# Write the formatted text report
with open(report_file, "w", encoding="utf-8") as file:
    file.write("=" * 50 + "\n")
    file.write("SALES SUMMARY REPORT\n")
    file.write("=" * 50 + "\n\n")

    file.write(f"Total Revenue: ${total_revenue:,.2f}\n")
    file.write(
        f"Highest Revenue Day: {highest_revenue_day} "
        f"(${highest_daily_revenue:,.2f})\n"
    )

    file.write("\nRevenue by Product\n")
    file.write("-" * 50 + "\n")

    for product, revenue in revenue_per_product.items():
        quantity = quantity_per_product[product]

        file.write(
            f"{product:<15}"
            f"Quantity: {quantity:<5}"
            f"Revenue: ${revenue:,.2f}\n"
        )

# Write the product summary CSV
with open(summary_file, "w", newline="", encoding="utf-8") as file:
    fieldnames = ["product", "total_quantity", "total_revenue"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for product in revenue_per_product:
        writer.writerow(
            {
                "product": product,
                "total_quantity": quantity_per_product[product],
                "total_revenue": f"{revenue_per_product[product]:.2f}",
            }
        )

print("Sales analysis completed successfully.")
print(f"Created: {report_file}")
print(f"Created: {summary_file}")