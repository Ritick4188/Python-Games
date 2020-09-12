from random import choice

choice_list = ['Rock', 'Paper', 'Scissor']

while True:

    print('ROCK-PAPER-SCISSOR GAME ')
    you_win = 0
    computer_win = 0

    for i in range(1, 4):
        print('Round', i, 'Start')
        print('Please Select Any One Option : ')
        print(' 1. Rock\n 2. Paper\n 3. Scissor')

        your_choice = int(input('Enter Your Choice : '))

        if your_choice == 1:
            print('You Select Rock')
            your_choice = 'Rock'
        elif your_choice == 2:
            print('You Select Paper')
            your_choice = 'Paper'
        elif your_choice == 3:
            print("You Select Scissor")
            your_choice = 'Scissor'
        else:
            print('Invalid Choice!')
            break

        computer_choice = choice(choice_list)
        print("Computer Select :", computer_choice)

        if your_choice == computer_choice:
            print('This Round Draw')
            you_win += 1
            computer_win += 1

        elif (your_choice == 'Rock' and computer_choice == 'Scissor') or (
                your_choice == 'Paper' and computer_choice == 'Rock') or (
                your_choice == 'Scissor' and computer_choice == 'Paper'):
            print('You Win This Round')
            you_win += 1

        else:
            print("Computer Win This Round")
            computer_win += 1

    if you_win > computer_win:
        print('Score : You Score = {} and Computer Score = {}'.format(you_win, computer_win))
        print("You Win This Game")

    elif computer_win > you_win:
        print('Score : You Score = {} and Computer Score = {}'.format(you_win, computer_win))
        print("You Lose This Game")

    else:
        print('Score : You Score = {} and Computer Score = {}'.format(you_win, computer_win))
        print("Game Draw")

    user_choice = input("Do You Want To Play Again ['Y' or 'N'] : ")

    if user_choice.lower()[0] == 'y':
        continue
    else:
        break
