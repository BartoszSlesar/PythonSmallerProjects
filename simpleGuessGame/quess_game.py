import random as rand

# Randomize a number from 1 to 100
secret_number = rand.randint(1, 100)

print("Guess the number game, please type a number from 1 to 100, you have 5 attempts")

# number of attempts player have
attempt = 5

while attempt > 0:
    try:
        print(f"attempts left: {attempt}")
        guess = int(input("Please select a number between 1 and 100:\n"))
        if secret_number > guess:
            print(f"secret_number is greater then {guess}")
        elif secret_number < guess:
            print(f"secret_number is smaller then {guess}")
        else:
            print(f"Congratulations you guessed the number!")
            break
        attempt -= 1
    except ValueError:  # when player typed string instead of int ValueError is catch, and attempt is lowered by one
        print("ups you put text instead of numbers, you loose one attempt")
        attempt -= 1
        continue

if attempt == 0:
    print(f"Game Over the secret_number was {secret_number}")
