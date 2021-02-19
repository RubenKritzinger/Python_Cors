#7-4


prompt = "\nChoose a topping: cheese, sweet chilli, chicken"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt)
if message != 'quit':
	print(message)



#7-5


prompt = "\nHow old are you?"
prompt += "\nEnter '0' to end the program."
while input != 0:
	age = int(input(prompt))

	if age > 0 and age < 3:
		print("\nThe ticket is free.")
	elif age >= 3 and age < 12:
		print("\nThe ticket is $10.")
	elif age > 12: 
		print("\nThe ticket is $15")

	if age == 0:
		break



#7-6





prompt = "\nHow old are you?"
prompt += "\nEnter '0' to end the program."
while input != 0:
	age = int(input(prompt))
	if age > 0 and age < 3:
		print("\nThe ticket is free.")
	elif age >= 3 and age < 12:
		print("\nThe ticket is $10.")
	elif age > 12:
		print("\nThe ticket is $15")
	if age == 0:
		break


#7-7
prompt = "\nHow old are you?"
prompt += "\nEnter '0' to end the program."

active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print(message)