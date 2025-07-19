import random 

options = ('Rock','Paper','Scissors')

running = True

while running:
    player = None 
    computer = random.choice(options)        
    while player not in options:
        player = input('Enter your choice (Rock, Paper, Scissors): ')

    print(f'Player: {player} X Computer: {computer}')

    if player == computer:
        print('Its a Tie!')
    elif player == 'Rock'and computer == 'Scissors':
        print('Rock smashes Scissors! Player wins!')
    elif player == 'Paper' and computer == 'Rock':
        print('Paper covers Rock! Player wins!')
    elif player == 'Scissors' and computer == 'Paper':
        print('Scissors cuts Paper! Player wins!')
    elif player == 'Rock' and computer == 'Paper':
        print('Paper covers Rock! Computer wins!')
    elif player == 'Paper' and computer == 'Scissors':
        print('Scissors cuts Paper! Computer wins!')
    elif player == 'Scissors' and computer == 'Rock':
        print('Rock smashes Scissors! Computer wins!')
    else:
        print('Invalid input')

    play_again = input('Play Again ? (yes/no): ')
    if not play_again .lower().startswith('y'):
        running = False
print('Thanks for playing !!!')