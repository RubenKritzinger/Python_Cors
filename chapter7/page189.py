#7-8


sandwich_orders = ['chicken sandwich', 'egg sandwich', 'grilled cheese sandwich']
finished_sandwiches = []

while sandwich_orders:
	order = sandwich_orders.pop()

	print(f"I made your {order.title()}.")
	finished_sandwiches.append(order)

# Display all confirmed users.
print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich.title())



#7-9

sandwich_orders = ['pastrami', 'chicken sandwich', 'pastrami', 'egg sandwich', 'pastrami', 'grilled cheese sandwich']
finished_sandwiches = []
print("The deli ran out of pastrami.")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
print(sandwich_orders)

while sandwich_orders:
	order = sandwich_orders.pop()

	print(f"I made your {order.title()}.")
	finished_sandwiches.append(order)

# Display all confirmed users.
print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich.title())


#7-10


dream_vacation = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
	# Prompt for the person's name and response.
	name = input("\nWhat is your name? ")
	response = input("If you could visit one place in the world, where would you go? ")

	# Store the response in the dictionary.
	dream_vacation[name] = response

	# Find out if anyone else is going to take the poll.
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == 'no':
		polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in dream_vacation.items():
	print(f"{name} would like to go to {response}.")