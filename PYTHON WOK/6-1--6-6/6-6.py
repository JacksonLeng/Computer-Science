languages = {'Andy': 'python', 'Sylvia': 'go', 'Jackson': 'ruby', 'Nicole': 'c',}

	

members = ['Andy', 'Sylvia', 'Jackson', 'Nicole','Peter', 'Google']

	

for member in members:

	if member in languages.keys():

		print('Thanks for responding, ' + member.title())

	else:

		print('Please take your poll, ' + member.title()) 