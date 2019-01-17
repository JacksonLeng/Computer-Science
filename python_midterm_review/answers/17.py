# 17. Movies You Want to See: 
# Use a for-loop and sorted() to print your list in 
# reverse alphabetical order without changing the order of the original list. 
# Show that your list is still in its original order by printing it again.

movies_i_want_to_see = ['Space Jam', 'Hidden Figures', 'The Pursuit of Happyness', 'Shrek', 'Independence Day']

# Print each Movie in Alphabetical Order With A For-Loop
for movie in sorted(movies_i_want_to_see, reverse=True):
	print(movie)


# Show list is still in its original order
print(movies_i_want_to_see)