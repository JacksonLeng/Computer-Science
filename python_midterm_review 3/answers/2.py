#2.	Create a list of songs you like, such as Twinkle Twinkle 
# Little Star and make a list that stores 
# several examples. Use a for-loop to print a series of 
# statements about these songs, such as 
# “I love to sing Twinkle Twinkle little star in the shower.”

# Creating list of favorite food
favorite_songs = ['Feso Jaiye by The Sahara All Stars of Jos', "Opposite People by Fela"]


# Create for loop
for song in favorite_songs:

	# Create message
	message = f"I love to sing {song} in the shower."

	# Alternative way
	# message = "I love to sing {} in the shower.".format(song)

	# Print message
	print(message)