product_price = "2499.50"
product_price_float = float(product_price)
quantity = "3"
quantity_int = int(quantity)
discount_percentage = 15
tax_percentage = "18"
tax_percentage_float = float(tax_percentage)
cashback_percentage = 5.0
is_payment_received = True


subtotal = product_price_float * quantity_int
discount = subtotal * discount_percentage / 100

after_discount = subtotal - discount 

tax_amount = after_discount * tax_percentage_float / 100

after_tax = after_discount + tax_amount

cashback = after_tax * cashback_percentage / 100

final_amount = after_tax - cashback

is_payment_successful = is_payment_received and final_amount > 0

padding = 40
ljust_width = 20


print('='*padding)
print('TRANSACTION RECONSTRUCTOR'.center(padding))
print('='*padding)
print()

print(f"{'Product Price'.ljust(ljust_width)} : ₹{product_price_float:.2f}")
print(f"{'Quantity'.ljust(ljust_width)} : {quantity_int}")

print()
print(f"{'Subtotal'.ljust(ljust_width)} : ₹{subtotal:.2f}")
print(f"{'Discount'.ljust(ljust_width)} : ₹{discount:.2f}")
print(f"{'After Discount'.ljust(ljust_width)} : ₹{after_discount:.2f}")
print(f"{'Tax'.ljust(ljust_width)} : ₹{tax_amount:.2f}")
print(f"{'After Tax'.ljust(ljust_width)} : ₹{after_tax:.2f}")
print(f"{'Cashback'.ljust(ljust_width)} : ₹{cashback:.2f}")

print(f"{'Final Amount'.ljust(ljust_width)} : ₹{final_amount:.2f}")

print(f"{'Payment Received'.ljust(ljust_width)} : {is_payment_received}")
print(f"{'Payment Successful'.ljust(ljust_width)} : {is_payment_successful}")

print()
print('-'*padding)
print()

print("TYPE ANALYSIS")
print()

print(f"{'Product Price'.ljust(ljust_width)} : {type(product_price_float)}")
print(f"{'Quantity'.ljust(ljust_width)} : {type(quantity_int)}")
print(f"{'Discount'.ljust(ljust_width)} : {type(discount)}")
print(f"{'Tax Percentage'.ljust(ljust_width)} : {type(tax_percentage_float)}")
print(f"{'Cashback Percentage'.ljust(ljust_width)} : {type(cashback_percentage)}")
print(f"{'Final Amount'.ljust(ljust_width)} : {type(final_amount)}")
print()
print('='*padding)