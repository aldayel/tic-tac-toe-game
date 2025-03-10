import numpy as np

# Initialize the game 
Matrix = np.array([["-", "-", "-"],
                   ["-", "-", "-"],
                   ["-", "-", "-"]])

# Function to display the current board state = Matrix
def display_Matrix():
    print("\nCurrent Board:")
    for i in range(3):
        print(" | ".join(Matrix[i])) 

        print("-" * 9) # 9 empty indexes 

# Function to check for a winer
def check_winner():
    # Check rows first
    for i in range(3):
        if Matrix[i][0] == Matrix[i][1] == Matrix[i][2] and Matrix[i][0] != "-":
            return Matrix[i][0] 
        # not changing the i which stands for row number and ckeck all the elemnts or boxes in the rows to check


    # Check columns, like rows 
    for i in range(3):
        if Matrix[0][i] == Matrix[1][i] == Matrix[2][i] and Matrix[0][i] != "-":
            return Matrix[0][i]
    
    
    # Check diagonals, by having two possible ways to way in diagonal way ( from left to right and from right to left)

    if Matrix[0][0] == Matrix[1][1] == Matrix[2][2] and Matrix[0][0] != "-":
        return Matrix[0][0]
    if Matrix[0][2] == Matrix[1][1] == Matrix[2][0] and Matrix[0][2] != "-":
        return Matrix[0][2]
    
#---------------------------------------------------

# Main LOOP
def play_game():
    print("Tic Tac Toe!")
    
    for turn in range(9):  # Maximum of 9 turns, cause logically can't a player plays more than that so we have to set a boundry for this
                            # and a player can't play two moves or more in one round >> so even number = player 1 and odd = player2
        display_Matrix()
        if turn % 2 == 0:
            current_player = "X"
            move = int(input("Player 1 X Enter your move (1-9): ")) - 1 #the main diffrence between the player aspect and the programmer aspect is the indexing in this game
            # from player aspect the game indexing is from 1-9 unlike the programming aspect which it 0-8 ( can't skip the index 0, or to be honest i don't know )
        else:
            current_player = "O"
            move = int(input("Player 2 O Enter your move (1-9): ")) - 1
        
        # Check if the move is valid
        if move < 0 or move > 8 or Matrix[move // 3][move % 3] != "-": # the following "Matrix[move // 3][move % 3] != "-":" i google it and understands why it is the best approach to apply for the game case
            print("the move is not valid")
            continue
        
        # Update the board
        Matrix[move // 3][move % 3] = current_player


        #---------------------------------------------------
        
        
        # Check for win case
        winner = check_winner()
        if winner:
            display_Matrix()
            print(f"Congratulations! Player {1 if winner == 'X' else 2} ({winner}) wins!")
            return
    

    #---------------------------------------------------

# Start the game
    play_game()
