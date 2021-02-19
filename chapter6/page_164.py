glossary = {'if_statement': 'looks if condition', 'slice': 'cuts', 'elif': 'if it is another statement','else': 'last if statment','opjects':'Python dictionary'}

for key, value in glossary.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")


#6-5
rivers = {'nile': 'egyp', 'orange river': 'South Africa', 'amazon river': 'south amarica'}
for key, value in rivers.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")

#6-6
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

