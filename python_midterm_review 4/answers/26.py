# 26.	Create a list of the last 5 stores you shopped at. 
# 	•	Print the message, “The first three items in the list are: ”. 
# 		Then use a slice and a for-loop to print the first 
#		three items from the list.
# 	•	Print the message, “Three items from the middle of the list are: .
#		Then use a slice and a for-loop to print three items from the 
#		middle of the list.
# 	•	Print the message, “The last three items from the end of the list are: ”
# 		Then use a slice and a for-loop to print the last 3 items in the list. 

stores = ['711', 'Walgreens', 'Apple Store', 'Fashion Outlet', 'Cool Kids Store']


# Print first three items
print("Here are the first three items:")
for item in stores[0:3]:
	print(f"\t{item}")


# Print middle three items
print("Here are the middle three items:")
for item in stores[1:4]:
	print(f"\t{item}")

# Print last three items
print("Here are the last three items:")
for item in stores[2:5]:
	print(f"\t{item}")