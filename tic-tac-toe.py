import itertools
from colorama import Fore, Back, Style, init
init()

game_size = int(input("What size game of tic tac toe? "))

def column_range():

    s = " "
    for i in range(len(game)):
        s += "  " + str(i)
    print(s)

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            print(f"Player {l[0]} has won!")
            return True
        else:
            return False

    #bottom_diagonal_win
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        return True

    #top_diagonal_win
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        return True

    #vertical_win
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            return True

    #horizontal_win
    for row in game:
        if all_same(row):
            return True

    return False

def game_board(game_map, choice=0, row=0, column=0, just_display =False): #defaults to 0 so we can use print_board()
    try:
        if game_map[row][column] != 0:
            print("This position is occupied! Choose another!")
            return game_map, False
        column_range()
        if not just_display:
            game_map[row][column] = choice

        for count, row in enumerate(game):
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.RED + ' X ' + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.GREEN + ' O ' + Style.RESET_ALL
            print (count, colored_row)
        return game_map, True

    except IndexError as e:
        print("Error: Make sure you input row/column as 0, 1, 2, etc", e)
        return game_map, False
    except Exception as e:
        print("Something went very wrong!", e)
        return game_map, False


play = True
players = [1, 2]
while play:
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game, just_display =True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        played_turn = False

        while not played_turn:
            '''if current_player == 1:
                player_shape = 'X'
            else:
                player_shape = 'O'       '''
            column_choice = int(input("What column do you want to play? : "))
            row_choice = int(input("What row do you want to play? : ")) 
            game, played_turn = game_board(game, current_player, row_choice, column_choice)
            
        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("Restarting")
            elif again.lower() == "n":
                print("Game Over!")
                play = False
            else:
                print("Not valid answer, Game Over!")
                play = False


