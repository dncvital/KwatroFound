import random
import os

def clear():
    os.system('clear')


def random_cell():
    random_row = random.randint(1, 10)
    random_col = random.randint(1, 10)
    loc = random_col + 10*(random_row-1)
    return loc


# function to create the board for the AI
def create_board_computer():
    board = {
        1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' ', 10:' ',
        11:' ', 12:' ', 13:' ', 14:' ', 15:' ', 16:' ', 17:' ', 18:' ', 19:' ', 20:' ',
        21:' ', 22:' ', 23:' ', 24:' ', 25:' ', 26:' ', 27:' ', 28:' ', 29:' ', 30:' ',
        31:' ', 32:' ', 33:' ', 34:' ', 35:' ', 36:' ', 37:' ', 38:' ', 39:' ', 40:' ',
        41:' ', 42:' ', 43:' ', 44:' ', 45:' ', 46:' ', 47:' ', 48:' ', 49:' ', 50:' ',
        51:' ', 52:' ', 53:' ', 54:' ', 55:' ', 56:' ', 57:' ', 58:' ', 59:' ', 60:' ',
        61:' ', 62:' ', 63:' ', 64:' ', 65:' ', 66:' ', 67:' ', 68:' ', 69:' ', 70:' ',
        71:' ', 72:' ', 73:' ', 74:' ', 75:' ', 76:' ', 77:' ', 78:' ', 79:' ', 80:' ',
        81:' ', 82:' ', 83:' ', 84:' ', 85:' ', 86:' ', 87:' ', 88:' ', 89:' ', 90:' ',
        91:' ', 92:' ', 93:' ', 94:' ', 95:' ', 96:' ', 97:' ', 98:' ', 99:' ', 100:' ',
        }

    ship_locs = []
    ship_sizes = [5, 4, 3, 3, 2]

    for size in ship_sizes:
        placed_tile = 0
        loc = random_cell()
        temp_loc = loc
        valid_tiles = 0
        while valid_tiles < size:
            if temp_loc not in board.keys():
                loc = random_cell()
                temp_loc = loc
                continue
            if temp_loc in ship_locs:
                loc = random_cell()
                temp_loc = loc
                continue
            if (temp_loc % 10 == 0) and ((valid_tiles+1) < size):
                loc = random_cell()
                temp_loc = loc
                continue
            temp_loc+=1
            valid_tiles += 1

            # will add the tiles that the ship will occupy in ship_locs
            # if all tiles were valid   
            if(valid_tiles == size):
                # while loop for placing the tiles to the slots
                while placed_tile < size:                    
                    ship_locs.append(loc)
                    placed_tile += 1
                    loc += 1

    for loc in ship_locs:
        board[loc] = 'O'
    
    return board


# function to create the board for the player
def create_board_player():
    number_of_ships = 5
    placed_destroyer = False
    placed_submarine = False
    placed_cruiser = False
    placed_battleship = False
    placed_aircraft = False
    board = {
            1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' ', 10:' ',
            11:' ', 12:' ', 13:' ', 14:' ', 15:' ', 16:' ', 17:' ', 18:' ', 19:' ', 20:' ',
            21:' ', 22:' ', 23:' ', 24:' ', 25:' ', 26:' ', 27:' ', 28:' ', 29:' ', 30:' ',
            31:' ', 32:' ', 33:' ', 34:' ', 35:' ', 36:' ', 37:' ', 38:' ', 39:' ', 40:' ',
            41:' ', 42:' ', 43:' ', 44:' ', 45:' ', 46:' ', 47:' ', 48:' ', 49:' ', 50:' ',
            51:' ', 52:' ', 53:' ', 54:' ', 55:' ', 56:' ', 57:' ', 58:' ', 59:' ', 60:' ',
            61:' ', 62:' ', 63:' ', 64:' ', 65:' ', 66:' ', 67:' ', 68:' ', 69:' ', 70:' ',
            71:' ', 72:' ', 73:' ', 74:' ', 75:' ', 76:' ', 77:' ', 78:' ', 79:' ', 80:' ',
            81:' ', 82:' ', 83:' ', 84:' ', 85:' ', 86:' ', 87:' ', 88:' ', 89:' ', 90:' ',
            91:' ', 92:' ', 93:' ', 94:' ', 95:' ', 96:' ', 97:' ', 98:' ', 99:' ', 100:' ',
            }
    while (number_of_ships != 0):
        valid_placement = False
        ship_locs = []
        display_board(board)  
        print('Hey Player! Choose a ship:')
        print('[1] Destroyer (2 tiles)')
        print('[2] Submarine (3 tiles)')
        print('[3] Cruiser (3 tiles)')
        print('[4] Battleship (4 tiles)')
        print('[5] Aircraft (5 tiles)')
        print("Your Choice: ", end="")
        choice_ship = int(input())
        print()
        print('Choose direction:')
        print('[1] Vertical')
        print('[2] Horizontal')
        print("Your Choice: ", end="")
        choice_dir = int(input())
        print()
        if (choice_ship == 1):
            if (placed_destroyer == False):
                board = place_ship("Destroyer", 2, choice_dir, ship_locs, board)            
                valid_placement = True
                placed_destroyer = True
        elif (choice_ship == 2):
            if (placed_submarine == False):
                board = place_ship("Submarine", 3, choice_dir, ship_locs, board)
                valid_placement = True
                placed_submarine = True
        elif (choice_ship == 3):
            if (placed_cruiser == False):
                board = place_ship("Cruiser", 3, choice_dir, ship_locs, board)
                valid_placement = True
                placed_cruiser = True
        elif (choice_ship == 4):
            if (placed_battleship == False):
                board = place_ship("Battleship", 4, choice_dir, ship_locs, board)
                valid_placement = True
                placed_battleship = True
        elif (choice_ship == 5):
            if (placed_aircraft == False):
                board = place_ship("Aircraft", 5, choice_dir, ship_locs, board)
                valid_placement = True
                placed_aircraft = True
        if (valid_placement == True):
            number_of_ships -= 1
        else:
            print("You can only place each ship ONCE! Try again.")
            print()
    return board


def choose_direction():
    print('Choose direction:')
    print('[1] Vertical')
    print('[2] Horizontal')
    print("Your Choice: ", end="")
    choice_dir = int(input())
    print()
    return choice_dir


## function to display board in a readeable format
def display_board(board):
    print('       1   2   3   4   5   6   7   8   9   10  ')
    print('     ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗')
    print('   1 ║ ' + board[1] + ' ║ ' + board[2] + ' ║ ' + board[3] + ' ║ ' + board[4] + ' ║ ' + board[5] + ' ║ ' + board[6] + ' ║ ' + board[7] + ' ║ ' + board[8] + ' ║ ' + board[9] + ' ║ ' + board[10] + ' ║')
    print('     ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
    print('   2 ║ ' + board[11] + ' ║ ' + board[12] + ' ║ ' + board[13] + ' ║ ' + board[14] + ' ║ ' + board[15] + ' ║ ' + board[16] + ' ║ ' + board[17] + ' ║ ' + board[18] + ' ║ ' + board[19] + ' ║ ' + board[20] + ' ║')
    print('     ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
    print('   3 ║ ' + board[21] + ' ║ ' + board[22] + ' ║ ' + board[23] + ' ║ ' + board[24] + ' ║ ' + board[25] + ' ║ ' + board[26] + ' ║ ' + board[27] + ' ║ ' + board[28] + ' ║ ' + board[29] + ' ║ ' + board[30] + ' ║')
    print('     ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
    print('   4 ║ ' + board[31] + ' ║ ' + board[32] + ' ║ ' + board[33] + ' ║ ' + board[34] + ' ║ ' + board[35] + ' ║ ' + board[36] + ' ║ ' + board[37] + ' ║ ' + board[38] + ' ║ ' + board[39] + ' ║ ' + board[40] + ' ║')
    print('     ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
    print('   5 ║ ' + board[41] + ' ║ ' + board[42] + ' ║ ' + board[43] + ' ║ ' + board[44] + ' ║ ' + board[45] + ' ║ ' + board[46] + ' ║ ' + board[47] + ' ║ ' + board[48] + ' ║ ' + board[49] + ' ║ ' + board[50] + ' ║')
    print('     ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
    print('   6 ║ ' + board[51] + ' ║ ' + board[52] + ' ║ ' + board[53] + ' ║ ' + board[54] + ' ║ ' + board[55] + ' ║ ' + board[56] + ' ║ ' + board[57] + ' ║ ' + board[58] + ' ║ ' + board[59] + ' ║ ' + board[60] + ' ║')
    print('     ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
    print('   7 ║ ' + board[61] + ' ║ ' + board[62] + ' ║ ' + board[63] + ' ║ ' + board[64] + ' ║ ' + board[65] + ' ║ ' + board[66] + ' ║ ' + board[67] + ' ║ ' + board[68] + ' ║ ' + board[69] + ' ║ ' + board[70] + ' ║')
    print('     ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
    print('   8 ║ ' + board[71] + ' ║ ' + board[72] + ' ║ ' + board[73] + ' ║ ' + board[74] + ' ║ ' + board[75] + ' ║ ' + board[76] + ' ║ ' + board[77] + ' ║ ' + board[78] + ' ║ ' + board[79] + ' ║ ' + board[80] + ' ║')
    print('     ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
    print('   9 ║ ' + board[81] + ' ║ ' + board[82] + ' ║ ' + board[83] + ' ║ ' + board[84] + ' ║ ' + board[85] + ' ║ ' + board[86] + ' ║ ' + board[87] + ' ║ ' + board[88] + ' ║ ' + board[89] + ' ║ ' + board[90] + ' ║')
    print('     ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
    print('  10 ║ ' + board[91] + ' ║ ' + board[92] + ' ║ ' + board[93] + ' ║ ' + board[94] + ' ║ ' + board[95] + ' ║ ' + board[96] + ' ║ ' + board[97] + ' ║ ' + board[98] + ' ║ ' + board[99] + ' ║ ' + board[100] + ' ║')
    print('     ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝')


def check_for_game_over(pc_point, player_point, round):
    """If all ships have been sunk or we run out of bullets its game over"""
    if round == 50:
        if pc_point == player_point:
            print("No more turns and it is a tie.")
        elif pc_point > player_point:
            print('No more turns and you LOST.')   
        elif player_point > pc_point:
            print('No more turns and you WON. Congrats!') 
        return False
    elif pc_point == 0:
        print("You WON. Congrats!")
        return False
    elif player_point == 0:
        print("You LOST.")  
        return False
    return True


def place_ship(ship_type, ship_size, choice_dir, ship_locs, board):
    valid_placement = False
    loc = 0
    ship_tiles = []
    while (valid_placement == False):
        placed_tile = 0
        print("Enter row: ", end="")
        row = int(input())
        print("Enter column: ", end="")
        col = int(input())
        print()
        loc = col + 10*(row-1)
        temp_loc = loc

        if choice_dir == 1:
            valid_tiles = 1
            # while loop for checking the slots to be occupied
            while valid_tiles < ship_size:
                if temp_loc not in board.keys():
                    print('That\'s out of range! Try again.')
                    print()
                    break
                if temp_loc in ship_locs:
                    print('The slot is occupied! Try again.')
                    print()
                    break
                temp_loc+=10
                valid_tiles += 1
            
            # will add the tiles that the ship will occupy in ship_locs
            # if all tiles were valid
            if(valid_tiles == ship_size):
                # while loop for placing the tiles to the slots
                while placed_tile < ship_size:
                    ship_locs.append(loc)
                    placed_tile += 1
                    loc += 10
                valid_placement = True
            

        elif choice_dir == 2:
            valid_tiles = 0
            #print("horizontal\n")
            # while loop for checking the slots to be occupied
            while valid_tiles < ship_size:
                if temp_loc not in board.keys():
                    print('That\'s out of range! Try again.')
                    print()
                    break
                if temp_loc in ship_locs:
                    print('The slot is occupied! Try again.')
                    print()
                    break
                if (temp_loc % 10 == 0) and ((valid_tiles+1) < ship_size):
                    print('That\'s out of range!')
                    print()
                    break
                temp_loc+=1
                valid_tiles += 1

            # will add the tiles that the ship will occupy in ship_locs
            # if all tiles were valid   
            if(valid_tiles == ship_size):
                # while loop for placing the tiles to the slots
                while placed_tile < ship_size:                    
                    ship_locs.append(loc)
                    placed_tile += 1
                    loc += 1
                valid_placement = True
    
    for loc in ship_locs:
        board[loc] = 'O'
    return board
    

## function to play Battleship
def game():
    ## create boards for NPC and player
    pc_board = create_board_computer()
    player_board = create_board_player()
    cont_game = True
    print("Displaying player board...")
    ## display player's board
    display_board(player_board)
    
    ## variables to control when the game ends
    turn = 'Player'
    pc_point = 6
    player_point = 6
    round = 0

    pc_moves = []
    player_moves = []
    
    ## lists to keep track of player and NPC's moves
    pc_movescheck_for_game_overer_moves = []
    
    while (cont_game == True):
        if turn == 'Player':
            score = False
            print(' ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
            print('\033[1m Player turn:\033[0m')
            print("Enter row: ", end="")
            row = int(input())
            print("Enter column: ", end="")
            col = int(input())
            loc = col + 10*(row-1)
            move = loc
            if move not in player_board.keys():
                print('  ▸ You hit a homerun! It\'s just not a good thing in this game.')
            elif move in player_moves:
                print('  ▸ C\'mon! You hit it twice! That is cheating.')
            else: 
                if pc_board[move] == 'O':
                    pc_point -= 1 
                    print(f'  ▸ Nice shot, Player. {pc_point} to go!')
                    score = True
                else:
                    print('  ▸ Oh! That was a miss. Try harder next time.')
            
            player_moves.append(move)
        
        if turn == 'Computer':
            score = False
            print(' ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
            print('\033[1m Computer turn:\033[0m')
            move = random.sample(player_board.keys(), 1)
            print(move[0])
            if player_board[move[0]] == 'O':
                player_point -= 1
                print(f'  ▸ Nice shot, Computer. {player_point} to go!')
                score = True
            elif move in pc_moves:
                print('  ▸ C\'mon! You hit it twice! That is cheating.')
            else:
                print('  ▸ Oh! That was a miss. Try harder next time.')

            pc_moves.append(move)
            
        ## check if the ships are all destroyed or no more turns
        if pc_point == 0:
            print('  ▸ Congrats, Player! You destroyed all the NPC ships.')
            break
        if player_point == 0:
            print('  ▸ Game over! Your ships were all destroyed. See you check_for_game_over!')
            break
                    
        #change player after each turn
        if turn == 'Player':
            if score == True:
                turn = 'Player'
            else:
                turn = 'Computer'
        else:
            if score == True:
                turn = 'Computer'
            else:
                turn = 'Player'
            
        print(f'\n\033[1m Player\'s point:\033[0m {player_point} | \033[1m Computer\'s point:\033[0m {pc_point}')
        
        round += 1
        cont_game = check_for_game_over(pc_point, player_point, round)
    
    restart = input('Do you want to play again? (Y/N)')
    if restart == 'Y':
        game()
    else:
        print('Good bye! See you next time.')

        
print("")
game()
