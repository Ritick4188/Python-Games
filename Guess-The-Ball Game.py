from random import shuffle

game_on = True

my_list = [' ', 'O', ' ']
print(my_list)

while game_on:

    def shuffle_list(my_list):
        shuffle(my_list)
        return my_list


    shuffle_list(my_list)


    def player_guess():
        guess = "Wrong"
        while guess not in ['0', '1', '2']:
            guess = input("Enter The Guess ['0','1','2'] : ")

        return int(guess)


    x = player_guess()
    print(x)


    def check_guess(my_list, guess):
        if my_list[guess] == 'O':
            print("Correct Guess!")
            print(my_list)
        else:
            print("Wrong Guess!")
            print(my_list)


    check_guess(my_list,x)


    def gameon_choice():

        choice = 'Wrong'
        while choice not in ['Y','N']:
            choice = input("Do You Want To Play Again [Y] or [N] : ")

        if choice == 'Y':
            return True
        else:
            return False


    game_on = gameon_choice()