# Raymund Zyron Abella, BSIT 2-B
import random
# first loop that keeps prompt the user to play again unless otherwise
while True:
    correctAnswer = random.randint(1, 100)
    attempts = 1
    # second while loop that keeps asking the user to guess
    while True:
        try:
            guess = int(input('Guess a number: ').strip())
            # breaks out of the loop when user has exceeded the number of attempts
            if attempts > 5:
                print('Sorry, you\'ve run out of guesses! ')
                print(f'The number was {correctAnswer}')
                break
            if guess == correctAnswer:
                print(f'Congratulations! You guessed the number in {attempts} attempts!')
                break
            elif guess > correctAnswer:
                print('Too high. Try again. ')
                attempts += 1
            else:
                print('Too low. Try again. ')
                attempts += 1
        except:
            print('Invalid input! ')
            attempts += 1
    choice = input('Do you want to play again? yes/no').upper()
    if choice == 'NO':
        break