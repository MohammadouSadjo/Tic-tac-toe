from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    
    print("+-------" * 3, "+", sep="")
    for b_row in range(3):
        print("|       " * 3, "|", sep="")
        for b_column in range(3):
            print("|   " , (board[b_row][b_column]), "   ", sep="", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    
    verif = True 
    while verif :
        choice = int(input("Enter your move: "))
        print(isinstance(choice, int))
        if not (isinstance(choice, int) and int(choice)>0 and (choice) < 9):
            #status=True
            print("Enter a correct move!")
            continue
        
        choice = choice - 1
        b_row = choice // 3 
        b_column =  choice % 3
        if (board[b_row][b_column] in ['X','O']):
            print("Choose a not used box")
            continue
        
        board[b_row][b_column]= "O"
        
        #ending loop action
        verif = False

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    
    free_fields = []
    for row in range(3):
        for column in range(3):
            if board[row][column] not in ["X","O"]:
                free_fields.append((row,column))
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    if sign == "X":
        winner = "Computer" 
    elif sign == "O": 
        winner = 'Player1'  
    
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign: 
            return winner
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return winner
        
        if board[0][0] == "X" and board[2][2] == "X":
            return "Computer"
        if board[0][2] == "X" and board[2][0] == "X":
            return "Computer"
        
    return None

def draw_move(board):
    # The function draws the computer's move and updates the board.
    
    free_fields = make_list_of_free_fields(board)
    height = len(free_fields)
    if height > 0:
        cpu_choice = randrange(height)
        b_row, b_column = free_fields[cpu_choice]
        board[b_row][b_column] = 'X'

#board = for i in range(3):
board = [[3*i+j+1 for j in range(3)] for i in range(3)]

board[1][1]="X"

free_fields = make_list_of_free_fields(board)
player1 = True 
while len(free_fields):
    display_board(board)
    if player1:
        enter_move(board)
        winner = victory_for(board,'O')
    else:   
        draw_move(board)
        winner = victory_for(board,'X')
    
    if winner != None:
        break
    
    player1 = not player1       
    free = make_list_of_free_fields(board)

display_board(board)

if winner == 'Player1':
    print("Victory Player 1!")
elif winner == "Computer":
    print("Victory CPU!")
else:
    print("Draw")