# This program will be meant to help a user plan a trip

# This section is for setting variables and calculating costs
destination = input("Enter your destination: ")
total_distance = float(input("Enter the total distance of your trip in miles: "))
car_mpg = float(input("Enter your car's miles per gallon (MPG): "))
gas_price = float(input("Enter the current gas price per gallon: "))
number_of_nights = int(input("Enter the number of nights you will be staying: "))
average_hotel_cost = float(input("Enter the average cost per night for your hotel: "))
daily_food_budget = float(input("Enter your daily food budget: "))
Gallons_needed = total_distance / car_mpg
Total_gas_cost = Gallons_needed * gas_price
Total_hotel_cost = average_hotel_cost * number_of_nights
Total_food_cost = daily_food_budget * number_of_nights
Grand_total_cost = Total_gas_cost + Total_hotel_cost + Total_food_cost


# This section is for displaying the results
print("\n=== Road Trip Budget Planner ===\n")

print(f"Destination: {destination}")
print(f"Total Distance: {total_distance} miles")

print("\n--- Cost Breakdown ---\n")

print(f"Gas Cost: ${Total_gas_cost:.2f}")
print(f"Hotel Cost: ${Total_hotel_cost:.2f}")
print(f"Food Cost: ${Total_food_cost:.2f}")

print("\n" + "-" * 30)

print(f"\nGrand Total Cost: ${Grand_total_cost:.2f}")
