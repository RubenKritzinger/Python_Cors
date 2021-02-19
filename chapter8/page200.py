#8-3


def make_shirt(size, text):
	"""Display information about my T-shirt."""
	print(f"\nI am a size {size.title()}.")
	print(f"\nThe text that appears on my T-shirt is {text.title()}")

make_shirt(size='16', text='Courtney_13')


#8-4


def make_shirt(size, text='I love Python'):
	"""Display information about my t-shirt."""
	print(f"\nI am a size {size.title()}.")
	print(f"\nThe text that appears on my T-shirt is {text.title()}.")

make_shirt(size='large')


def make_shirt(size, text='I love Python'):
	"""Display information about my t-shirt."""
	print(f"\nI am a size {size.title()}.")
	print(f"\nThe text that appears on my T-shirt is {text.title()}.")

make_shirt(size='medium')


#8-5


def describe_cities(name, country= 'South Africa'):
	#display information about cities.
	print(f"\nPretoria is in {country.title()}.")

describe_cities(name = 'Pretoria')



def describe_cities(name, country= 'Australia'):
	print(f"\nBrisbin is in {country.title()}.")
	
describe_cities(name = 'Brisbin')



def describe_cities(name, country):
	print(f"\n{name.title()} is in {country.title()}")

describe_cities('Durban', 'South Africa')