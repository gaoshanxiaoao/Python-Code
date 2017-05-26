players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[2:])
value = -3
print(players[value:])

# or player in players[value:]:
##  player = 'hello'
# print(players)

players1 = players[value:]
for player in players1:
    player = 'hello'
print(players1)
for t in range(0, 3):
    players1[t] = 'hello'
print(players1)
print(players)

print("hello world")
