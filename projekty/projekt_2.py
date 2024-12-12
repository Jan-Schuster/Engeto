##############################################################################

'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie

autor: Jan Schuster
email: schuster.jan@seznam.cz
'''


from project_2_module import (initial_text, who_is_first_X_or_O, 
            clear_the_board, who_is_first_comp_or_human, check_the_correctness, 
            assign_values, draw_the_board, player_OX_setter, 
            player_move_number, comp_random_move, check_if_not_integer, 
            convert_num_to_int, check_num_in_range, available_squares,
            set_the_sign_XY_to_square, the_winner_check, the_winner_declaration, 
            add_number_one, draw_it_is, comp_forced_move, comp_forced_display)


squares = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
double_liner = '=' * 44
single_liner = '-' * 44
counter = 1
first_player = ''
second_player = ''
comp_or_man_first = ''
comp_or_man_second = ''

clear_the_board()

#display the initial text and the board 
initial_text(double_liner, single_liner)

# let the user define who is supposed to move as first - X or O
while True:
    first_player = who_is_first_X_or_O()
    if check_the_correctness(first_player, 'X', 'O'):
        break

second_player = assign_values(first_player, second_player, 'X', 'O')

# let the user define who is supposed to move as computer or man
while True:
    comp_or_man_first = who_is_first_comp_or_human()
    if check_the_correctness(comp_or_man_first, 'C', 'H'):
        break

comp_or_man_second = assign_values(comp_or_man_first, comp_or_man_second, 
                                   'C', 'H')

draw_the_board(squares)

while True:
    # define if it is the 'X' or 'O' player's turn
    playerOX = player_OX_setter(counter, first_player, second_player)

    # define if it is computer's or man's move
    if counter % 2 == 1 and comp_or_man_first == 'C':
        # check if the computer's move is forced
        if comp_forced_move(squares, first_player, second_player) is not None:
            inputNum = str(comp_forced_move(squares, first_player, 
                                            second_player))
            comp_forced_display(double_liner, playerOX, inputNum)
        # if the computer's move is not forced let the comp play ranfom move
        else:
            inputNum = str(comp_random_move(double_liner, playerOX, squares))
    elif counter % 2 == 1 and comp_or_man_first == 'H':
        inputNum = player_move_number(double_liner, playerOX)
    elif counter % 2 == 0 and comp_or_man_second == 'C':
        print(squares)
        print(first_player, second_player)
        if comp_forced_move(squares, second_player, first_player) is not None:
            inputNum = str(comp_forced_move(squares, second_player, 
                                            first_player))
            comp_forced_display(double_liner, playerOX, inputNum)            
        else:
            inputNum = str(comp_random_move(double_liner, playerOX, squares))
    else:
        inputNum = player_move_number(double_liner, playerOX)    

    #check if the input is a number
    if check_if_not_integer(inputNum):
        print(f"This: {inputNum} is not a number.\nYou should have "
              f"written\nan integer in the requested range: 1-{len(squares)}.\n"
              f"Please do better next time.")
        continue

    inputNum = convert_num_to_int(inputNum)

    # check if the input is a number in selected range
    if check_num_in_range(inputNum, squares):
        print(f"The number {inputNum} is not in requested range 1-"
            f"{len(squares)}\nplease do better next time.")
        continue

    #  check if the chosen square is available
    elif (inputNum - 1) not in available_squares(squares):
        print("The square you have selected is already occupied.\n"
              "Please select another square.")
        continue        

    # draw the board in case available square was selected
    else:
        set_the_sign_XY_to_square(squares, inputNum, playerOX)
        draw_the_board(squares)

    # check if winner exists - in that case quit the game
    if the_winner_check(squares, playerOX):
        the_winner_declaration(double_liner, playerOX)
        break

    counter = add_number_one(counter)

    # check the draw - in that case quit the game
    if counter > 9:
        draw_it_is(double_liner)
        break

##############################################################################
