import random as rand

# Randomize a number from 1 to 100
lowest_Number = 1
highest_number = 100
secret_number = rand.randint(lowest_Number, highest_number)
attempt = 5

print(f"Guess the number , please type a number from {lowest_Number} to {highest_number}, you have {attempt} attempts")

# number of attempts player have


while attempt:
    try:
        print(f"attempts left: {attempt}")
        guess = int(input(f"Please select a number between {lowest_Number} and {highest_number}:\n"))
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
