#8-6


def city_country(name, Ruben):
	"""should return a string."""
	place = f"{name} {Ruben}"
	return place.title()

place = city_country('pretoria', 'south africa')
print(f"\"{place}\"")



#8-7


def make_album(artist_name, album_title):
	#should return a dictionary
	album_info = {'name': artist_name, 'title': album_title}
	return album_info

album_info = make_album('youngboy', 'al youngboy 2')
print(album_info)



def make_album(artist_name, album_title):
	#should return a dictionary
	album_info = {'name': artist_name, 'title': album_title}
	return album_info

album_info = make_album('beyonce', 'cater 2 you')
print(album_info)



def make_album(artist_name, album_title):
	'''should return a dictionary'''
	album_info = {'name': artist_name, 'title': album_title}
	return album_info

album_info = make_album('blue magic', 'blue magic')
print(album_info)




#8-8


def make_album(artist_name, album_title):
	'''while loop'''
	album_info = f"{artist_name} {album_title}"
	return album_info.title()

while True:
	print("\nEnter artist and album name:")
	print("(Enter 'quit' at any time to quit)")

	album_info = input("artist_name:")
	if album_info == 'quit':
		break

	album_info = input("album_title:")
	if album_info == 'quit':
		break