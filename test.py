import hashlib

g = 2351
n = 5683
y = 114742425369030229922320788782658049582952322786275543536167364038574317502328
f = open('passwd.txt','r').read()
z = f.rstrip('\n')
x = int(z,10)

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
