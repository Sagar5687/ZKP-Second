user=raw_input ('enter your username: ')
file='server/userdata/'+user+'.txt'

g = open('server/servervalues/g.txt','r').read()
g = g.rstrip('\n')
g = int(g,10)

n = open('server/servervalues/n.txt','r').read()
n = n.rstrip('\n')
n = int(n,10)

y = open('server/servervalues/y.txt','r').read()
y = y.rstrip('\n')
y = int(y,10)

val1='server/userdata/'+user+'value.txt'
f = open(val1,'r').read()
z = f.rstrip('\n')
A = int(z,10)

challenge='server/userdata/'+user+'challenge.txt'
c = open(challenge,'r').read()
c = c.rstrip('\n')
c = int(c,10)

b = open(file,'r').read()
b = b.rstrip('\n')
b = int(b,10)

d = c*b

k2= d % n

if A == k2:
	print ("Correct Password")
	print ("Sucessfully logged into system")
	print ("==============================")
	data = open('server/sensitive-data/data.txt','r').read()
	data = data.rstrip('\n')
	print data
	print ("==============================")
else:
       while not A == k2:
       		print("Wrong Password!")
		print("Logged out!")
                break
