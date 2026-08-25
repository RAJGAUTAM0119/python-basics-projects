usd_amount = 50

usd_to_inr = 95

inr_amount = usd_amount * usd_to_inr

distance_in_km = 50.001
distance_in_meters = distance_in_km * 1000
distance_in_miles = (distance_in_km * 0.621371)

is_inr_greater_than_20000 = inr_amount > 20000
is_distance_greater_than_40 = distance_in_km >= 40
is_range_40_50_km = 40 <= distance_in_km <= 50
is_usd_amount_zero = usd_amount == 0

padding = 40
ljust_width = 20

print("="*padding)
print("TRAVEL CONVERSION REPORT".center(padding))
print("="*padding)
print()
print(f"{"USD Amount".ljust(ljust_width)} : ${usd_amount  }")
print(f"{"INR Amount".ljust(ljust_width)} : ₹{inr_amount:.2f}")
print()
print(f"{"Distance KM".ljust(ljust_width)} : {distance_in_km:.2f}")
print(f"{"Distance Meters".ljust(ljust_width)} : {distance_in_meters:.2f}")
print(f"{"Distance Miles".ljust(ljust_width)} : {distance_in_miles:.2f}")
print()
print("-"*padding)
print()
print(f"{"INR > ₹20000".ljust(ljust_width)} : {is_inr_greater_than_20000}")
print(f"{"Distance >= 40KM".ljust(ljust_width)} : {is_distance_greater_than_40}")
print(f"{"40-50 KM Range".ljust(ljust_width)} : {is_range_40_50_km}")
print(f"{"USD Amount = 0".ljust(ljust_width)} : {is_usd_amount_zero}")
print()
print("="*padding)