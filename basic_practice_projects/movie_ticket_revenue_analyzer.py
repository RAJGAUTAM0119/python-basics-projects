movie_name = "  avengers:endgame                "

adult_ticket_price = 250
adult_ticket_count = 25
adult_revenue = adult_ticket_price *  adult_ticket_count

children_ticket_price = 150
child_ticket_count = 15
child_revenue =  children_ticket_price * child_ticket_count

food_revenue = 3500
cinema_revenue_sharing_percentage = 60

total_ticket_revenue = adult_revenue + child_revenue

total_revenue_including_food =  food_revenue + total_ticket_revenue

cinema_revenue = total_revenue_including_food * cinema_revenue_sharing_percentage / 100

distributor_revenue = total_revenue_including_food - cinema_revenue

is_successful = total_revenue_including_food > 10000

clean_movie_name = ": ".join(movie_name.strip().split(":")).title()

padding = 42
ljust_width = 20

print("="*padding)
print(f"{"MOVIE REVENUE REPORT".center(padding)}")
print("="*padding)
print()
print(f"{"Movie".ljust(ljust_width)} : {clean_movie_name}")

print()

print(f"{"Adult Ticket".ljust(ljust_width)} : {adult_ticket_count}")
print(f"{"Adult Revenue".ljust(ljust_width)} : ₹{adult_revenue}")

print(f"{"Child Ticket".ljust(ljust_width)} : {child_ticket_count}")
print(f"{"Child Revenue".ljust(ljust_width)} : ₹{child_revenue}")
print()
print("-" * padding)
print()
print(f"{"Ticket Revenue".ljust(ljust_width)} : ₹{total_ticket_revenue}")
print(f"{"Food Revenue".ljust(ljust_width)} : ₹{food_revenue}")
print(f"{"Total Revenue".ljust(ljust_width)} : ₹{total_revenue_including_food}")
print()
print("-"*padding)
print()
print(f"{"Cinema Share".ljust(ljust_width)} : ₹{cinema_revenue}")
print(f"{"Distributor Share".ljust(ljust_width)} : ₹{distributor_revenue}")
print()
print(f"{"Successful".ljust(ljust_width)} : {is_successful}")
print()
print("="*padding)
