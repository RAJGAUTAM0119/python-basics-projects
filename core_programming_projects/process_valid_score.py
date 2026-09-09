scores = [85, -10, 72, 0, 91, 105, 68, 45]

invalid_count = 0
valid_count = 0 
total_valid_score = 0
stopped_by_invalid_greater_than_100 = False

for i in range(len(scores)):
  score = scores[i]

  if(score < 0):
    invalid_count += 1
    continue
  elif(score > 100):
    invalid_count += 1
    stopped_by_invalid_greater_than_100 = True
    break
  else:
    valid_count += 1
    total_valid_score += score
    
ljust_width = 20

print(f"{"Valid Scores".ljust(ljust_width)} : {valid_count}")
print(f"{"Total Valid Score".ljust(ljust_width)} : {total_valid_score}")
print(f"{"Invalid Scores Skipped".ljust(ljust_width)} : {invalid_count}")
print(f"{"Stopped By Invalid >100".ljust(ljust_width)} : {stopped_by_invalid_greater_than_100}")