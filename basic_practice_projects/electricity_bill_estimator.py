unit_used = 200
rate_per_unit = 3.5

energy_cost = unit_used * rate_per_unit
gst = 0.18

total = energy_cost + energy_cost * gst
print(f"Total unit used {unit_used} and Rate Per Unit {rate_per_unit}")
print(f"Total money to be paid {total}")