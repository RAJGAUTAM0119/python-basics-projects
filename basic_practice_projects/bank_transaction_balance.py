initial_balance = 5000
deposit = 1000
withdrawal = 500
cashback_percentage = 10
transaction_fee = 10

balance_after_deposit = initial_balance + deposit
balance_after_withdrawal = balance_after_deposit - withdrawal
cashback_earned = withdrawal * cashback_percentage / 100

final_balance = balance_after_withdrawal + cashback_earned - transaction_fee

is_positive = final_balance > 0

padding = 42
padding2 = 25

print(f"{"="*padding}")
print(f"{"BANK TRANSACTION SUMMARY".center(padding)}")
print(f"{"="*padding}")
print()
print(f"{"Initial Balance".ljust(padding2)} : Rs {initial_balance}")
print(f"{"Deposit".ljust(padding2)} : Rs {deposit}")
print(f"{"Withdrawal".ljust(padding2)} : Rs {withdrawal}")
print()
print(f"{"Balance after deposit".ljust(padding2)} : Rs {balance_after_deposit}")
print(f"{"Balance after withdrawal".ljust(padding2)} : Rs {balance_after_withdrawal}")
print()
print(f"{"CashBack Percentage".ljust(padding2)} : Rs {cashback_percentage}")
print(f"{"Cashback earned".ljust(padding2)} : Rs {cashback_earned}")
print()
print(f"{"Transaction Fee".ljust(padding2)} : Rs {transaction_fee}")
print()
print(f"{"-"*padding}")
print()

print(f"{"Final balance".ljust(padding2)} : Rs {final_balance}")
print(f"{"Is balace positive".ljust(padding2)} : {is_positive}")
print()
print(f"{"="*padding}")