patient_name = "John doe"
room_charges = 500
doctor_charges = 1000
medicine_charges = 500
lab_charges = 1500

total_before_tax =  room_charges + doctor_charges + medicine_charges + lab_charges
print(total_before_tax)

gst = 0.18

total_after_tax = total_before_tax * (1 + gst )
print(total_after_tax)

print("-----------------------")
print("-----------------------")
print(f"Patent name : {patient_name}")
print(f"Room charges : {room_charges}")
print(f"Doctor fee : {doctor_charges}")
print(f"Medicine charges : {medicine_charges}")
print(f"Lab charges : {lab_charges}")
print("")
print(f"Total ( before tax ) : {total_before_tax}")
print("")
print(f"GST : {gst*100}%")
print("")
print(f"Total ( after tax ) : {total_after_tax}")
print("-----------------------")
print("-----------------------")