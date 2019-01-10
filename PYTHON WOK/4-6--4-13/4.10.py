numbers=range(1,20,2)
for number in numbers:
	print(number)
#start from 4.6
print("The first three items in the list are:")
for number in numbers[:3]:
	print(number)
print("Three items from the middle of the list are:")
for number in numbers[3:6]:
	print(number)
print("The last three items in the list are:")
for number in numbers[7:]:
	print(number)