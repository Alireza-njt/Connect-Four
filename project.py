# Alireza Nejati (alirezanejatiz27@gmail.com)
# Saturday , July 26 , 2025
# Course name : CS50's Introduction to Programming with Python
# Final project name : Connect Four

from colorama import Fore, Style
from pyfiglet import Figlet

piece_char = '⬤'  # final variable
Red = Fore.RED + piece_char + Style.RESET_ALL  # final variable
Yellow = Fore.YELLOW + piece_char + Style.RESET_ALL  # final variable
Empty = None  # final variable
rows = 6  # final variable
cols = 7  # final variable

state = None


def initial_state(rows=rows, cols=cols):
    state = [[Empty for _ in range(cols)] for _ in range(rows)]
    return state


def actions(state):
    result = []
    for col in range(cols):
        for row in range(rows-1, -1, -1):
            if state[row][col] == Empty:
                result.append((row, col))
                break
    return result


def result(state, action, player_color, rows=rows, cols=cols):
    new_state = [i[:] for i in state]
    i_action, j_action = action
    if state[i_action][j_action] == Red or state[i_action][j_action] == Yellow:
        raise NotImplementedError
    else:
        new_state[i_action][j_action] = player_color
        return new_state


def winner(state, rows=rows, cols=cols):
    def find_quadruples():
        rows = len(state)
        if rows == 0:
            return []
        cols = len(state[0])
        quadruples = []
        for i in range(rows):
            for j in range(cols - 3):
                quadruple = (i, j), (i, j + 1), (i, j + 2), (i, j + 3)
                quadruples.append(quadruple)

        for i in range(rows - 3):
            for j in range(cols):
                quadruple = (i, j), (i + 1, j), (i + 2, j), (i + 3, j)
                quadruples.append(quadruple)

        for i in range(rows - 3):
            for j in range(cols - 3):
                quadruple = (i, j), (i + 1, j + 1), (i + 2, j + 2), (i + 3, j + 3)
                quadruples.append(quadruple)

        for i in range(3, rows):
            for j in range(cols - 3):
                quadruple = (i, j), (i - 1, j + 1), (i - 2, j + 2), (i - 3, j + 3)
                quadruples.append(quadruple)

        return quadruples
    for q in find_quadruples():
        q1, q2, q3, q4 = q
        q1x, q1y = q1
        q2x, q2y = q2
        q3x, q3y = q3
        q4x, q4y = q4
        if (state[q1x][q1y] == state[q2x][q2y] == state[q3x][q3y] == state[q4x][q4y] == Red):
            return Red
        elif (state[q1x][q1y] == state[q2x][q2y] == state[q3x][q3y] == state[q4x][q4y] == Yellow):
            return Yellow
    return None


def terminal(state, rows=rows, cols=cols):
    if winner(state) == Red or winner(state) == Yellow:
        return True

    for i in range(rows):
        for j in range(cols):
            if state[i][j] == Empty:
                return False

    return True


def utility(state, rows=rows, cols=cols):
    if winner(state, rows, cols) == Red:
        return 1
    elif winner(state, rows, cols) == Yellow:
        return -1
    elif winner(state, rows, cols) is None and terminal(state, rows, cols) is True:
        return 0
    return 0


def minimax(state, turn):
    def max_value(board, alpha, beta, depth):
        if terminal(board) or depth == max_depth:
            return utility(board), None

        value = float('-inf')
        best_move = None
        for action in actions(board):
            new_state = result(board, action, turn)
            new_value, _ = min_value(new_state, alpha, beta, depth+1)

            if new_value > value:
                value = new_value
                best_move = action
                alpha = max(alpha, value)

            if value >= beta:
                break

        return value, best_move

    def min_value(board, alpha, beta, depth):
        if terminal(board) or depth == max_depth:
            return utility(board), None

        value = float('inf')
        best_move = None
        for action in actions(board):
            opponent = Yellow if turn == Red else Red
            new_state = result(board, action, opponent)
            new_value, _ = max_value(new_state, alpha, beta, depth+1)

            if new_value < value:
                value = new_value
                best_move = action
                beta = min(beta, value)

            if value <= alpha:
                break

        return value, best_move

    max_depth = 5
    alpha = float('-inf')
    beta = float('inf')

    if terminal(state):
        return None

    if turn == Red:
        _, action = max_value(state, alpha, beta, 0)
    else:
        _, action = min_value(state, alpha, beta, 0)

    return action


def print_ascii_art_text(text, font='slant'):
    F = Figlet()
    F.setFont(font=font)
    print(F.renderText(text), end='')


def print_board(state, rows=rows, cols=cols):

    print("  " + "   ".join(Fore.BLUE + str(i+1) + Style.RESET_ALL for i in range(cols)))

    for i in range(rows):
        print(" ---" * cols)
        for j in range(cols):
            key = state[i][j]
            if key in [Red, Yellow]:
                print(f"| {key} ", end="")
            else:
                print("|   ", end="")
        print("|")

    print(" ---" * cols)


def main():
    print_ascii_art_text('Connect Four !')
    print('by : Alireza Nejati')
    print('-'*125)
    user_color = None
    while True:
        user_color = input('please inter your color [between Red or Yellow] : ').capitalize()
        user_color = user_color.strip()
        if user_color == 'Red' or user_color == 'Yellow':
            if user_color == 'Red':
                user_color = Red
            else:
                user_color = Yellow
            break
        else:
            print(Fore.RED + 'Invalid color ! please type another color !!' + Style.RESET_ALL)
    ai_turn = False
    ai_color = Red if user_color == Yellow else Yellow
    state = initial_state()
    while True:
        print('*'*125)
        print_board(state)
        if ai_turn:
            ai_move = minimax(state, ai_color)
            state = result(state, ai_move, ai_color)
            ai_turn = False
        else:
            user_action_completed = False
            while True:
                if user_action_completed:
                    break
                user_actions = actions(state)
                while True:
                    user_col_choice = input(
                        'Please specify which column you want to drop the piece into : ')
                    user_col_choice = int(user_col_choice)
                    if 1 <= user_col_choice and user_col_choice <= 7:
                        break
                    else:
                        print(
                            Fore.RED + 'Invalid number ! please type another number between 1 to 7 !!' + Style.RESET_ALL)
                user_col_choice -= 1
                for a in user_actions:
                    a_row, a_col = a
                    if a_col == user_col_choice:
                        state = result(state, (a_row, a_col), user_color)
                        ai_turn = True
                        user_action_completed = True
                        break
        if terminal(state):
            print_board(state)
            if winner(state) == ai_color:
                print_ascii_art_text('AI Wins !')
            elif winner(state) == user_color:
                print_ascii_art_text('you Wins !')
            else:
                print_ascii_art_text('Draw !')
            break


if __name__ == "__main__":
    main()
