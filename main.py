from random import randint

lower_num = int(input("Enter a lower number to start guessing: "))
higher_num = int(input("Enter a top number to start guessing: "))

random_number: int = randint(lower_num, higher_num)

print(f"Guess the number in range from {lower_num} to {higher_num}")

while True:
    try:
        user_guess: int = int(input("Guess: "))
    except ValueError as e:
        print("Please enter a valid number.")
        continue
    if user_guess > random_number:
        print("The number is too high!!!")
    elif user_guess < random_number:
        print("Your number is too small!!!")
    else:
        print("Congratulations! You guessed it.")
        break