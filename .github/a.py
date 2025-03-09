import numpy as np
Matrix = np.array([["-", "-", "-"],
                             ["-", "-", "-"],
                             ["-", "-", "-"]])


checker=False

player1= input("make your move! ")
player2= input("make your movie!")

def player1_turn():
    if (player1 == "1"):
        Matrix[0] = "X"
    elif player1 == "2":
        Matrix[1] = "X"
    elif player1 == "3":
            Matrix[2] = "X"
    elif player1 == "4":
        Matrix[3] = "X"
    elif player1 == "5":
            Matrix[4] = "X"
    elif player1 == "6":
        Matrix[5] = "X"
    elif player1 == "7":
            Matrix[6] = "X"
    elif player1 == "8":
            Matrix[7] = "X"
    elif player1 == "9":
            Matrix[8] = "X"

#-------------------------------------------------------

def player2_turn():
    if (player2 == "1"):
        Matrix[0] = "O"
    elif player2 == "2":
        Matrix[1] = "O"
    elif player2 == "3":
            Matrix[2] = "O"
    elif player2 == "4":
        Matrix[3] = "O"
    elif player2 == "5":
            Matrix[4] = "O"
    elif player2 == "6":
        Matrix[5] = "O"
    elif player2 == "7":
            Matrix[6] = "O"
    elif player2 == "8":
            Matrix[7] = "O"
    elif player2 == "9":
            Matrix[8] = "O"

#-------------------------------------------------------
def checkHorizontleCondition(Matrix):
    global winner
    if Matrix[0] == Matrix[1] == Matrix[2] and Matrix[0] != "":
        winner = Matrix[0]
        return True
    elif Matrix[3] == Matrix[4] == Matrix[5] and Matrix[3] != "":
        winner = Matrix[3]
        return True
    elif Matrix[6] == Matrix[7] == Matrix[8] and Matrix[6] != "":
        winner = Matrix[6]
        return True

#-------------------------------------------------------
def checkColCondition(Matrix):
    global winner
    if Matrix[0] == Matrix[3] == Matrix[6] and Matrix[0] != "":
        winner = Matrix[0]
        return True
    elif Matrix[1] == Matrix[4] == Matrix[7] and Matrix[1] != "":
        winner = Matrix[1]
        return True
    elif Matrix[2] == Matrix[5] == Matrix[8] and Matrix[2] != "":
        winner = Matrix[2]
        return True
#-----------------------------------------------------------    

 
def checkDiagonalCondition(Matrix):
     global winner
     if Matrix[0] == Matrix[4] == Matrix[8] and Matrix[0] != "":
        winner = Matrix[0]
        return True
     elif Matrix[2] == Matrix[4] == Matrix[6] and Matrix[2] != "":
        winner = Matrix[2]
        return True
    
    
    
while (player1 <10 and palyer2<10):
         print("palyer1 turn")
         player1 = input("enter your choose")
         if player1 == "1":
              Matrix[0]= "X"
         elif player1 == "2":
              Matrix[1]= "X"
         elif player1 == "3":
              Matrix[2]= "X"
         elif player1 == "4":
              Matrix[3]="X"
         elif player1 == "5":
              Matrix[4]="X"
         elif player1 == "6":
              Matrix[5] = "X"





              
              

         
         