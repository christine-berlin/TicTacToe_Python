# print game board
def print_board(board):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

# check rows, columns and diagonals for winner
def check_winner(board):
    cond1 = (board[0]== board[1] ==board[2])  or  (board[3]== board[4]==board[5]) or  (board[6]== board[7]==board[8])
    cond2 = (board[0]== board[3] ==board[6])  or  (board[1]== board[4]==board[7]) or  (board[2]== board[5]==board[8])
    cond3 = (board[0]== board[4] ==board[8])  or  (board[2]== board[4]==board[6])
    
    if cond1 or cond2 or cond3:
        return True
    return False 

# write X or 0 into the board
def make_move(board, symbol, var):
    index = board.index(var)
    board[index] = symbol
    return board

if __name__ == "__main__":

    # initialize board
    board = ["a1","a2","a3","b1","b2","b3","c1", "c2", "c3"]
    print_board(board)
    print("Player1 = X, Player2 = O")
    player = ["Player 1", "Player 2"]

    game = True

    while game:
        for i in range(9):
            if i%2 ==0: 
                p = player[0]
                symbol = "X"
            else: 
                p = player[1]
                symbol = "O"

            #print(f'{p} choose a field: ')
            print('{} choose a field: '.format(p))
            var = input(' ')

            if var in board:
                make_move(board, symbol, var)
            
            else:
                # check for incorrect input
                input_wrong=True
                while input_wrong:
                    var = input("Choose another field:")       
                    if var in board:
                        make_move(board, symbol, var)
                        input_wrong=False   
        

            print_board(board)

            if check_winner(board) == True: 
                print(f'{p} won!')
                break

        if check_winner(board) == False: 
            print("It's a tie")

        print("You want to play one more time? Y/N")    
        var = input(' ')
        if var == 'N': 
            game = False
            break
        if var == 'Y': 
            board = ["a1","a2","a3","b1","b2","b3","c1", "c2", "c3"]
        else:
            input_wrong=True
            while input_wrong:
                var = input("Please type 'Y' or 'N': ")       
                if var == 'Y':
                    game=True
                    input_wrong=False   
                if var == 'N':
                    game=False
                    input_wrong=False
