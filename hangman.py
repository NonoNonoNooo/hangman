'''hangman'''
def hangman(word):
    wrong = 0
    stages = ["",
              "_________",
              "|       |       ",
              "|       O       ",
              "|     / | \\    ",
              "|      / \\     "]
    rletters = list(word)
    board = ['__'] * len(word)
    win = False
    print('Welcome back to life!')


    while wrong < len(stages) - 1:
        print('\n')
        char = input('Enter a letter: ')
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((' '.join(board)))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '__' not in board:
            print('You won! It was a word: ')
            print(''.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages))
        print(f'You lost! The word was chosen: {word}.')



hangman('Chargoggagoggmanchauggagoggchaubunagungamaugg')
