transactions = [0, -200, 1500, 3000, 750, 12000, 5000]

is_big_transaction = False
skipped_transaction = 0
transaction_checked = 0
first_valid_transaction = 0

for i in range(len(transactions)):
  transaction_checked += 1
  element = transactions[i]

  if(element <= 0):
    skipped_transaction += 1
    continue
  
  elif(element > 0 and element <= 10000):
    if(not first_valid_transaction):
      first_valid_transaction = element
    continue
  
  elif(element > 10000):
      is_big_transaction = True
      break


print(f"First Valid Transaction : ₹{first_valid_transaction}")
print(f"Transactions Checked : {transaction_checked}")
print(f"Skipped Transactions : {skipped_transaction}")
print(f"Stopped By Large Amount : {is_big_transaction}")