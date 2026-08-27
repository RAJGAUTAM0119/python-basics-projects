full_name = "   rAj     gAutAm   "
normalized_full_name = " ".join(full_name.strip().split()).title()
is_full_name_valid = normalized_full_name != ""

username = "   Raj_Gautam23   "
normalized_username = username.strip()
is_username_valid = len(normalized_username) >= 8 and '_' in normalized_username

email = "   RAJ.GAUTAM23@GMAIL.COm   "
normalized_email = email.strip().lower()
is_email_valid = "@" in normalized_email and normalized_email.endswith('.com')

phone = "   9821628393   "
normalized_phone = int(phone.strip())
is_phone_valid = len(str(normalized_phone)) == 10

age = "21"
normalized_age = int(age.strip())
is_age_valid = 18 <= normalized_age <= 60

balance = "12500.75"
normalized_balance = float(balance.strip())
is_balance_valid = normalized_balance >= 1000

country = "   iNdIa   "
normalized_country = " ".join(country.strip().split()).title()
is_country_valid = normalized_country == "India"

is_verified = True

is_low_risk_account = normalized_age >= 18 and normalized_balance >= 10000 and is_verified and normalized_country == "India"

is_account_eligible = is_full_name_valid and is_username_valid and is_email_valid and is_phone_valid and is_age_valid and is_balance_valid and is_country_valid and is_verified


padding = 40
ljust_width = 20


print('='*padding)
print("REGISTRATION DATA ANALYZER".center(padding))
print('='*padding)
print()
print('PERSONAL INFORMATION')
print()
print(f"{"Name".ljust(ljust_width)} : {normalized_full_name}")
print(f"{"Username".ljust(ljust_width)} : {normalized_username}")
print(f"{"Email".ljust(ljust_width)} : {normalized_email}")
print(f"{"Phone".ljust(ljust_width)} : {normalized_phone}")
print(f"{"Age".ljust(ljust_width)} : {normalized_age}")
print(f"{"Country".ljust(ljust_width)} : {normalized_country}")
print(f"{"Balance".ljust(ljust_width)} : ₹{normalized_balance}")
print(f"{"Verified".ljust(ljust_width)} : {is_verified}")

print()
print('-'*padding)
print()

print('VALIDATION')
print()

print(f"{"Name Valid".ljust(ljust_width)} : {is_full_name_valid}")
print(f"{"Username Valid".ljust(ljust_width)} : {is_username_valid}")
print(f"{"Email Valid".ljust(ljust_width)} : {is_email_valid}")
print(f"{"Phone Valid".ljust(ljust_width)} : {is_phone_valid}")
print(f"{"Age valid".ljust(ljust_width)} : {is_age_valid}")
print(f"{"Balance Valid".ljust(ljust_width)} : {is_balance_valid}")
print(f"{"Country Valid".ljust(ljust_width)} : {is_country_valid}")
print(f"{"Verified".ljust(ljust_width)} : {is_verified}")

print()
print('-'*padding)
print()

print("USERNAME ANALYSIS")
print()

print(f"{"Has Underscore".ljust(ljust_width)} : {"_" in normalized_username}")
print(f"{"Length Valid".ljust(ljust_width)} : {len(normalized_username) >= 8}")

print(f"{"Original Type".ljust(ljust_width)} : {type(username)}")
print(f"{"Cleaned Type".ljust(ljust_width)} : {type(normalized_username)}")

print()
print('-'*padding)
print()
print('NUMERIC INTEGRITY')
print()

print(f"{"Age Original Type".ljust(ljust_width)} : {type(age)}")
print(f"{"Age Converted".ljust(ljust_width)} : {type(normalized_age)}")

print(f"{"Balance Original".ljust(ljust_width)} : {type(balance)}")
print(f"{"Balance Converted".ljust(ljust_width)} : {type(normalized_balance)}")

# ------------------------------------------------
print()
print('-'*padding)
print()
print('ACCOUNT STATUS')
print()

print(f"{"Account Eligibility".ljust(ljust_width)} : {is_account_eligible}")
print(f"{"Low Risk Account".ljust(ljust_width)} : {is_low_risk_account}")

print()
print('='*padding)
print()