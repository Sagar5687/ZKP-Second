import time

g = open('server/servervalues/g64.txt','r').read()
g = g.rstrip('\n')
g = int(g, 10)

n = open('server/servervalues/n64.txt','r').read()
n = n.rstrip('\n')
n = int(n, 10)

y = open('server/servervalues/y.txt','r').read()
y = y.rstrip('\n')
y = int(y, 10)

user = input('enter your username: ')
loc = 'server/userdata/'
file = loc + user + '.txt'

A = open(file, 'r').read()
A = A.rstrip('\n')
A = int(A, 10)

secret = 'client/' + user + 'pass.txt'

x = open(secret, 'r').read()
x = x.rstrip('\n')
x = int(x, 10)

starta = time.time()
q = (x + y) % (n - 1)
val1 = pow(g, q, n)

c = pow(g, y, n)

val = 'server/userdata/' + user + 'value.txt'
with open(val, "w") as e:
    print(val1, file=e)

challenge = 'server/userdata/' + user + 'challenge.txt'
with open(challenge, "w") as f:
    print(c, file=f)

enda = time.time()

print("Logon information provided. Please run 'authorise' script to authenticate")
print('Time to complete calculations:')
print(enda - starta)
