# 13. You have just been accepted to early admission by UCLA. 
# Unfortunately, their early admission rules limit you 
# to applying to only 2 other universities. 
# Add a new line that prints a message saying that 
# you can only apply to two universities. 
# Then use pop() to remove universities from your list 
# one at a time until only two universities remain in your list . 
# Each time you pop a university from your list, print a 
# message to that university letting them know you’re 
# sorry you can no longer attend.

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

# Print message saying I can only attend 2 univeristies
print("Sorry. I can only apply to two univeristies.")


# Move the two universities I want to position 0 and 1
univerities_i_wish_to_attend.remove("Harvard")
univerities_i_wish_to_attend.remove("University of Lagos")
univerities_i_wish_to_attend.insert(0, "Harvard")
univerities_i_wish_to_attend.insert(1, "University of Lagos")

# Get number of univerities
total_universities = len(univerities_i_wish_to_attend)

# Use for loop to remove all but last two universities
for i in range(total_universities - 2):
	popped = univerities_i_wish_to_attend.pop()
	print(f"Sorry, I cannot attend {popped}.")
		