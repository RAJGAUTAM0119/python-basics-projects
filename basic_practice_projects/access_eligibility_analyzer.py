employee_name = "Raj Gautam"
employee_age = 21
employee_experience = 4

is_adult = employee_age >= 18
is_experienced = employee_experience >= 3

employee_is_active = True
employee_is_verified = True
can_access_internal_system = employee_is_active and employee_is_verified
security_training_completed = True

can_access_sensitive_system = employee_is_active and employee_is_verified and security_training_completed and is_experienced

employee_email = "raj@uber.com"
is_company_email = employee_email.endswith("@uber.com")

is_eligible_for_promotion = is_experienced and employee_is_active and employee_is_verified and security_training_completed

employee_position = "developer"
employee_is_manager = employee_position == "manager"
has_manager_experience = employee_experience >= 5


is_privileged_employee = employee_is_verified and ( employee_is_manager or has_manager_experience) 


padding = 40
label_width = 15

print("="*padding)
print(f"{"EMPLOYEE ACCESS ANALYZER".center(padding, " ")}")
print("="*padding)
print()
print(f"{"Employee".ljust(label_width," ")}: {employee_name}")
print(f"{"Age".ljust(label_width," ")}: {employee_age}")
print(f"{"Experience".ljust(label_width, " ")}: {employee_experience} Years")
print()
print(f"{"Adult".ljust(label_width," ")}: {is_adult}")
print(f"{"Experienced".ljust(label_width," ")}: {is_experienced}")
print(f"{"Active".ljust(label_width," ")}: {employee_is_active}")
print(f"{"Verified".ljust(label_width," ")}: {employee_is_verified}")
print(f"{"Training".ljust(label_width," ")}: {security_training_completed}")
print(f"{"Company Email".ljust(label_width," ")}: {is_company_email}")
print()
print("-"*padding)
print()
print(f"{"Internal Access".ljust(label_width + 10, " ")}: {can_access_internal_system}")
print(f"{"Sensitive Access".ljust(label_width + 10, " ")}: {can_access_sensitive_system}")
print(f"{"Promotion Eligibility".ljust(label_width + 10, " ")}: {is_eligible_for_promotion}")
print(f"{"Privileged Employees".ljust(label_width + 10, " ")}: {is_privileged_employee}")
print()
print("="*padding)