import random

# The computer randomly selects a number between 0 and 100
secret_number = random.randint(0, 100)

# Set the maximum number of attempts
max_attempts = 10

print(f"Guess a number between 0 and 100. and try to find it in less than {max_attempts} steps.")

for attempt in range(1, max_attempts + 1):
    # The computer makes a guess
    guess = int(input("Enter a guess : "))

    # Check the guess
    if guess < secret_number:
        print("It's higher!")
        low = guess + 1
    elif guess > secret_number:
        print("It's lower!")
        high = guess - 1
    else:
        print(f"Win !! \n The secret number {secret_number} in {attempt} attempts.")
        break
else:
    print(f"Lose !! Couldn't find the number in {max_attempts} attempts.\nThe secret number was {secret_number}.")
