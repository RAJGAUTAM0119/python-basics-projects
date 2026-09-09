numbers = [5, 12, 25, 8, 40, 75, 150, 60, 90]

skipped_numbers = 0
processed_numbers = 0
sum_of_processed_number = 0
is_stopped_by_large_number = False
first_processed_number = 0

for i in range(len(numbers)):
  number = numbers[i]

  if (number < 10):
    skipped_numbers += 1
    continue
  elif(number > 100):
    # skipped_numbers += 1
    is_stopped_by_large_number = True
    break
  else:
    if(not first_processed_number):
        first_processed_number = number
    processed_numbers += 1
    sum_of_processed_number += number
    
ljust_width = 20
print(f"{"Processed Count".ljust(ljust_width)} : {processed_numbers}")
print(f"{"Processed Sum".ljust(ljust_width)} : {sum_of_processed_number}")
print(f"{"First Processed Number".ljust(ljust_width)} : {first_processed_number}")
print(f"{"Skipped Numbers".ljust(ljust_width)} : {skipped_numbers}")
print(f"{"Stopped By Large Number".ljust(ljust_width)} : {is_stopped_by_large_number}")