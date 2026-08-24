customer_name = "  raj gautam  "
hotel_name = "  grand palace hotel  "

room_price_per_night = 3500
number_of_nights = 4

room_cost = room_price_per_night * number_of_nights 

discount_percentage = 10
service_charge_percentage = 5
tax_percentage = 18

discount_amount = room_cost * discount_percentage / 100 

discounted_room_cost = room_cost - discount_amount 

service_charge = discounted_room_cost * service_charge_percentage / 100 

cleaning_fee = 500

taxable_amount = discounted_room_cost + service_charge + cleaning_fee 

tax = taxable_amount * tax_percentage / 100

final_cost = taxable_amount + tax

is_high_value_booking = final_cost >= 15000

padding = 40
ljust_width = 25

print("="*padding)
print("HOTEL BOOKING SUMMARY".center(padding))
print("="*padding)

print()
print(f"{"Customer Name".ljust(ljust_width)} : {" ".join(customer_name.strip().split()).title()}")
print(f"{"Hotel".ljust(ljust_width)} : {" ".join(hotel_name.strip().split()).title()}")
print()

print(f"{"Room Price Per Night".ljust(ljust_width)} : ₹{room_price_per_night}")

print(f"{"Number of Nights".ljust(ljust_width)} : {number_of_nights}")
print()
print("-"*padding)
print()


print(f"{"Room Cost".ljust(ljust_width)} : ₹{room_cost}")
print(f"{"Discount (10%)".ljust(ljust_width)} : ₹{discount_amount}")
print(f"{"After Discount".ljust(ljust_width)} : ₹{discounted_room_cost}")
print()
print(f"{"Service Charge".ljust(ljust_width)} : ₹{service_charge}")
print(f"{"Cleaning Fee".ljust(ljust_width)} : ₹{cleaning_fee}")
print(f"{"Taxable Amount".ljust(ljust_width)} : ₹{taxable_amount}")
print()
print(f"{"Tax (18%)".ljust(ljust_width)} : ₹{tax}")
print()
print("-"*padding)
print()
print(f"{"Final Cost".ljust(ljust_width)} : ₹{final_cost}")
print(f"{"High Value Booking".ljust(ljust_width)} : {is_high_value_booking}")
print()
print("="*padding)