# Problem 4: Largest of Two Numbers
# Write a Python program that:
# Takes two integers as input.
# Print s which number is larger.
# If both numbers are equal, print Both are Equal.

N1 = int(input())
N2= int(input())

if N1 > N2:
	print(f"Number {N1} was greater than {N2}")
elif N2 > N1:
	print(f"Number {N2} was greater than {N1}")
else:
	print(f"Number {N1} was equal to Number {N2}")

