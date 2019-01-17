# 4. Use len() to print a message indicating the number of 
# universities you wish to attend. 
# You should say “I want to apply to 6 universities.”, 
# replacing 6 with the output from len(). 


# Creating list of Universities
univerities_i_wish_to_attend = ["Harvard", "Stanford", "Princeton", "MIT", "CalTech", "Berkeley"]

# Get number of univerities
number_of_univerities = len(univerities_i_wish_to_attend)


# Create message
message = f"I wish to apply to {number_of_univerities} univerities."

# Alternative way
# message = "I wish to apply to {} universities.".format(number_of_univerities)

# Print message
print(message)