password_attempts = [
    "",
    "abc",
    "hello",
    "raj123",
    "python99",
    "admin123",
    "secret123"
]

empty_attempts_skiped = 0
invalid_attempts = 0
failed_attempts = 0
attempts_actualy_processed = 0
is_login_successful = None
successfull_attempts = 0

for password in password_attempts:
  
  if password == '' :
    empty_attempts_skiped += 1
    continue
  elif len(password) < 6 :
    invalid_attempts += 1
    continue
  elif "admin123" == password :
    is_login_successful = True
    attempts_actualy_processed += 1
    successfull_attempts += 1
    break

  else:
    attempts_actualy_processed += 1
    failed_attempts += 1
  
ljust_width = 25
padding = 40
print("="*padding)
print(f"{"LOGIN ATTEMPT ANALYZER".center(padding)}")
print("="*padding)
print()
print(f"{"Empty Attempts Skipped".ljust(ljust_width)} : {empty_attempts_skiped}")
print(f"{"Invalid Attempts".ljust(ljust_width)} : {invalid_attempts}")
print(f"{"Failed Attempts".ljust(ljust_width)} : {failed_attempts}")
print(f"{"Attempts Processed".ljust(ljust_width)} : {attempts_actualy_processed}")

print(f"{"Login Successful".ljust(ljust_width)} : {is_login_successful}")
print(f"{"Successful Attempt".ljust(ljust_width)} : {successfull_attempts}")
print()
print("="*padding)