import os
import sys
import random

game = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
global count
count=0

'''
TIC TAC TOE
'''

def player_computer(cpu):
    global count
    print("=====\n<==CPU playin his turn==>\n=====")
    t = random.randint(1,9)
    while True:
        if game[t-1] != " " :
            t=random.randint(1,9)
        else :
            break
    game[t-1]=cpu
    count+=1
    print_game()       
            
    

def checkresult(p1,cpu):
    value = 0 #value = 0 for game still on nobody won yet!
    for i in range(9):
        if game[i]==" ":
            game[i]=6
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
            var = result[i][0][0]
            print("var : ",var)
            value=1 #game ends
    if value == 0 :
        for i in range(9):
            if game[i]==6:
                game[i]=" "
                    
    if (value==1 and count<=9):
        if var == p1:
            print("\nPlayer1 wins!!\n")
        elif var == cpu:
            print("\nCPU wins!!\n")
        sys.exit()
    if value!=1 and count==9:
        print("\nMatch Drawn!!\n")
        sys.exit()
    if value!=1 and count<9:
        return
    
def begin():
    print("""press 1: for Player1 = 'X' and CPU = 'O'
press 2: for Player1 = 'O' and CPU = 'X'""")
    tr = int(input("Enter option : "))
    if tr == 1:
        player1 = 'X'
        cpu = 'O'
    else:
        player1 = 'O'
        cpu = 'X'
    while True:
        print("Player1's turn :")
        player(player1)
        checkresult(player1,cpu)
        
        player_computer(cpu)
        checkresult(player1,cpu)
        
def print_game():
    #os.system('clear')
    '''
    print(""",
          game[0] |game[1] |game[2]
          __|__|__
          game[3] |game[4] |game[5]
          __|__|__
          game[6] |game[7] |game[8]
            |  |  
          """)
    '''
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
    if game[t-1] != " " :
        print("Space not empty")
        player(p)
    else:
        game[t-1]=p
        count=count+1
        print_game()


    
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