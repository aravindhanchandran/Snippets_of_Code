# Problem 1: Check Positive or Negative

# Write a Python program that:
# Takes an integer as input.
# If the number is greater than 0, print:

try:
	n = int(input("Enter the integer only-"))

	if n < 0 :
		print("It was a Negative number")
	elif n > 0:
		print("It was a Positive number")
	else:
	    print("It was Zero")



except ValueError:
    print("Invalid number")