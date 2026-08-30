transactions = [1200, 10, -500, 3000, 0, 750, -200, 6000, 450, 30]

total_accepted_transactions = 0
number_of_accepted_transaction = 0
number_of_skip_transaction = 0
skipped_early = 0


for i in range(len(transactions)):
    if (transactions[i] >= 5000):
        skipped_early = len(transactions) - (i + 1)
        break
    elif (transactions[i] <= 0):
        # print(transactions[i])
        number_of_skip_transaction += 1
        continue
    else:
        total_accepted_transactions += transactions[i]  # 4950
        number_of_accepted_transaction += 1


padding = 40
ljust_width = 25


print('='*padding)
print('TRANSACTION STREAM FILTER'.center(padding))
print('='*padding)

print(f"{"Accepted Transactions".ljust(ljust_width)} : {number_of_accepted_transaction}")
print(f"{"Skipped Transactions".ljust(ljust_width)} : {number_of_skip_transaction + skipped_early}")
print(f"{"Accepted Total".ljust(ljust_width)} : ₹{total_accepted_transactions}")

print(f"{"Stopped Early".ljust(ljust_width)} : {skipped_early}")

print('='*padding)
