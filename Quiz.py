questions = ('The smallest Even number',
             'The largest two digit number',
             'The difference between 10 and 3 is')

options = (('A. 4','B. 2','C. 8','D. 1'),
           ('A. 12','B. 87','C. 98','D. 99'),
           ('A. 4','B. 3','C. 7','D. 9'))

answers = ('B','D','C')

guesses= []

score = 0 

question_num = 0


for question in questions :
    print('------Quiz------')
    print(question)
    for option in options[question_num]:
        print (option)
    guess = input('Enter your answer (A, B, C, D): ').upper()
    guesses.append
    if guess == answers[question_num]:
        print('Correct')
        score += 1
    else:
        print('Incorrect')
    question_num += 1

if question_num == len(questions):
    print('Quiz finished')
    print(f'Your final score is {score} out of {question_num}')
else:
    print('Quiz not finished')