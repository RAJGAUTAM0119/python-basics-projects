username = "  Raj_Gautam23  "
is_username_valid = len(username.strip()) >= 8 and username.strip().__contains__('_')

email = "  raj.gautam23@gmail.com  "
is_email_valid = email.strip() and email.strip().__contains__('@') and email.strip().endswith(".com")

country = "  iNdIa  "
is_country_valid = country.strip().title() == "India"

age = 23
is_age_valid = age >= 18

password = "Raj@12345"
is_password_valid = len(password) >= 8 and "@" in password and any(char.isdigit() for char in password
 )

padding = 40
ljust_width = 15

print("="*padding)
print("ACCOUNT VALIDATION".center(padding))
print("="*padding)
print()
print(f"{"Username Valid".ljust(ljust_width)} : {is_username_valid}")
print(f"{"Email Valid".ljust(ljust_width)} : {is_email_valid}")
print(f"{"Country Valid".ljust(ljust_width)} : {is_country_valid}")
print(f"{"Age Valid".ljust(ljust_width)} : {is_age_valid}")
print(f"{"Password Valid".ljust(ljust_width)} : {is_password_valid}")
print()
print("-"*padding)
print() 

is_account_valid = is_username_valid and is_email_valid and is_country_valid and is_age_valid and is_password_valid
print(f"{"Account Valid".ljust(ljust_width)} : {is_account_valid}")
print()
print("="*padding)