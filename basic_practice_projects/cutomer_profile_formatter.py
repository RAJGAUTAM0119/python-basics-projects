customer_name = "   rAj   gAutAm   "
customer_email = "   RAJGAUTAM0119@GMAIL.COM "
customer_city = "   hYDeRaBaD "
customer_country = "   iNdIa "
customer_profession = "   pYtHoN dEvElOpEr "
customer_company = "   uBeR tEcHnOlOgIeS "

clean_name = " ".join(customer_name.strip().title().split()) 
clean_username = "_".join(customer_name.strip().lower().split())
clean_email = " ".join(customer_email.strip().lower().split())
clean_city = " ".join(customer_city.strip().title().split())
clean_country = " ".join(customer_country.strip().title().split())
clean_profession = " ".join(customer_profession.strip().title().split())
clean_company = " ".join(customer_company.strip().title().split())
clean_company_email = f"{".".join(clean_username.split("_"))}{"@"}{clean_company.split()[0].lower()}{".com"}"

title = "CUSTOMER PROFILE"

padding = 42

print("=" * padding)
print(title.center(padding," "))
print("=" * padding)
print()
print(f'{"Name".ljust(15," ")}: {clean_name}')
print()
print(f'{"User Name".ljust(15," ")}: {clean_username}')
print()
print(f"{"Email".ljust(15," ")}: {clean_email}")
print()
print(f"{"Company Email".ljust(15," ")}: {clean_company_email}")
print()
print(f"{"City".ljust(15, " ")}: {clean_city}")
print()
print(f"{"Country".ljust(15," ")}: {clean_country}")
print()
print(f"{"Profession".ljust(15," ")}: {clean_profession}")
print()
print(f"{"Company".ljust(15," ")}: {clean_company}")