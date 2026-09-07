# slots = [1, 1, 1, 1, 0, 1, 0, 0]
# slots = [1, 1, 0, 1, 0]
# slots = [1, 1, 1, 1]
slots = [0, 1, 1]
slots_checked = 0
first_available_slot = -1

is_slot_found = False

for i in range(len(slots)):
  slots_checked += 1
  element = slots[i]
  if(element == 0):
    first_available_slot = i
    is_slot_found = True
    break
  
print(f"First available slot : {first_available_slot}")
print(f"Slots checked : {slots_checked}")
print(f"Slots found : {is_slot_found}")