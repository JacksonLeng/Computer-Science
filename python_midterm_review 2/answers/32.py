# 32.	Bubble Sort: Write a program that implements bubble sort 
# on the list [38, 4, 84, 19, 54].

the_list = [38, 4, 84, 19, 54]
n = len(the_list)

for i in range(1, n):
	for j in range(1, (n + 1) - i):
		if the_list[j-1] > the_list[j]:
			the_list[j-1], the_list[j] = the_list[j], the_list[j-1]


print(the_list)
print(sorted(the_list) == the_list)