# Question 8 — if / elif / else: Number Comparison
# Write a Python program that takes two numbers as input and prints:
# If the first number is greater → First number is greater
# If the second number is greater → Second number is greater
# If both are equal → Both numbers are equal

n1 = int(input())
n2=  int(input())

if n1 > n2:
	print("First no. greater than second no.")
elif n2 > n1:
	print("Second no. greater than first no.")
else:
	print("Given two no. Equal")
	