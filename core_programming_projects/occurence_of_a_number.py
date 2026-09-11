list1 = [10, 20, 10, 30, 10, 40, 50]
target = 10
count = 0

for item in list1:
  if item == target:
    count += 1

print(f"{target} appears {count} times")