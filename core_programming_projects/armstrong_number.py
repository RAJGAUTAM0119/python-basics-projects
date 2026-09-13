n = int(input("Enter a number : ")) #153

temp = n
armstrong = 0
is_armstrong = False
 
while n > 0:
  digit = n % 10
  armstrong = armstrong + digit ** 3
  n = n // 10
is_armstrong = armstrong == temp

print(is_armstrong)