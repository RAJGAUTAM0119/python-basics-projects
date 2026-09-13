n = int(input("Enter a number : "))
a = 65

for i in range(1,n+1):
  print()
  for j in range(a,i+a):
    print(chr(j),end=" ")
    j += 1

# rows = 5
# ascii_value = 65

# for i in range(rows):
#     letter = chr(ascii_value + i)
#     for j in range(i + 1):
#         print(letter, end=" ")
#     print()