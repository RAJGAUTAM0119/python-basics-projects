product_name = "Mechanical Keyboard"

base_price = 2500
discount_percentage = 12.5
quantity = 3
tax_percentage = "18"
tax_percentage_int = int(tax_percentage)
is_member = True

subtotal = base_price * quantity
discount_amount = subtotal * discount_percentage / 100
after_discount = subtotal - discount_amount
tax_amount = after_discount * tax_percentage_int / 100
final_price = after_discount + tax_amount

padding = 40
ljust_width = 20


print("="*padding)
print('PRICE TYPE ANALYZER'.center(padding))
print("="*padding)
print()
print(f"{"Product".ljust(ljust_width)} : {product_name}")
print(f"{"Base Price".ljust(ljust_width)} : ₹{base_price}")
print(f"{"Quantity".ljust(ljust_width)} : {quantity}")
print(f"{"Discount".ljust(ljust_width)} : {discount_percentage}%")
print(f"{"Tax".ljust(ljust_width)} : {tax_percentage_int}%")
print()
print('-'*padding)
print()

print(f"{"Subtotal".ljust(ljust_width)} : ₹{subtotal:.2f}")
print(f"{"Discount Amount".ljust(ljust_width)} : ₹{discount_amount:.2f}")
print(f"{"After Discount".ljust(ljust_width)} : ₹{after_discount:.2f}")
print(f"{"Tax Amount".ljust(ljust_width)} : ₹{tax_amount:.2f}")
print(f"{"Final Price".ljust(ljust_width)} : ₹{final_price:.2f}")
print()
print('-'*padding)
print()

print("TYPE ANALYSIS")
print(f"{"Base Price".ljust(ljust_width)} : {type(base_price)}")
print(f"{"Discount".ljust(ljust_width)} : {type(discount_percentage)}")
print(f"{"Quantity".ljust(ljust_width)} : {type(quantity)}")
print(f"{"Tax Percentage".ljust(ljust_width)} : {type(tax_percentage)}")
print(f"{"Membership".ljust(ljust_width)} : {type(is_member)}")
print()
print(f"{"Subtotal".ljust(ljust_width)} : {type(subtotal)}")
print(f"{"Discount Amount".ljust(ljust_width)} : {type(discount_amount)}")
print(f"{"After Discount".ljust(ljust_width)} : {type(after_discount)}")
print(f"{"Tax Amount".ljust(ljust_width)} : {type(tax_amount)}")
print(f"{"Final Price".ljust(ljust_width)} : {type(final_price)}")

print()
print('-'*padding)
print()
print(f"{"Membership Value".ljust(ljust_width)} : {bool(is_member)}")