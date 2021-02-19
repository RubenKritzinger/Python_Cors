with open('pi_digits.txt') as file_object:
	contents = file_object.read()
print(contents)

print(contents.rstrip())

file_path = 'C:/Users/User/Desktop/python/python_work/chapter10/pi_digits.txt'
with open(file_path) as file_object:
	contents = file_object.read()
print(contents)