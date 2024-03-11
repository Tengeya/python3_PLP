"""
Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
"""
def calculate_discount(price, discount_percent):
    if discount_percent >=20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
#prompt user for their input
product_name = input("Enter the name of the product: ")
price = float(input("Enter the price of the product: "))
discount_percent = int(input("Enter the discount percentage: "))

#calculate the final price
final_price = calculate_discount(price, discount_percent)

print("\nProduct Name: ", product_name.title())
print("Price: Ksh.", format(price, '.2f'))

if final_price == price:
    print("No discount applied. Final price:", final_price)
else:
    print("Final price after discount:", final_price)
    

