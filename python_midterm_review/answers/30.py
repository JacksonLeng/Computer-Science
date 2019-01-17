# 30.	Write 4 more conditional tests. These conditional tests should:
# •	Test using the and keyword and the or keyword
# •	Test whether an item is in a list
# •	Test whether an item is not in a list


age = 29
name = "Kalu"
friends = ['Eke', 'Dike', 'Hali', 'Sara']

# test with lower()
if "EKE".lower().title() in friends:
	print("Hi Eke!")
else:
	print("I don't know Eke.")

if name == "Kalu" or "Dike":
	print("Hi Kalu brothers")

if "Hali" and "Sara" in friends:
	print("Hi Hali and Sara")

if "Agbai" not in friends:
	print("Sorry, I do not know Agbai.")
