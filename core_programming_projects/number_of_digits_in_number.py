num = 765432
digit_count = 0
while num != 0:
  digit_count += 1
  num = num // 10
print(f"Total digits are : {digit_count}")