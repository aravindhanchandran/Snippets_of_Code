# Problem 2: Even or Odd Number
# Write a Python program that:
# Takes an integer as input.
# If the number is even, print: this was Event no. or 
#                        print: this was Odd no.


try:
	N = int(input("Enter number please:"))
	if N%2 == 0:
		print(f"Given no. { N }  was Even")

	else:
		print(f"Given no. { N } was Odd")

except ValueError:
		print("This not an integer")