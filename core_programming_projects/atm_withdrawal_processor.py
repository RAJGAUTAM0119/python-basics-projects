initial_atm_balance = 10000
atm_balance = 10000

withdrawals = [2000, 0, 3000, 500, 7000, 1000]


approved_withdrawal = 0
skip_withdrawal = 0

total_amount_withdrawn = 0

remaining_atm_balance = 0

is_atm_stopped_early = False


for i in withdrawals:
  if(i <= 0):
    skip_withdrawal += 1
    continue
  elif(i > atm_balance):
    is_atm_stopped_early = True
    break
  else:
    atm_balance -= i
    approved_withdrawal += 1
    total_amount_withdrawn += i
    remaining_atm_balance = atm_balance


padding = 40
ljust_width = 25

print('='*padding)
print('ATM WITHDRAWAL PROCESSOR'.center(padding))
print('='*padding)
print()
print(f"{"Initial Balance".ljust(ljust_width)} : ₹{initial_atm_balance}")
print(f"{"Approved Withdrawals".ljust(ljust_width)} : {approved_withdrawal}")
print(f"{"Skipped Requests".ljust(ljust_width)} : {skip_withdrawal}")
print(f"{"Total Withdrawn".ljust(ljust_width)} : ₹{total_amount_withdrawn}")
print(f"{"Remaining Balance".ljust(ljust_width)} : ₹{atm_balance}")
print()
print(f"{"Stopped Early".ljust(ljust_width)} : {is_atm_stopped_early}")
print()
print('='*padding)