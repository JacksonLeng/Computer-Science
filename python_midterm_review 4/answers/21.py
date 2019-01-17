# 21. Make a list of the numbers from one to five million, 
# and then use min() and max() to make sure your list actually
# starts at one and ends at five million.
# Also, use the sum()function to see how quickly Python can add 5 million #s.

numbers = range(1, (5000 * 1000) + 1)

# Print min
smallest = min(numbers)
largest = max(numbers)
the_sum = sum(numbers)

message1 = f"The smallest is {smallest}.\nThe biggest is {largest}."
message2 = f"The sum of all numbers is {the_sum}"
print(message1)
print(message2)
