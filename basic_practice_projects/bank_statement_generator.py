customer_name = "Raj Gautam"
account_number = 23872883
opening_balance = 50000
deposit = 2000
withdraw = 1500

closing_balance = opening_balance + deposit 

# displaying a bank statement
print("----------------------------------")
print("----------------------------------")
print(f"Account Name : {customer_name}")
print(f"Account Number : {account_number}")
print(f"Deposite of rupees : {deposit} and the current balance is {opening_balance + deposit}")
print(f"Withdraw of rupees : {withdraw} and the current balance is {closing_balance - withdraw}")
print("----------------------------------")
print("----------------------------------")