pizzas=['tao yuan pizza','Cyn pizza','beef pizza']
friend_pizzas=pizzas[:]
pizzas.append('wu han pizza')
friend_pizzas.append('tomato pizza')
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("My friend’s favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)