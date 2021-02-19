number = list(range(1, 6))
print(number)

#next
even_numbers = list(range(2 , 11, 2)) 
print(even_numbers)

#next
squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)
print(squares)

#next
squares = []
for value in range(1, 11):
	squares.append(value**2)
print(squares)


#newWork
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

#next
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:])

#next

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title()) 

 #next

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#next
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

    