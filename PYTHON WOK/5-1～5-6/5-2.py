car = 'Subaru'
Joy = 12
requested_toppings = ['mushrooms', 'onions', 'pineapple']

print("Is car == 'Subaru'? I predict True.")
print(car == 'Subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car == 'sudi'? I predict False.")
print(car == car.lower())

print(Joy > 12)
print(Joy == 12)
print(Joy < 13)
print(Joy >= 13)
print(Joy <= 13)

num = 9
if num >= 0 and num <= 10:    
# 判断值是否在0~10之间
    print ('hello')
# 输出结果: hello
 
num = 10
if num < 0 or num > 10:    
# 判断值是否在小于0或大于10
    print ('hello')


print('\n mushrooms' in requested_toppings )
print('\n A' in requested_toppings )

