# 18. Movies You Want to See: Use reverse() to change the order of your list. 
# Use a for-loop to print to show that its order has changed. 
# Use reverse() to change the order of your list again. 
# Use a for-loop to print the list to show it’s back to its original order.  

movies_i_want_to_see = ['Space Jam', 'Hidden Figures', 'The Pursuit of Happyness', 'Shrek', 'Independence Day']

# reverse list
movies_i_want_to_see.reverse()

# Print each Movie in Reverse Order from Original 
for movie in movies_i_want_to_see:
	print(movie)

# reverse list again to get original order
movies_i_want_to_see.reverse()

# Add some space to seperate the two printed outputs
print("\n")

# Print each movie to show it's back to its original order
for movie in movies_i_want_to_see:
	print(movie)
