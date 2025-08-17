# Function to apply discount 
def calculate_discount(price, discount_percent):
    # Apply discount if 20% and more
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        discounted_price = price - discount
        return discounted_price
    else:
        return price
    
# Prompt for user input
try:
    original_price = float(input("Enter the original price: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Call the function
    final_price = calculate_discount(original_price, discount_percentage)

    # Print
    if final_price != original_price:
        print(f"Discount applied! The final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${original_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values.")
