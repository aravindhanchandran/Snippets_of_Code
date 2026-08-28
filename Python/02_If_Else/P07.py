# Question 6 — if / elif / else: Temperature Checker 🌡️
# Write a Python program that takes the temperature as input and prints:
# Above 30 → Hot
# 20 to 30 → Warm
# 10 to 19 → Cool
# Below 10 → Cold


T = int(input())

if T >= 30:
	print("Hot Weather like Sahara desert")
elif T >=20 :
	print("Warm Weather")
elif T >= 10:
	print("Cool Weather")
else:
	print("Cold Weather  like Antartica")

