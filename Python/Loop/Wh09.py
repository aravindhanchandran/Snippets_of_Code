# Write a Python program using a while loop to find the largest digit in a number.

n = int(input())
r = 0
l = []

while n != 0:
	r = n % 10 
	n//=10
	# l = r
	l.append(r)

# str(l)
print(max(l))

# print(n)
# print(r)
