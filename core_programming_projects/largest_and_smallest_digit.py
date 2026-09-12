num = 75869

min = num
max = 0

while num > 0:
  digit = num % 10
  num = num // 10
  # min = digit
  if(digit > max):
    max = digit
  elif(digit < min):
    min = digit
  else:
    pass
print(f"Minimum Value is : {min}")
print(f"Maximum Value is : {max}")