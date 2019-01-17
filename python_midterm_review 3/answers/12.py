# 12. Use a for-loop to print a new set of 
# invitation messages, one for each university in your list. 

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

# Using insert to add Tsinghua University at beginning
univerities_i_wish_to_attend.insert(0, "Tsinghua University")

# Get middle position
# To get middle position I was use this formula:
# floor( (len(univerities_i_wish_to_attend) + 1) / 2 )

# First do len(univerities_i_wish_to_attend) + 1 / 2
middle = (len(univerities_i_wish_to_attend) + 1) / 2

# To get the floor I will use int() which will cut off the decimal point
middle = int(middle)

# Now I can use insert to add Cambridge to the middle
univerities_i_wish_to_attend.insert(middle, "Cambridge University")

# Use append to add Oxford to the end of my list.
univerities_i_wish_to_attend.append("Oxford")

# Print a set of Invitation Letters
for university in univerities_i_wish_to_attend:

	message = f"Dear {university}, I am writing to request a visit to your campus."
	print(message)