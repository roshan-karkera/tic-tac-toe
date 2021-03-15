from board import printBoard
from board import game_board
def game():
    turn = 'X'
    count = 0
    game_board = {'7': ' ', '8': ' ', '9': ' ',
                '4': ' ', '5': ' ', '6': ' ',
                '1': ' ', '2': ' ', '3': ' '}


    for i in range(10):
        printBoard(board=game_board)
        print("Its your turn", turn, " Move to which place:")
        move = input()
        if game_board[move] == ' ':
            game_board[move] = turn
            count += 1
        else:
            print("That place is already filled\n.Move to which place?")
            continue

        if count >= 5:
            if game_board['7'] == game_board['8'] == game_board['9']:
                printBoard(board = game_board)
                print("Game Over!,\n")
                print("You" + turn + "Won!")
                break
            elif game_board['4'] == game_board['5'] == game_board['6']:
                printBoard(board=game_board)
                print("Game Over!,\n")
                print("You" + turn + "Won!")
                break
            elif game_board['1'] == game_board['2'] == game_board['3']:
                printBoard(board=game_board)
                print("Game Over!,\n")
                print("You" + turn + "Won!")
                break
            elif game_board['7'] == game_board['5'] == game_board['3']:
                printBoard(board=game_board)
                print("Game Over!,\n")
                print("You" + turn + "Won!")
                break
            elif game_board['9'] == game_board['5'] == game_board['1']:
                printBoard(board=game_board)
                print("Game Over!,\n")
                print("You" + turn + "Won!")
                break
            elif game_board['7'] == game_board['4'] == game_board['1']:
                printBoard(board=game_board)
                print("Game Over!,\n")
                print("You" + turn + "Won!")
                break
            elif game_board['8'] == game_board['5'] == game_board['2']:
                printBoard(board=game_board)
                print("Game Over!,\n")
                print("You" + turn + "Won!")
                break
            elif game_board['9'] == game_board['6'] == game_board['3']:
                printBoard(board=game_board)
                print("Game Over!,\n")
                print("You" + turn + "Won!")
                break

        if count == 9:
            print("Game over!, \n")
            print("It's a Tie!!")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


