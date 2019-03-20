import hashlib

g = 2351
n = 5683
y = 114742425369030229922320788782658049582952322786275543536167364038574317502328

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

password = raw_input('Please enter your password: ')

key = hashlib.sha256(password)
hex_dig = key.hexdigest()
a = int(hex_dig,16)

v = pow (g,y,n)
m1=pow (x,y,n)
m2=pow (v,a,n)

if m1 == m2:
	print ("Correct Password")
else:
	while not m1 == m2:
		print("Wrong Password!")
		password = raw_input('Please enter correct password: ')
		key = hashlib.sha256(password)
		hex_dig = key.hexdigest()
		a = int(hex_dig,16)

		v = pow (g,y,n)
		m1=pow (x,y,n)
		m2=pow (v,a,n)
		if m1==m2:
			print ("Correct Password!")
			break
