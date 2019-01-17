# 7. Use a for-loop to print a second set of messages, 
# one for each university in your list, stating your 
# desire to attend the university. 


# Creating list of Universities
univerities_i_wish_to_attend = ["Harvard", "Stanford", "Princeton", "MIT", "CalTech", "Berkeley"]

# University I cannot attend
university_i_cannot_attend = "Princeton"

# Remove university I cannot attend
univerities_i_wish_to_attend.remove(university_i_cannot_attend)

# Create new university
new_university = "University of Lagos"

# Add new university to my list
univerities_i_wish_to_attend.append(new_university)

# For Loop
for university in univerities_i_wish_to_attend:

	# Create message
	message = f"I wish to attend {university} next semester."

	# Print message
	print(message)