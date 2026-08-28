# Question 9 — if / elif / else: Largest of Three Numbers
# Write a Python program that takes three integers as input and prints the largest number.
# Requirements
# If n1 is the largest → print First number is largest
# If n2 is the largest → print Second number is largest
# If n3 is the largest → print Third number is largest
# # If all three are equal → print All numbers are equal

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 > n2 and n1 > n3:
	print("First number greater than all")
elif n2 > n3 and n2 > n1:
	print("Second number greater than all")
elif n3 > n2 and n3 > n1:
	print("Third number greater than all")
else:
	print("Given two integer two are equal")
