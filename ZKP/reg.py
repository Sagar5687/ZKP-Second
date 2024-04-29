import time
import hashlib
import os

g = open('server/servervalues/g64.txt','r').read()
g = g.rstrip('\n')
g = int(g, 10)

n = open('server/servervalues/n64.txt','r').read()
n = n.rstrip('\n')
n = int(n, 10)

user = input('enter your username: ')
loc = 'server/userdata/'
file = loc + user + '.txt'

secret = 'client/' + user + 'pass.txt'

reg = input('Register your password with the system: ')
while len(reg) < 8:
    reg = input('Password must be more than 8 characters ')

reg2 = input('Please confirm password: ')
if reg == reg2:
    print("Password set!")
    print("..........................")
    print("..........................")
    print("Password saved to system")
    print("Please run logon script to provide logon details")
    print("..........................")
else:
    print("Passwords don't match!")
    while not reg == reg2:
        reg = input('Register your password with the system: ')
        while len(reg) < 8:
            reg = input('Password must be more than 8 characters ')
        reg2 = input('Please confirm password: ')
        if not reg == reg2:
            print("Passwords don't match!")
        if reg == reg2:
            print("Passwords Match!")
            print("Password set!")
            print("..........................")
            print("..........................")
            print("Password saved to system")
            print("Please run 'logon' script to provide logon details")
            print("..........................")
            break

starta = time.time()
rkey = hashlib.sha256(reg.encode())
rkey_dig = rkey.hexdigest()
x = int(rkey_dig, 16)

A = pow(g, x, n)

secret_dir = os.path.dirname(secret)
if not os.path.exists(secret_dir):
    os.makedirs(secret_dir)

with open(file, "w") as f:
    print(A, file=f)

with open(secret, "w") as xvalue:
    print(x, file=xvalue)

enda = time.time()
print('---------------------')
print('Time to complete calculations:')
print(enda - starta)
