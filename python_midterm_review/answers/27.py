# 27. Start with your program from the first question. 
# Make a copy of the list of food and call it friend_food.
# Then do the following:
# 	•	Add a new food item to the original list
# 	•	Add a different food to the list friend_food.
# 	•	Prove that you have two separate lists. 
#		i.	Print the message, “My favorite types of food are:" 
#			and use a for-loop to print the first list. 
#		ii.	Print the message, my friend’s favorite types of food are:
#			and then use a for loop to print the second list. 
#		iii. Make sure each new food item is stored in the appropriate list. 


favorite_food = ['Egusi Soup', 'Pepper Soup', 'Jollof Rice']

# Make copy of favorite food
friend_food = favorite_food[:]

# Add a new food item to the original list
favorite_food.append("Vegetable Soup")



# Add a different food to the list friend_food.
friend_food.append("Pizza")


# Print the message, “My favorite types of food are:" 
# “ and use a for-loop to print the first list. 
print("My favorite types of food are:")
for food_item in favorite_food:
	print(f"\t{food_item}")


# Print the message, my friend’s favorite types of food are:
# and then use a for loop to print the second list.

print("My friend's favorite types of food are:")
for food_item in friend_food:
	print(f"\t{food_item}")

# Make Sure Vegetable Soup in favorite_food, but not in friend_food
print("Vegetable Soup" in favorite_food)
print("Vegetable Soup" not in friend_food)


# Make Sure Vegetable Soup in favorite_food, but not in friend_food
print("Pizza" in friend_food)
print("pizza" not in favorite_food)