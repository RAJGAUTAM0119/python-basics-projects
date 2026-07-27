basic_salary = 50000
house_rent_allowence = basic_salary * 0.5
dearness_allowence = basic_salary * 0.2
bonus = basic_salary * 0.1
provident_fund = basic_salary * 0.05

gross_salary = basic_salary + house_rent_allowence + dearness_allowence + bonus + provident_fund
tax = 0.05

net_salary = gross_salary - (tax + provident_fund) 
 
print(f"Your Gross salary is {gross_salary} after taxation and deduction your net salary is {net_salary}")