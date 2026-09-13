number = 121

temp = number
reverse = 0
is_palindrome = False
while number > 0:
  digit = number % 10
  reverse = reverse * 10 + digit
  number //=  10
is_palindrome = reverse == temp
print(is_palindrome)