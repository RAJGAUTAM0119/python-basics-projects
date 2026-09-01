temperatures = [32, 35, 38, 41, 39, 46, 42, 37]

normal_readings = 0
warning_readings = 0
invalid_readings = 0
processed_readings = 0
critical_condition_occured = False
highest_temperature = 0
total_of_all_normal_temperature = 0

for temp in temperatures:
  processed_readings += 1
  if temp < 20:
    invalid_readings += 1
    continue
  elif 20 <= temp <= 40:
    normal_readings += 1
    total_of_all_normal_temperature += temp
    continue
  elif 41 <= temp <= 45:
    warning_readings += 1
    continue
  else:
    highest_temperature = temp
    critical_condition_occured = True
    break
 

padding = 40
ljust_width = 25
print('='*padding)
print('SENSOR MONITORING SYSTEM'.center(padding))
print('='*padding)
print()
print(f"{"Normal Reading".ljust(ljust_width)} : {normal_readings}")
print(f"{"Warning Readings".ljust(ljust_width)} : {warning_readings}")
print(f"{"Invalid Readings".ljust(ljust_width)} : {invalid_readings}")
print(f"{"Processed Readings".ljust(ljust_width)} : {processed_readings}")

print(f"{"Highest Temperature".ljust(ljust_width)} : {highest_temperature}")
print(f"{"Normal Temperature Sum".ljust(ljust_width)} : {total_of_all_normal_temperature}")

print(f"{"Critical Detected".ljust(ljust_width)} : {critical_condition_occured}")
print()
print('='*padding)