#10-1
with open('learning_python.txt') as file_object:
	contents = file_object.read()
print(contents)

filename = 'learning_python.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line)

filename = 'learning_python.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
	for line in lines:
		print(line.rstrip())
#10-2_____________________________________________________________________________________________________________
filename = 'learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    # Get rid of newline, then replace Python with C.
    line = line.rstrip()
    print(line.replace('Python', 'C'))



