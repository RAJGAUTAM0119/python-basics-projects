num = 76543
num2 = num

reversed_num = 0

while num != 0:
  digit = num % 10
  reversed_num = reversed_num * 10 + digit
  num = num // 10

print(f"The reverse of the number {num2} is {reversed_num}")