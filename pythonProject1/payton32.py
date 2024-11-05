import random
# prompt messages, for the correct and wrong answers
correctPrompt = ['Very Good!',
                 'Excellent!',
                 'Nice Work!',
                 'Keep up the good work!']

wrongPrompt = ['No. Please try again.',
               'Wrong. Try once more.',
               "Don't give up!",
               'No, Keep trying.']
# start of loop
while True:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    correctAnswer = num1 * num2
    answer = 0

    while True:
        try:
            # keeps looping until the right answer
            answer = int(input(f"How much is {num1} times {num2}?\n").strip())
            if answer == correctAnswer:
                randPrompt = random.randint(0, 3)
                prompt = correctPrompt[randPrompt]
                print(prompt)
                break
            else:
                randPrompt = random.randint(0, 3)
                prompt = wrongPrompt[randPrompt]
                print(prompt)
        except ValueError:
            print('Invalid input. Try again')
    # asks the user to continue or not
    status = input('do you want to continue?(y/n)\n').upper()
    if status == 'N':
        break
