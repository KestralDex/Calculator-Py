import random 
lowest_int=1
highest_int=10
answer = random.randint(lowest_int,highest_int)
guesses = 0
is_running = True

print('Python Number Guessing Game')
print(f'Select your number between {lowest_int} and {highest_int}')

while is_running:
    guess = input('Enter your guess : ')

    if guess.isdigit():
        guess = int(guess)
        guesses+= 1
        if guess < lowest_int or guess > highest_int:
            print(f'Number is out of range. Please enter a number between {lowest_int} and {highest_int}')
        elif guess == answer:
            print(f'You have guessed the number in {guesses} guesses')
        elif guess < answer:
            print(f'Too Low!')
        elif guess > answer:
            print(f'Too High!')
    else:
        print (f'Invalid input. Please enter a number between {lowest_int} and {highest_int}')