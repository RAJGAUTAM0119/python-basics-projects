customer_name = "Raj Gautam"
customer_email = "raj@gmail.com"

product_name = "Mechanical Keyboard"
product_price = 1200
quantity = 10

subtotal = product_price * quantity
discount_20 = subtotal >= 10000 and 20

discount_percentage = int(discount_20 or 10)

discount_amount = subtotal * discount_percentage / 100

discounted_price = subtotal - discount_amount

shipping_cost = discounted_price < 5000 and 150
shipping = shipping_cost or 0

is_free_shipping = discounted_price >= 5000

gst_percentage = 18 
gst_amount = discounted_price * gst_percentage / 100

final_amount = discounted_price + gst_amount + shipping

is_premium = final_amount >= 10000 and is_free_shipping

padding = 42

print(f"{"="*padding}")
print(f"{"E-COMMERCE ORDER SUMMARY".center(padding)}")
print(f"{"="*padding}")
print()

leftpadding = 20

print(f"{"Customer".ljust(20)} : {customer_name}")
print(f"{"Email".ljust(20)} : {customer_email}")
print()
print(f"{"Product".ljust(20)} : {product_name}")
print(f"{"Price".ljust(20)} : ₹{product_price}")
print(f"{"Quantity".ljust(20)} : {quantity}")
print()
print(f"{"-"*padding}")
print()


print(f"{"Subtotal".ljust(20)} : ₹{subtotal}")
print(f"{"Discount".ljust(20)} : {discount_percentage}%")
print(f"{"Discount Amount".ljust(20)} : ₹{discount_amount}")
print(f"{"After Discount".ljust(20)} : ₹{discounted_price}")
print()
print(f"{"GST".ljust(20)} : {gst_percentage}%")
print(f"{"GST Amount".ljust(20)} : ₹{gst_amount}")
print()
print(f"{"Shipping".ljust(20)} : ₹{shipping}")
print(f"{"Free Shipping".ljust(20)} : {is_free_shipping}")

print()
print(f"{"-"*padding}")
print()


print(f"{"Final Amount".ljust(20)} : {final_amount}")
print(f"{"Premium Order".ljust(20)} : {is_premium}")
print()
print(f"{"="*padding}")