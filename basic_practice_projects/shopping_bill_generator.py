meal = 500 * 1
tshirt = 399 * 4
shirt = 999 * 2
pc = 200000 * 1
keyboard = 3500 * 1
mouse = 1200 * 1

total_before_tax = meal + tshirt + shirt + pc + keyboard + mouse
gst = 0.18
total_after_tax = total_before_tax + (gst * total_before_tax)

print(f"Your total bill is {total_after_tax}")