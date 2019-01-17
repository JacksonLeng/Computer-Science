# 3. Make a list of universities you would like to attend. 
# Then use a for-loop to print a message to each university 
# stating your desire to attend the university. 


# Creating list of Universities
univerities_i_wish_to_attend = ["Harvard", "Stanford", "Princeton", "MIT", "CalTech", "Berkeley"]


# Create for loop
for university in univerities_i_wish_to_attend:

	# Create message
	message = f"I wish to attend {university} next semester."

	# Alternative way
	# message = "I wish to attend {} next semester.".format(university)

	# Print message
	print(message)