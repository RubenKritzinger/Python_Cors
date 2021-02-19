person_information = {'first_name': 'pieter', 'last_name': 'vd_walt', 'age': '19','city': 'pretoria'}
print(person_information)
print(person_information['first_name'])
print(person_information['last_name'])
print(person_information['age'])
print(person_information['city'])

#6-2
Favorite_Numbers = {'pieter': '14', 'paul': '112', 'deno': '27','jhon': '8','jonnie':'30'}
print(Favorite_Numbers['pieter'])
print(Favorite_Numbers['paul'])
print(Favorite_Numbers['deno'])
print(Favorite_Numbers['jhon'])
print(Favorite_Numbers['jonnie'])


#6-3
glossary = {'if_statement': 'looks if condition', 'slice': 'cuts', 'elif': 'if it is another statement','else': 'last if statment','opjects':'Python dictionary'}
print(f"{glossary['if_statement']}\n")
print(f"{glossary['slice']}\n")
print(f"{glossary['elif']}\n")
print(f"{glossary['else']}\n")
print(f"{glossary['opjects']}\n")

#pg158
for key, value in glossary.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")