##############################################################################
import os
import random

def initial_text(double_liner, single_liner):
    print("Welcome to Tic Tac Toe\n"
    f"{double_liner}\n"
    "GAME RULES:\n"
    "Each player can place one mark (or stone)\n"
    "per turn on the 3x3 grid. The WINNER is\n"
    "who succeeds in placing three of their\n"
    "marks in a:\n"
    "* horizontal,\n"
    "* vertical or\n"
    "* diagonal row\n"
    f"{double_liner}\n"
    "Let's start the game\n"
    f"{single_liner}")

def clear_the_board():
    os.system("cls")

def who_is_first_X_or_O():
    letter = input("Type in who should start the game first (X or O): ").upper()
    return letter

def who_is_first_comp_or_human():
    letter = input("Type in who should start the game first C or H\n"
                "C stands for computer and H stands for human: ").upper()
    return letter

def check_the_correctness(input, first_check, second_check):
    if input == first_check or input == second_check:
        return True
    else:
        print('Incorrect, try again please.\n')
        return False

def assign_values(first, scnd, first_letter, second_letter):
    if first == first_letter:
        scnd = second_letter
        return scnd
    else:
        scnd = first_letter
        return scnd

def draw_the_board(li):
    print("+---+---+---+\n"
    f"| {li[6]} | {li[7]} | {li[8]} |\n"
    "+---+---+---+\n"
    f"| {li[3]} | {li[4]} | {li[5]} |\n"
    "+---+---+---+\n"
    f"| {li[0]} | {li[1]} | {li[2]} |\n"
    "+---+---+---+")

def player_OX_setter(number, first_player, second_player):
    if number % 2 == 1:
        return first_player
    else:
        return second_player

def computers_turn(li):
    available_sqrs = available_squares(li)
    rand_idx = int(random.random() * len(available_sqrs))
    return available_sqrs[rand_idx] + 1

def comp_random_move(double_liner, player, li):
    print(f"{double_liner}")
    inputValue = computers_turn(li)
    print(f"Player {player} | Please enter your move number: {inputValue}")
    print(f"{double_liner}")
    return inputValue   

def comp_forced_display(double_liner, player, inputValue):
    print(f"{double_liner}")
    print(f"Player {player} | Please enter your move number: {inputValue}")
    print(f"{double_liner}")

def player_move_number(double_liner, player):
    print(f"{double_liner}")
    inputValue = input(f"Player {player} | Please enter your move number: ")
    print(f"{double_liner}")
    return inputValue

def check_if_not_integer(number):
    if number.isdigit() is False:
        return True
    else:
        return False

def convert_num_to_int(num):
    num = int(num)
    return num

def check_num_in_range(number, squares):
    if number not in range(1, len(squares) + 1):
        return True 

def available_squares(li):
    empty_squares = []
    for i, char in enumerate(li):
        if char == ' ':
            empty_squares.append(i)
    return empty_squares

def set_the_sign_XY_to_square(li, number, XorO):
    li[number - 1] = XorO

def the_winner_check(li, XorO):
    if (li[0] == li[1] == li[2] == XorO or li[3] == li[4] == li[5] == XorO or
        li[6] == li[7] == li[8] == XorO or
        li[0] == li[3] == li[6] == XorO or li[1] == li[4] == li[7] == XorO or
        li[2] == li[5] == li[8] == XorO or        
        li[0] == li[4] == li[8] == XorO or li[2] == li[4] == li[6] == XorO
        ):
        return True
    
def the_winner_declaration(double_liner, XorO):
    print(double_liner)
    print(f"Congratulations, the player {XorO} WON!")
    print(double_liner)

def add_number_one(num):
    return num + 1

def draw_it_is(double_liner):
    print(double_liner)
    print(f"It is a DRAW! No winner this time!")
    print(double_liner)

def comp_forced_move(li, player_1, player_2):
    if (li[0] == ' ' and
        ((li[1] == li[2] == player_1) or (li[1] == li[2] == player_2) or
        (li[3] == li[6] == player_1) or (li[3] == li[6] == player_2) or
        (li[4] == li[8] == player_1) or (li[4] == li[8] == player_2))):
        return 1
    elif (li[1] == ' ' and
        ((li[0] == li[2] == player_1) or (li[0] == li[2] == player_2) or
        (li[4] == li[7] == player_1) or (li[4] == li[7] == player_2))):
        return 2
    elif (li[2] == ' ' and
        ((li[0] == li[1] == player_1) or (li[0] == li[1] == player_2) or
        (li[5] == li[8] == player_1) or (li[5] == li[8] == player_2) or
        (li[4] == li[6] == player_1) or (li[4] == li[6] == player_2))):
        return 3
    elif (li[3] == ' ' and
        ((li[4] == li[5] == player_1) or (li[4] == li[5] == player_2) or
        (li[0] == li[6] == player_1) or (li[0] == li[6] == player_2))):
        return 4 
    elif (li[4] == ' ' and
        ((li[3] == li[5] == player_1) or (li[3] == li[5] == player_2) or
        (li[1] == li[7] == player_1) or (li[1] == li[7] == player_2) or
        (li[6] == li[2] == player_1) or (li[6] == li[2] == player_2) or                
        (li[0] == li[8] == player_1) or (li[0] == li[8] == player_2))):
        return 5    
    elif (li[5] == ' ' and
        ((li[3] == li[4] == player_1) or (li[3] == li[4] == player_2) or
        (li[2] == li[8] == player_1) or (li[2] == li[8] == player_2))):
        return 6 
    elif (li[6] == ' ' and
        ((li[7] == li[8] == player_1) or (li[7] == li[8] == player_2) or
        (li[3] == li[0] == player_1) or (li[3] == li[0] == player_2) or
        (li[4] == li[2] == player_1) or (li[4] == li[2] == player_2))):
        return 7
    elif (li[7] == ' ' and
        ((li[6] == li[8] == player_1) or (li[6] == li[8] == player_2) or
        (li[1] == li[4] == player_1) or (li[1] == li[4] == player_2))):
        return 8 
    elif (li[8] == ' ' and
        ((li[6] == li[7] == player_1) or (li[6] == li[7] == player_2) or
        (li[5] == li[2] == player_1) or (li[5] == li[2] == player_2) or
        (li[0] == li[4] == player_1) or (li[0] == li[4] == player_2))):
        return 9

##############################################################################