employee_id = "EMP001"
employee_first_name  = "Raj"
employee_last_name = "Gautam"
employee_age = 23
employee_gender = "Male"
employee_email = "rajgautam0119@gmail.com"
employee_phone = "9821628393"
employee_company = "Uber"
employee_department = "Artificial Intelligence & Machine Learning"
employee_role = "Junior Ai Engineer"
employee_salary = 120000.0
employee_experience_in_years = 4
employee_city = "Hyderabad"
employee_country = "India"
employee_status = True

# Add spacing to align the output for better readability
level1 = " " * 4
level2 = " " * 8
level3 = " " * 11

print("====================================")
print("           EMPLOYEE ID CARD         ")
print("====================================")
print("")
print(f"Employee ID {level1}: {employee_id}")
print("")
print(f"Name {level3}: {employee_first_name} {employee_last_name}")
print("")
print(f"Department {level1 + " "}: {employee_department}")
print("")
print(f"Role {level3}: {employee_role}")
print("")
print(f"Experience {level1 + " "}: {employee_experience_in_years} Years")
print("")
print(f"Salary {level2 + " "}: ₹{employee_salary}")
print("")
print(f"Company {level2}: {employee_company}")
print("")
print(f"Location {level1 + " "*3}: {employee_city}, {employee_country}")
print("")
print(f"Email {level2 + "  "}: {employee_email}")
print("")
print(f"Phone {level2 + "  "}: {"+91"+employee_phone}")
print("")
print(f"Status {level2 + "  "}: {employee_status}")
print("")