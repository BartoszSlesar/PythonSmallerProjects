# In this program, you will choose a number between 1 - 1000 and program will try to guess this number (binary search)


low = 1
high = 10000

correct_value = True
try:
    # player is selecting number program should guess
    guess = int(input(f"choose number between {low} and {high} inclusive"))
    if 1 > guess > 10000:
        correct_value = False
except ValueError:
    correct_value = False

# if user did not typed value, typed string or incorrect value in low >= n <=high, it is game over
if not correct_value:
    print("Game Over you typed incorrect value !")


pc_attempts = 0
while correct_value:
    pc_attempts += 1
    pc_guess = low + (high - low) // 2
    if guess < pc_guess:
        high = pc_guess
    elif guess > pc_guess:
        low = pc_guess
    else:
        print(f"I guessed the number it is {pc_guess} attempts needed {pc_attempts}")
        break
