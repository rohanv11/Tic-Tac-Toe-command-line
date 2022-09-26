import os
import sys
game = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
global count
count=0

'''
TIC TAC TOE
'''
 
def checkresult(p1,p2):
    value = 0 #to check if somebody won or not
    for i in range(9):
        if game[i]==" ":
            game[i]=6 #random value to occupy position
    result=[]
    result.append(list(set((game[0],game[4],game[8]))))
    result.append(list(set((game[0],game[3],game[6]))))
    result.append(list(set((game[1],game[4],game[7]))))
    result.append(list(set((game[3],game[4],game[5]))))
    result.append(list(set((game[2],game[5],game[8]))))
    result.append(list(set((game[2],game[4],game[6]))))
    result.append(list(set((game[6],game[7],game[8]))))
    result.append(list(set((game[0],game[1],game[2]))))
    
    for i in range(8):
        if len(result[i]) == 1 and result[i][0] != 6:
            if result[i][0] == p1 :
                print("Player 1 wins!")
            else :
                print("Player 2 wins!")
            value=1
    if value == 1 or count==9:
        return 1 #game stops
    #else :
     #   return 2 #game resumes
    for i in range(9):
        if game[i] == 6:
            game[i] = " "
    return 2 #game resumes!
            

def begin():
    n=2
    print("""press 1: for Player1 = 'X' and Player2 = 'O'
press 2: for Player1 = 'O' and Player2 = 'X'""")
    tr = int(input("Enter option : "))
    if tr == 1:
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'
    while True:
        print("Player 1's turn :")
        player(player1)
        n = checkresult(player1,player2)
        if n==1:
            if count==9:
                print("Match Drawn!")
                sys.exit()
            else:
                sys.exit()
        print("Player 2's turn :")
        player(player2)
        n = checkresult(player1,player2)
        if n==1:
            if count==9:
                print("Match Drawn!")
                sys.exit()
            else:
                sys.exit()
            
def print_game():
    os.system('cls')
    print(game[0]+" |"+game[1]+" |"+game[2])
    print("__|__|__")
    print(game[3]+" |"+game[4]+" |"+game[5])
    print("__|__|__")
    print(game[6]+" |"+game[7]+" |"+game[8])
    print("  |  |  ")
    print("Value of count :",count)
    
def player(p):
    global count
    print("Choose an empty space from 1 to 9 : ")
    t = int(input("Enter position of '"+p+"' : "))
    if game[t-1] != ' ' :
        print("Space not empty")
        player(p)
    else:
        game[t-1]=p
        count=count+1
        print_game()


#code starts!    
print("The pattern of tic tac toe board is as follows :")
print("""
1 |2 |3 
__|__|__
4 |5 |6 
__|__|__
7 |8 |9 
  |  |
      """)
begin()