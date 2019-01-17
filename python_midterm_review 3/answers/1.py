# 1. Create a list containing the names of some of your 
# favorite food. Use bracket-notation and position numbers to 
# print each food’s name as well as a message about the food 
# item, one at a time (do not use a for-loop). 
# The text of the message should be the same, with only 
# the name of the food being different. 

# Creating list of favorite food
favorite_food = ['Egusi Soup', 'Pepper Soup', 'Jollof Rice']


# Create message that I will print with each food name
message = "I love my mom's"

# Printing each food's name along with message
print(message + " " + favorite_food[0] + ".")
print(message + " " + favorite_food[1] + ".")
print(message + " " + favorite_food[2] + ".")


# Alternative Method #1
# Only Works w/ Python 3.6 and up
# This is the preferred Method.
# print(f"{message} {favorite_food[0]}.")
# print(f"{message} {favorite_food[1]}.")
# print(f"{message} {favorite_food[2]}.")





# Alterative Way #2
# Works with Python 2 and up
# print("{} {}.".format(message, favorite_food[0]))
# print("{} {}.".format(message, favorite_food[1]))
# print("{} {}.".format(message, favorite_food[2]))


# Alterative Way #3
# Works with Python 2 and up
# # Old School Way
# print("%s %s" % (message, favorite_food[0]))
# print("%s %s" % (message, favorite_food[1]))
# print("%s %s" % (message, favorite_food[2]))


# To Read More Info On the Different Ways
# of Formatting Strings check this website out
# https://realpython.com/python-f-strings/


