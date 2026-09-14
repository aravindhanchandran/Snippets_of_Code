# Write a Python program to count how many numbers between 1 and 20 are divisible by 3

c = 0
n =1

while n <= 20:
	if n%2 == 1:
		c += 1
	n += 1

print('Count of 1 to 20 divisible by 3',c)