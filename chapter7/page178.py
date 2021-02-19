#7-1


prompt = "Let me see if i can find you a Subaru"
prompt += "\nWhat kind of rental car would you like?" 
name = input(prompt)
print(f"\nHello, {name}!")

#7-2

group = input("How many people are in the dinner group?")
group = int(group)

group = 6
if group >= 8:
	print("\nYou'll have to wait for another table.")
else:
	print("\nTable is ready!")


#7-3

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 11 == 0:
	print(f"\nThe number {number} is even.")
else:
	print(f"\nThe number {number} is odd.")
