import random

print("Welcome to the Guessing Game!")
print("I'm thinking of a of a number between 1 and 20.")

secret_number  = random.randint(1,20)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Take a guess: "))
    if guess < secret_number: 
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You've guessed the number ({secret_number}) correctly!")
        break
    attempts +=1
    remaining_attempts = max_attempts - attempts
    print(f"You have {remaining_attempts} attempts left.")
else:
    print(f"Sorry, you've run out of attempts. The number was {secret_number}.")