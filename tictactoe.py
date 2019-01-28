"""

Tic tac toe game for 2 players to play in terminal
"""

def tic_tac_toe_game():
    """ Game tic tac toe to play in terminal"""

    print("Welcome to Tic Tac Toe!")
    print('')

    dict_players_token = assign_tokens()

    print("Player 1 will go first.")
    print('')

    while True:
        ready_to_play = input("Are you ready to play? Enter Yes or No.")

        if ready_to_play.lower() == 'yes':
            play(dict_players_token)
        elif ready_to_play.lower() == 'no':
            print("See you soon")
            print('')
            break
        else:
            print("You need to put yes or no")


def assign_tokens():
    """ Ask player for the token 'x' or 'o'
    return dictionari with players as keys and tokens as values"""

    while True:
        player1 = input("Player 1: Do you want to be X or O?")

        if player1.lower() == 'x':
            return {'Player1':'x', 'Player2':'o'}
        elif player1.lower() == 'o':
            return {'Player1':'o', 'Player2':'x'}


def play(dict_players_token):
    """Ask to players for positions and
    draw tokens in the board until someone wins or the turn ends"""

    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    display_board(board)

    turn = 0

    while turn < 9:

        position = int(input("Choose your next position: (1 - 9)"))

        position_in_range = check_position(position)

        if position_in_range and board[position] == ' ':
        # if it is the right position and the position is empty,
        # put the token depends on the turn
            if turn % 2 == 0:
                board[position] = dict_players_token['Player1']
            else:
                board[position] = dict_players_token['Player2']

            clear_screen()

            display_board(board)

            token_winner = check_winner(board)

            if token_winner:
                show_winner(token_winner, dict_players_token)
                break
            elif not token_winner and turn == 9:
                print('Nobody wins. Tie Game!')
                print('')

            turn += 1

        elif position_in_range and board[position] != ' ':
            print("This position is already ocupied. Try with an empty one")

        else:
            print("The number must be between 1 and 9, both included")


def display_board(board):
    """ Display the board"""

    print(board[7], '|', board[8], '|', board[9])
    print('---------')
    print(board[4], '|', board[5], '|', board[6])
    print('---------')
    print(board[1], '|', board[2], '|', board[3])
    print('')


def check_position(position):
    """ Check if the integer position is between 1 and 9, both included"""
    return position in range(1, 10)


def clear_screen():
    """Clear the screen"""
    print('\n' * 10)


def check_winner(board):
    """ If there is a winner return the token of the winner,
    else return None"""

    if board[7] == board[8] == board[9] and board[7] != ' ':
        return board[7]
    elif board[4] == board[5] == board[6] and board[4] != ' ':
        return board[4]
    elif board[1] == board[2] == board[3] and board[1] != ' ':
        return board[1]
    elif board[7] == board[5] == board[3] and board[7] != ' ':
        return board[7]
    elif board[9] == board[5] == board[1] and board[9] != ' ':
        return board[9]
    elif board[7] == board[4] == board[1] and board[7] != ' ':
        return board[7]
    elif board[8] == board[5] == board[2] and board[8] != ' ':
        return board[8]
    elif board[9] == board[6] == board[3] and board[9] != ' ':
        return board[9]


def show_winner(token_winner, dict_players_token):
    """ Show a message with the winner"""

    if token_winner == dict_players_token['Player1']:
        print('Congratulations! Player1 has won!')
        print('')
        print('')
    elif token_winner == dict_players_token['Player2']:
        print('Congratulations! Player2 has won!')
        print('')
        print('')


tic_tac_toe_game()
