# Problem 3: Check Voting Eligibility
# Write a Python program that:
# Takes the user's age as input.
# If the age is 18 or above, print:
# Eligible to Vote
# Otherwise, print:
# Not Eligible to Vote


Age = int(input("Enter your Age for Voter eligibility check"))

if  Age >= 18 and Age <= 50:
	print("Eligibility for Vote in the Booth")
elif Age > 50 :
	print("Eligibility for Vote in the mail")
else:
	print("Not eligible for this time")
