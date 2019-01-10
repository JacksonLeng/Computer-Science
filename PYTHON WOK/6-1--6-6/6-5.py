rivers = {'yellow river': 'China', 'Euphrates': 'Turkey', 'nile': 'Egypt',

		

	}

	

for river, location in rivers.items():

	print('The ' + river.title() + ' is in ' + location.title())

for river in rivers.keys():

	print(river.title())    

for location in rivers.values():

	print(location.title()) 