import random

def guess_number():
    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        guess = int(input("Guess the secret number (1-10): "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations, you guessed the secret number in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Too low, try again.")
        else:
            print("Too high, try again.")

guess_number()
