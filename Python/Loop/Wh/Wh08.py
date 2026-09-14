# Write a Python program using a while loop to reverse a number.


n = int(input())
r = 0

while n != 0:
	r = r*10 + n%10 
	n//=10

print(r)