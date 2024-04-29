import time

user = input('enter your username: ')
file = 'server/userdata/' + user + '.txt'

with open('server/servervalues/g64.txt', 'r') as f:
    g = int(f.read().strip())

with open('server/servervalues/n64.txt', 'r') as f:
    n = int(f.read().strip())

with open('server/servervalues/y.txt', 'r') as f:
    y = int(f.read().strip())

val1 = 'server/userdata/' + user + 'value.txt'
with open(val1, 'r') as f:
    A = int(f.read().strip())

challenge = 'server/userdata/' + user + 'challenge.txt'
with open(challenge, 'r') as f:
    c = int(f.read().strip())

with open(file, 'r') as f:
    b = int(f.read().strip())

starta = time.time()
d = c * b
k2 = d % n

if A == k2:
    print("Correct Password")
    print("Successfully logged into system")
    print("==============================")
    with open('server/sensitive-data/data.txt', 'r') as f:
        data = f.read().strip()
        print(data)
    print("==============================")
else:
    print("Wrong Password!")
    print("Logged out!")

enda = time.time()

print('Time to complete calculations:')
print(enda - starta)
