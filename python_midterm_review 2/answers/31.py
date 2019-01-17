# 31. Write a program that converts a list of gpas to the appropriate 
# percentage scale. Then convert the following list 
# [1.3, 3.4, 3.9, 3.3, 2.8, 2.2, 3.7] into the appropriate percentage grade. 
# You should output the gpas in the same order.

gpas = [1.3, 3.4, 3.9, 3.3, 2.8, 2.2, 3.7]
new_list = []

for gpa in gpas:
	if gpa < 1.0:
		grade = 'Below 65'
	elif gpa < 1.3:
		grade = "65-66"
	elif gpa < 1.7:
		grade = "67-69"
	elif gpa < 2.0:
		grade = "70-72"
	elif gpa < 2.3:
		grade = "73-76"
	elif gpa < 2.7:
		grade = "77-79"
	elif gpa < 3.0:
		grade = "80-82"
	elif gpa < 3.3:
		grade = "83-86"
	elif gpa < 3.7:
		grade = "87-89"
	elif gpa < 4.0:
		grade = "93-96"
	elif gpa == 4.0:
		grade = "97-100"
	else:
		raise Exception(f"There was a problem with {gpa}")
	new_list.append(grade)


print(new_list)
