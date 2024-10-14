# Number guessing game
import random

print("Hello Gamer, Welcome to the Number Guessing Game...")

# declare variables
num_to_guess = random.randrange(100)
num_chances = 11
counter = 0

while counter < num_chances:
	counter = counter + 1
	my_num = int(input("Enter your number: "))

	if my_num == num_to_guess:
		print(f'The number is {num_to_guess} and you got it in the {counter} attempt')
		break

	elif counter >= num_chances and my_num != num_to_guess:
		print(f'Sorry, the number is {num_to_guess} try again and Good luck')

	elif my_num > num_to_guess:
		print("Your guess is higher")
	elif my_num < num_to_guess:
		print("Your guess is lesser")