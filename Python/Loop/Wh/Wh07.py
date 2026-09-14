# Write a Python program using a while loop to calculate the sum of all even numbers from 1 to 20.

n = 1
c = 0
while n<21:
	if n%2 == 0:
		c+=n
	n+=1

print(c)

