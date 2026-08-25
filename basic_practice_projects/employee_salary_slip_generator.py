employee_id = "EMP0012"
employee_first_name = "Raj"
employee_last_name = "Gautam"
company_name = "Uber"
designation = "Junior Engineer"
salary_increment = 0.05

basic_salary = 85000.00
bonus = basic_salary * 0.05
gross_salary = basic_salary + bonus
tax = 0.1
total_tax_amount = gross_salary * tax
provident_funds = 1800
professional_tax = 200

total_deduction = total_tax_amount + provident_funds + professional_tax
net_salary = gross_salary - total_deduction
annual_salary = net_salary * 12


print("=======================================")
print("         Monthly Salary Report         ")
print("=======================================")
print()
print(f"Employee Name : {employee_first_name} {employee_last_name}")
print()
print(f"Basic Salary : ₹{basic_salary}")
print()
print(f"Bonus : ₹{bonus}")
print()
print(f"Gross Salary : ₹{gross_salary}")
print()
print(f"Tax (10%) : ₹{total_tax_amount}")
print()
print(f"Provident Fund : ₹{provident_funds}")
print()
print(f"Professional Tax : ₹{professional_tax}")
print()
print("-----------------------------------------")
print()
print(f"Total Deduction : ₹{total_deduction}")
print()
print(f"Net Salary : ₹{net_salary}")
print()
print(f"Annual Salary : ₹{annual_salary}")
print()
print("==========================================")