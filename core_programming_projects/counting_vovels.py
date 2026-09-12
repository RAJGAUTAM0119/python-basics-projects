original_string = "Loops are Fun!"
vovel="aeiou"

vovel_count = 0
consonant_count = 0


for char in original_string.lower():
  if char.isalpha():
    if(char in vovel):
      vovel_count += 1
    else:
      consonant_count += 1

print(f"Total vovel in the given string is : {vovel_count}")
print(f"Total consonant in the given string is : {consonant_count}")
