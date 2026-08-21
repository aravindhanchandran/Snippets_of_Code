# Question 5 — if / elif / else: Grade Checker
# Write a Python program that takes a student's mark as input and prints:
# 90–100 → Grade A
# 75–89 → Grade B
# 60–74 → Grade C
# 40–59 → Grade D
# Below 40 → Fail


m = int(input())


try:
	if 90 <= m <= 100:
		print("Student got Grade A")
	elif 75 <= m <= 89:
		print("Student got Grade B")
	elif 60 <= m <= 74:
		print("Student got Grade C")
	elif 40 <= m <= 59:
		print("Student got Grade D")
	elif m < 40:
		print("Below 40 and try again")
except ValueError:
	print("Invalid value , please enter as integer")
