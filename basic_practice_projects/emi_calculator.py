# EMIs based on simple interest 
principal = 10000 
rate_of_interest_per_cent = 15
time_in_year = 5
interest = principal * rate_of_interest_per_cent * time_in_year / 100
total_amount_to_be_paid = (principal + interest)
emi_per_month = total_amount_to_be_paid / (time_in_year * 12)
print(f"Emi Per month {emi_per_month:.2f}")

# Emis based on compound interest
principal = p = 10000 
rate_of_interest_anually = 0.15
rate_of_interest_monthly = r = rate_of_interest_anually / 12
time_in_year = 5
number_of_times_interest_is_compounded_in_year = n = 60

# interest calculator formula
interest = p * r * (1 + r)**n / ((1 + r)**n - 1)

print(f"Emis per month{interest:.2f}")
