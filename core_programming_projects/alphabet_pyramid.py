rows = 5
ascii_value = 65

for i in range(rows):
    letter = chr(ascii_value + i)
    for j in range(i + 1):
        print(letter, end=" ")
    print()

# Even better version no need of inner loop
rows = 5

for i in range(rows):
    letter = chr(65 + i)
    print((letter + " ") * (i + 1))