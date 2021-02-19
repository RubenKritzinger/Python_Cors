user_names = ['jon' , 'piet' , 'sarie' , 'admin'  ]
name = 'leonardo'

if name == 'admin':
	print(f"Hello {name.title()},would you like to see a status report?")
elif name != 'admin':
	print(f"Hello {name.title()}, thank you for logging in again")
else:
	print("Invalid user")

#5-9

usernames =[]
length = len(usernames)
if length < 1:
 	print("We need to find some users!")
else:
	print("Invalid user")

#5-10
current_users = ['Courtney', 'Ruben', 'Tash', 'Anjee', 'Mpho']

new_users = ['Danee', 'Shannon', 'Kyle', 'Tash', 'Ruben']

user = 'Tash'
if current_users == new_users:
	print("Username is available")
elif current_users != new_users:
	print("Need to enter a new username")
else:
	print("Invalid user!")

current_users = ['courtney', 'ruben', 'tash', 'anjee', 'mpho']

for users in current_users:
	 if users == 'courtney':
	 	print(users.upper())
	 else:
	 	print(users.title())
#5-11

ordinal_numbers = [1, 2, 3, '4th', '5th', '6th', '7th', '8th', '9th']

for numbers in ordinal_numbers:
	 if numbers == 'courtney':
	 	print(users.upper())
	 else:
	 	print(users.title())

ordinal_numbers = '4th'

if ordinal_numbers == '4th':
	print("You have earned 5 points")
elif alienColour == 'yellow':
	print("You have earned 10 points")
elif alienColour == 'red':
	print("You have earned 15 points")
else:
	print("Invalid colour!")