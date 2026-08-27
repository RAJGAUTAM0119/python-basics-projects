customer_name = "   rAj gAUtaM   "
normalized_customer_name = " ".join(customer_name.strip().split()).title()
account_id = " ACC-1025 "
account_balance = "15000.50"
account_balance_float = float(account_balance)
transaction_amount = 2500.75
remaining_balance = account_balance_float - transaction_amount
minimum_balance = 5000
is_minimum_balance_maintained = remaining_balance >= minimum_balance
is_sufficient_balance = account_balance_float >= minimum_balance
is_transaction_possible = account_balance_float >= transaction_amount
is_account_active = True
is_verified = "True"

is_data_consistent = type(account_balance) == str and type(minimum_balance) == int and type(transaction_amount) == float and type(is_account_active) == bool and type(is_verified) == str

is_transaction_safe = is_account_active and is_verified and is_sufficient_balance and is_transaction_possible and is_minimum_balance_maintained

padding = 40
ljust_width = 25



print('='*padding)
print('ACCOUNT CONSISTENCY ANALYZER'.center(padding))
print('='*padding)
print()

print(f"{'Customer Name'.ljust(ljust_width)} : {normalized_customer_name}")
print(f"{'Account ID'.ljust(ljust_width)} : {account_id.strip()}")
print()
print(f"{'Account Balance'.ljust(ljust_width)} : ₹{account_balance_float:.2f}")
print(f"{'Minimum Balance'.ljust(ljust_width)} : ₹{minimum_balance:.2f}")
print(f"{'Transaction Amount'.ljust(ljust_width)} : ₹{transaction_amount:.2f}")
print()
print('-'*padding)
print()
print(f"{'Account Active'.ljust(ljust_width)} : {is_account_active}")
print(f"{'Account Verified'.ljust(ljust_width)} : {is_verified}")

print(f"{'Sufficient Balance'.ljust(ljust_width)} : {is_sufficient_balance}")
print(f"{'Transaction Possible'.ljust(ljust_width)} : {is_transaction_possible}")

print(f"{'Remaining Balance'.ljust(ljust_width)} : ₹{account_balance_float - transaction_amount}")
print(f"{'Minimum Maintained'.ljust(ljust_width)} : {is_minimum_balance_maintained}")

print()
print('-'*padding)
print()
print('DATA CONSISTENCY')
print()
print(f"{'Balance Type'.ljust(ljust_width)} : {type(account_balance)}")
print(f"{'Minimum Type'.ljust(ljust_width)} : {type(minimum_balance)}")
print(f"{'Transaction Type'.ljust(ljust_width)} : {type(transaction_amount)}")
print(f"{'Active Type'.ljust(ljust_width)} : {type(is_account_active)}")
print(f"{'Verification Type'.ljust(ljust_width)} : {type(is_verified)}")
print() 
print(f"{'Data Consistent'.ljust(ljust_width)} : {is_data_consistent}")


print()
print('-'*padding)
print()
print(f"{'TRANSACTION SAFE'.ljust(ljust_width)} : {is_transaction_safe}")

print()
print('='*padding)