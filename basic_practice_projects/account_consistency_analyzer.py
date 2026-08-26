customer_name = "   Raj Gautam   "
account_id = " ACC-1025 "
account_balance = "15000.50"
account_balance_float = float(account_balance)
transaction_amount = 2500.75
remaining_balance = account_balance_float - transaction_amount
minimum_balance = 5000
account_active = True
is_verified = "True"

is_data_consistent = ''
is_transaction_safe = False

padding = 40
ljust_width = 25



print('='*padding)
print('ACCOUNT CONSISTENCY ANALYZER'.center(padding))
print('='*padding)
print()

print(f"{'Customer Name'.ljust(ljust_width)} : {" ".join(customer_name.strip().split()).title()}")
print(f"{'Account ID'.ljust(ljust_width)} : {account_id.strip()}")
print()
print(f"{'Account Balance'.ljust(ljust_width)} : ₹{account_balance_float:.2f}")
print(f"{'Minimum Balance'.ljust(ljust_width)} : ₹{minimum_balance:.2f}")
print(f"{'Transaction Amount'.ljust(ljust_width)} : ₹{transaction_amount:.2f}")
print()
print('-'*padding)
print()
print(f"{'Account Active'.ljust(ljust_width)} : {account_active}")
print(f"{'Account Verified'.ljust(ljust_width)} : {is_verified}")

print(f"{'Sufficient Balance'.ljust(ljust_width)} : {account_balance_float >= minimum_balance}")
print(f"{'Transaction Possible'.ljust(ljust_width)} : {account_balance_float >= transaction_amount}")

print(f"{'Remaining Balance'.ljust(ljust_width)} : ₹{account_balance_float - transaction_amount}")
print(f"{'Minimum Maintained'.ljust(ljust_width)} : {remaining_balance >= minimum_balance}")

print()
print('-'*padding)
print()
print('DATA CONSISTENCY')
print(f"{'Balance Type'.ljust(ljust_width)} : {type(account_balance_float)}")
print(f"{'Minimum Type'.ljust(ljust_width)} : {type(minimum_balance)}")
print(f"{'Transaction Type'.ljust(ljust_width)} : {type(transaction_amount)}")
print(f"{'Active Type'.ljust(ljust_width)} : {type(account_active)}")
print(f"{'Verification Type'.ljust(ljust_width)} : {type(is_verified)}")
print(f"{'Data Consistent'.ljust(ljust_width)} : {is_data_consistent}")


print()
print('-'*padding)
print()
print(f"{''.ljust(ljust_width)} : {is_transaction_safe}")

print()
print('='*padding)  