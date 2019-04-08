import hashlib

g = open('server/servervalues/g.txt','r').read()
g = g.rstrip('\n')
g = int(g,10)

n = open('server/servervalues/n.txt','r').read()
n = n.rstrip('\n')
n = int(n,10)

user=raw_input ('enter your username: ')
loc = 'server/userdata/'
file = loc+user+'.txt'

secret='client/'+user+'pass.txt'

reg = raw_input('Register your password with the system: ')
while len(reg) < 8 :
        reg=raw_input('Password must be more than 8 characters ')

reg2 = raw_input('Please confirm password: ')
if reg == reg2:
        print ("Password set!")
	print ("..........................")
	print ("..........................")
	print ("Password saved to system")
	print ("Please run logon script to privide logon details")
	print ("..........................")
else:
        print("Passwords dont match!")
	while not reg == reg2:
		reg=raw_input('Register your password with the system: ')
		while len(reg) < 8:
        		reg=raw_input('Password must be more than 8 characters ')
		reg2 = raw_input('Please confirm password: ')
		if not reg == reg2:
			print("Passwords dont match!")
		if reg == reg2:
			print ("Passwords Match!")
			print ("Password set!")
		        print ("..........................")
		        print ("..........................")
		        print ("Password saved to system")
		        print ("Please run 'logon' script to privide logon details")
		        print ("..........................")

			break

rkey = hashlib.sha256(reg)
rkey_dig = rkey.hexdigest()
x = int(rkey_dig,16)

A = pow (g,x,n)

f = open(file, "w")
print >> f,A

xvalue = open(secret, "w")
print >> xvalue,x
