magicians = ['alice', 'david', 'carolina']
count = 0
for magician in magicians:
    print(magician)
    count = count + 1
    print('\n')
print(count)
for value in range(1, 10):
    print(value)

numbers = list(range(2, 11, 4))

print(numbers)

squares = []
for value1 in range(1, 11):
    square = value1**2
    squares.append(square)
print(squares)
digits = [2, 3, 4, 5, 7, 8, 99, 99.6, 98]
print(min(digits))
print(max(digits))
print(sum(digits))
