people = {'first_name': 'pieter', 'last_name': 'vd_walt', 'age': '19','city': 'pretoria'}
print(people)
print(people['first_name'])
print(people['last_name'])
print(people['age'])
print(f"{people['city']}\n")


people2 = {'first_name': 'jonny', 'last_name': 'voerie', 'age': '22','city': 'jobirg'}
print(people2)
print(people2['first_name'])
print(people2['last_name'])
print(people2['age'])
print(f"{people2['city']}\n")


people3 = {'first_name': 'johan', 'last_name': 'kritzinger', 'age': '23','city': 'stilbaai'}
print(people3)
print(people3['first_name'])
print(people3['last_name'])
print(people3['age'])
print(f"{people3['city']}\n")

#6-8
pets = {'owners_name': 'johan', 'animal': 'dog', 'animal_name': 'jok'}
print(pets)
print(pets['owners_name'])
print(pets['animal'])
print(f"{pets['animal_name']}\n")


pets2 = {'owners_name': 'pieter', 'animal': 'cat', 'animal_name': 'bongo'}
print(pets2['owners_name'])
print(pets2['animal'])
print(f"{pets2['animal_name']}\n")


#6-9
favorite_places = {'pieter': 'US', 'adam': 'Australia', 'jonny': 'Dubai'}
print(favorite_places['pieter'])
print(favorite_places['adam'])
print(f"{favorite_places['jonny']}\n")

Favorite_Numbers = {'pieter': '14' '12' ,'paul': '112''147', 'deno': '27''22','jhon': '8''3','jonnie':'30''21'}
print(Favorite_Numbers['pieter'])
print(Favorite_Numbers['paul'])
print(Favorite_Numbers['deno'])
print(Favorite_Numbers['jhon'])
print(f"{Favorite_Numbers['jonnie']}\n")

#6-10
Favorite_Numbers = {'pieter': '14' '12' ,'paul': '112''147', 'deno': '27''22','jhon': '8''3','jonnie':'30''21'}
print(Favorite_Numbers['pieter'])
print(Favorite_Numbers['paul'])
print(Favorite_Numbers['deno'])
print(Favorite_Numbers['jhon'])
print(f"{Favorite_Numbers['jonnie']}\n")

#6-11
cities = {
	'santiago':{
		'country': 'cchile',
		'population' :6158080,
		'nearby mountains': 'andes',
		},
	'talkeetna':{
		'country': 'alaska',
		'population' :987,
		'nearby mountains': 'alaska range',
		},
	'katamandu':{
		'country': 'nepal',
		'population' :103285,
		'nearby mountains': 'himilaya',
		}
	}
	
for city,city_info in cities.items():
	country = city_info['country'].title()
	population = city_info['population']
	mountains = city_info['nearby mountains'].title()

	print("\n" + city.title() + "is in" + country + ".")
	print("it is a population of about " + str(population) + ".")
	print("the" + mountains + "mountains are nearby.")