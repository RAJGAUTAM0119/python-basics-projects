a = 10
b = 2.5
c = True
d = "10"


padding = 40 
ljust_width = 20


print('='*padding)
print('EXPRESSION TYPE DETECTIVE'.center(padding))
print('='*padding)
print()

print(f"{'EXPRESSION'.ljust(ljust_width)} {'RESULT'.ljust(ljust_width)} {'TYPE'.ljust(ljust_width)}")
print()

print(f"{'a + b'.ljust(ljust_width)} {(a + b)} {str(type(a+b)).rjust(ljust_width + 11)}")
print(f"{'a - b'.ljust(ljust_width)} {(a - b)} {str(type(a-b)).rjust(ljust_width + 11)}")
print(f"{'a * b'.ljust(ljust_width)} {(a * b)} {str(type(a*b)).rjust(ljust_width + 11)}")
print(f"{'a / b'.ljust(ljust_width)} {(a / b)} {str(type(a/b)).rjust(ljust_width + 11)}")
print(f"{'a // b'.ljust(ljust_width)} {(a // b)} {str(type(a//b)).rjust(ljust_width + 11)}")
print(f"{'a ** b'.ljust(ljust_width)} {(a ** b):.2f} {str(type(a**b)).rjust(ljust_width + 11)}")

print(f"{'a > b'.ljust(ljust_width)} {(a > b)} {str(type(a>b)).rjust(ljust_width + 11)}")
print(f"{'a == b'.ljust(ljust_width)} {(a == b)} {str(type(a==b)).rjust(ljust_width + 11)}")
print(f"{'c == 1'.ljust(ljust_width)} {(c == 1)} {str(type(c==1)).rjust(ljust_width + 11)}")
print(f"{'c + a'.ljust(ljust_width)} {(c + a)} {str(type(c + a)).rjust(ljust_width + 11)}")
print(f"{'bool(a)'.ljust(ljust_width)} {(bool(a))} {str(type(bool(a))).rjust(ljust_width + 11)}")
print(f"{'bool(0)'.ljust(ljust_width)} {(bool(0))} {str(type(bool(0))).rjust(ljust_width + 11)}")

print(f"{'d + "5"'.ljust(ljust_width)} {(d + "5")} {str(type(d + "5")).rjust(ljust_width + 11)}")
print(f"{'d * 3'.ljust(ljust_width)} {(d * 3)} {str(type(d * 3)).rjust(ljust_width + 11)}")
