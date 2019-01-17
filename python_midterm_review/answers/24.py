# 24. Cubes: A number raised to the second power is called a square. 
# For example, the square of 2 is written as 5**2 in Python. 
# Use a for-loop to make a list of the first 10 squares (that is, the square of each integer from 1 through 10) 
# and print out the value of each square.

powers_of_two = []

for num in range(1,11):
	num_squared = num ** 2
	powers_of_two.append(num_squared)
	print(num_squared)