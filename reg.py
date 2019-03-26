import hashlib

g = 2351
n = 5683

reg = raw_input('Register your password with the system: ')
while len(reg) < 8 :
        reg=raw_input('Password must be more than 8 characters ')

reg2 = raw_input('Please confirm password: ')
if reg == reg2:
        print ("Password set!")
	print ("..........................")
	print ("..........................")
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
			print ("..........................")
			break

rkey = hashlib.sha256(reg)
rkey_dig = rkey.hexdigest()
rk = int(rkey_dig,16)

x = pow (g,rk,n)

f = open("passwd.txt", "w")
print >> f,x
