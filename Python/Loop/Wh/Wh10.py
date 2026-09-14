# Using a while loop, count how many digits in a number are even.

n = int(input())
r = 0
l =[]
c = 0

while n != 0:
	r=n%10 
	n//=10
	l.append(r)

for i in l:
   if i%2 == 0:
	   c+=1

print(c)
