user_name = "   rAj    gAutAm   "
age = "21"
age_int = int(age)
height = "175.5"
height_float = float(height)
account_balance = "45890.75"
account_balance_float = float(account_balance)
is_premium = True
completed_orders = 12

padding = 40
ljust_width = 20

print('='*padding)
print('USER DATA NORMALIZER'.center(padding))
print('='*padding)
print()
print(f"{"Name".ljust(ljust_width)} : {" ".join(user_name.strip().split()).title()}")
print(f"{"Age".ljust(ljust_width)} : {age_int}")
print(f"{"Height".ljust(ljust_width)} : {height_float}")
print(f"{"Account Balance".ljust(ljust_width)} : {account_balance_float}")
print(f"{"Premium".ljust(ljust_width)} : {is_premium}")
print(f"{"Completed Orders".ljust(ljust_width)} : {completed_orders}")
print()
print('-'*padding)
print()
print("ORIGINAL TYPES")
print()

print(f"{"Name".ljust(ljust_width)} : {type(user_name)}")
print(f"{"Age".ljust(ljust_width)} : {type(age)}")
print(f"{"Height".ljust(ljust_width)} : {type(height)}")
print(f"{"Balance".ljust(ljust_width)} : {type(account_balance)}")
print(f"{"Premium".ljust(ljust_width)} : {type(is_premium)}")
print(f"{"Orders".ljust(ljust_width)} : {type(completed_orders)}")

print()
print('-'*padding)
print()
print("NORMALIZED TYPES")
print()

print(f"{"Name".ljust(ljust_width)} : {type(user_name)}")
print(f"{"Age".ljust(ljust_width)} : {type(age_int)}")
print(f"{"Height".ljust(ljust_width)} : {type(height_float)}")
print(f"{"Balance".ljust(ljust_width)} : {type(account_balance_float)}")
print(f"{"Premium".ljust(ljust_width)} : {type(is_premium)}")
print(f"{"Orders".ljust(ljust_width)} : {type(completed_orders)}")
print()
print('-'*padding)
print()

print(f"{"Premium Number".ljust(ljust_width)} : {int(is_premium)}")
print(f"{"Orders Text".ljust(ljust_width)} : {str(completed_orders)}")
print('='*padding)