full_name = "  Raj    Gautam   "
age = 21
height = 175.5
is_student = True
monthly_income = "85000"
phone_number = "9821628393"

padding = 40
ljust_width = 20


print('='*padding)
print("PERSONAL DATA REPORT".center(padding))
print('='*padding)
print()
print(f"{"Full Name".ljust(ljust_width)} : {" ".join(full_name.strip().split()).title()}")
print(f"{"Age".ljust(ljust_width)} : {age}")
print(f"{"Height".ljust(ljust_width)} : {height}")
print(f"{"Student".ljust(ljust_width)} : {is_student}")
print(f"{"Income".ljust(ljust_width)} : {monthly_income}")
print(f"{"Phone".ljust(ljust_width)} : {phone_number}")
print()
print('-'*padding)
print()

print(f"{"Name".ljust(ljust_width)} : {type(full_name)}")
print(f"{"Age".ljust(ljust_width)} : {type(age)}")
print(f"{"Height".ljust(ljust_width)} : {type(height)}")
print(f"{"Student".ljust(ljust_width)} : {type(is_student)}")
print(f"{"Income".ljust(ljust_width)} : {type(monthly_income)}")
print(f"{"Phone".ljust(ljust_width)} : {type(phone_number)}")
print()
print('-'*padding)
print()

print(f"{"Income (int)".ljust(ljust_width)} : {int(monthly_income)}")
print(f"{"Age (float) ".ljust(ljust_width)} : {float(age)}")
print(f"{"Height (int)".ljust(ljust_width)} : {int(height)}")
print(f"{"Student (int)".ljust(ljust_width)} : {int(is_student)}")
print()
print('='*padding)