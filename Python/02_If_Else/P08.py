# Question 7 — if / elif / else: Positive, Negative, or Zero
# Write a Python program that takes a number as input and prints:
# Greater than 0 → Positive
# Less than 0 → Negative
# Exactly 0 → Zero

n = int(input())

if n > 0:
	print("Given no. was Positive")
elif n < 0:
	print("Negative Integer")
else:
	print("Exactly ZERO")
