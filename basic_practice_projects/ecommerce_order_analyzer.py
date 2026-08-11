customer_name = "Raj Gautam"
customer_email = "raj@gmail.com`"

product_name = "Mechanical Keyboard"
product_price = 1000
quantity = 10

subtotal = product_price * quantity
discount_20 = subtotal >= 10000 and 20

discount_percentage = int(discount_20 or 10)

discount_amount = subtotal * discount_percentage / 100

discounted_price = subtotal - discount_amount

gst_percentage = 18 
gst_amount = discounted_price * gst_percentage / 100


shipping_cost = discounted_price <= 7999 and 150
shipping = shipping_cost or 0

is_free_shipping  = not bool(shipping)

print(is_free_shipping)

final_amount = discounted_price + gst_amount + shipping
print(discounted_price)
print(gst_amount)
print(shipping)
print(final_amount)