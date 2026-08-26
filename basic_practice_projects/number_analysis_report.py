original_number = 256
binary_representation_of_original_number = bin(original_number)
octal_representation_of_original_number = oct(original_number)
hexadecimal_representation_of_original_number = hex(original_number)

addition_in_original_number = original_number + 100
subtraction_in_original_number = original_number - 50
multiplication_in_original_number = original_number * 2
division_in_original_number = original_number / 2
power_of_original_number = original_number ** 2

padding = 40 
ljust_width = 25


print('='*padding)
print('NUMBER ANALYSIS REPORT'.center(padding))
print('='*padding)
print()
print(f"{'Original Number'.ljust(ljust_width)} : {original_number}")
print()
print(f"{'Binary'.ljust(ljust_width)} : {binary_representation_of_original_number}")
print(f"{'Octal'.ljust(ljust_width)} : {octal_representation_of_original_number}")
print(f"{'Hexadecimal'.ljust(ljust_width)} : {hexadecimal_representation_of_original_number}")

print()
print('-'*padding)
print()

print(f"{'+ 100'.ljust(ljust_width)} : {addition_in_original_number}")
print(f"{'- 50'.ljust(ljust_width)} : {subtraction_in_original_number}")
print(f"{'x 2'.ljust(ljust_width)} : {multiplication_in_original_number}")
print(f"{'/ 2'.ljust(ljust_width)} : {division_in_original_number}")
print(f"{'Power 2'.ljust(ljust_width)} : {power_of_original_number}")

print()
print('-'*padding)
print()

print('TYPE ANALYSIS')
print()
print(f"{'Original'.ljust(ljust_width)} : {type(original_number)}")
print(f"{'Division Result'.ljust(ljust_width)} : {type(division_in_original_number)}")
print(f"{'Multiplication Result'.ljust(ljust_width)} : {type(multiplication_in_original_number)}")
print(f"{'Power Result'.ljust(ljust_width)} : {type(power_of_original_number)}")

print()
print('-'*padding)
print()
print(f"{'Greater Than 200'.ljust(ljust_width)} : {original_number > 200}")
print(f"{'Exactly 255'.ljust(ljust_width)} : {original_number == 255}")
print(f"{'Less Than 100'.ljust(ljust_width)} : {original_number < 100}")
print(f"{'Even Number'.ljust(ljust_width)} : {original_number % 2 == 0}")
print()
print('='*padding)