# 29. Write 6 conditional tests. These conditional tests should:
# •	Test using the lower() function
# •	Compare numbers with inequality, greater than, 
#	less than, greater than or equal to, and less than or equal to


age = 29
name = "Kalu"
# test with lower()
if "KALU".lower().title() == name:
	print(f"Hi {name}!")

# test with >=
if age >= 15:
	print("You can get a driver's permit.")
else:
	print("You cannot get a driver's permit.")


# test with <=
if age <= 3:
	print("You can fly for free.")
else:
	print("You cannot fly for free.")


# test with <
if age < 18:
	print("You cannot vote.")
else:
	print("You can vote.")


# test with >
if age > 24:
	print("You can rent a car.")
else:
	print("You cannot rent a car.")