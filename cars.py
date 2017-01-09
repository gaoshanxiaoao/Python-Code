cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


age = 12
if age < 4:
    print("your admission cost is $0.")
elif age < 18:
    print("your admission cost is $5")
else:
    print("your admission cost is $10")

requested_toppings = ['mushroom', 'extra cheese']
if 'mushroom' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("\nFinished making your pizza!")


requested_toppings = []

if requested_toppings:
    print("hull")
