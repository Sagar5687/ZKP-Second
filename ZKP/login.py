import hashlib

g = open('server/servervalues/g.txt','r').read()
g = g.rstrip('\n')
g = int(g,10)

n = open('server/servervalues/n.txt','r').read()
n = n.rstrip('\n')
n = int(n,10)

y = open('server/servervalues/y.txt','r').read()
y = y.rstrip('\n')
y = int(y,10)

user=raw_input ('enter your username: ')
loc = 'server/userdata/'
file = loc+user+'.txt'

A = open(file,'r').read()
A = A.rstrip('\n')
A = int(A,10)

secret='client/'+user+'pass.txt'

x = open(secret,'r').read()
x = x.rstrip('\n')
x = int(x,10)

q = (x+y)%(n-1)
val1=pow (g,q,n)

c= pow (g,y,n)

e = open("server/val1.txt", "w")
print >> e,val1

f = open("server/challenge.txt", "w")
print >> f,c

print "logon information provided. Please run 'authoise' script to authenticate"
