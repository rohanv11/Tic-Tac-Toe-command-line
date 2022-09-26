"""
Priority :
    win DONE
    block DONE
    strategy block or win DONE (beta)
    random move DONE (beta) (situation where you cannot do anything block or win)
"""
import os
import sys
import random

List_of_resultcombinations=[[0,4,8],[0,3,6],[1,4,7],[3,4,5],[2,5,8],[2,4,6],[6,7,8],[0,1,2]]


game = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
tempgame = []
List_of_centre=[5]
List_of_remaining_except_centre=[1,2,3,4,6,7,8,9]
List_of_corners=[1,3,7,9]
List_of_side_edges=[2,4,6,8]
List_of_cpu_starting_first_elements =[1,3,5,7,9]

global count
count=0

'''
TIC TAC TOE
'''
def CPU_FirstMove(player,cpu): #implement!
    global count
    print("FirstCPU!!")
    r = random.choice(List_of_cpu_starting_first_elements)
    game[r-1]=cpu
    count+=1
    

def player_computer(cpu): #Random SHIT
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

def second_move(player,cpu):
    global count
    found=0
    for i in range(1,10):
        if game[i-1] == player:
            found = i
            break
    if found in List_of_remaining_except_centre:
        game[5-1]=cpu
        count+=1
        return
    else:
        r = random.choice(List_of_corners)
        game[r-1]=cpu
        count+=1
        return


def win_or_block(player,cpu,choice,g): 
    global count
    for i in range(9):
        if game[i] == " ":
            game[i] = 6
    result=[]
    result.append(list((game[0],game[4],game[8])))
    result.append(list((game[0],game[3],game[6])))
    result.append(list((game[1],game[4],game[7])))
    result.append(list((game[3],game[4],game[5])))
    result.append(list((game[2],game[5],game[8])))
    result.append(list((game[2],game[4],game[6])))
    result.append(list((game[6],game[7],game[8])))
    result.append(list((game[0],game[1],game[2])))
    countCpu=0
    countPlayer=0
    count6=0
    j=-1 #keep track of index of i
    if g!=25:
        for i in result:
            j+=1
            countCpu=i.count(cpu)
            countPlayer=i.count(player)
            count6=i.count(6)
            if count6 == 1 and countCpu == 2 and choice == 1: # win structure
                if game[List_of_resultcombinations[j][0]] == 6:
                    game[List_of_resultcombinations[j][0]] = cpu
                    count+=1
                    resubstitute()
                    print_game()
                    print("\n\nCPU WINS!!")
                    sys.exit()
                elif game[List_of_resultcombinations[j][1]] == 6:
                    game[List_of_resultcombinations[j][1]] = cpu
                    count+=1
                    resubstitute()
                    print_game()
                    print("\n\nCPU WINS!!")
                    sys.exit()
                elif game[List_of_resultcombinations[j][2]] == 6:
                        game[List_of_resultcombinations[j][2]] = cpu
                        count+=1
                        resubstitute()
                        print_game()
                        print("\n\nCPU WINS!!")
                        sys.exit()
            elif count6 == 1 and countPlayer == 2 and choice == 0: #block structure
           # if g == 25:
            #    return 2
                if game[List_of_resultcombinations[j][0]] == 6:
                    game[List_of_resultcombinations[j][0]] = cpu
                    count+=1
                    break
                elif game[List_of_resultcombinations[j][1]] == 6:
                    game[List_of_resultcombinations[j][1]] = cpu
                    count+=1
                    break
                elif game[List_of_resultcombinations[j][2]] == 6:
                    game[List_of_resultcombinations[j][2]] = cpu
                    count+=1
                    break
    elif g==25:   #Call from Best move (g=25)          
    #====================================================================================
        j=-1 #keep track of index of i
        temp = 0
        for i in result:
            j+=1
            countCpu=i.count(cpu)
            countPlayer=i.count(player)
            count6=i.count(6)
            if count6 == 1 and countPlayer == 2 and choice == 0:
                temp+=1
        if temp == 2:
            return 2
        if temp == 1:
            return 1
        return 0
    #====================================================================================
    resubstitute()
    
def resubstitute():
    for i in range(9):
        if game[i] == 6:
            game[i] = " "


def bestMove(player,cpu):  #working partly
    print("Reached best move block!")
    global count
    for i in range(9):
        if game[i] == " ":
            game[i] = 6
    for i in range(9):
        tempgame.append(game[i]) #tempgame holds my actual game!!
    ListOfPossibleSolutions = [] #countofcombs = 1
    ListOfClashingCombinations = [] #countofcombs = 2

    for i in range(9):
        if game[i] == 6:
            game[i] = player
            n=win_or_block(player,cpu,0,25)
            if n == 1:
                ListOfPossibleSolutions.append(i)
            elif n == 2:
                ListOfClashingCombinations.append(i)
            game[i] = 6 #DOUBTFUL
    resubstitute()
    print("List of posssible combinations :",ListOfPossibleSolutions)
    print("List of clashing combinations :",ListOfClashingCombinations)
    if len(ListOfClashingCombinations) != 0:
        r = random.choice(ListOfClashingCombinations)
        game[r] = cpu
        count+=1 
        return
    if len(ListOfPossibleSolutions) != 0:
        r = random.choice(ListOfPossibleSolutions)
        game[r] = cpu
        count+=1
        return
    if len(ListOfPossibleSolutions) == 0:
        print("RandomMoveExecuted/nPLEASE WRITE CODE IF IT EVER COMES HERE ONNNNLYYY!!!")
        """
        t = random.randint(1,9)
        while True:
            if game[t-1] != " " :
                t=random.randint(1,9)
            else :
                game[t-1]=cpu
                count+=1
                break
        """
    
        
def generic_move(player,cpu): 
    global count
    var = 1
    """
    var = 0 check for block
    var = 1 check for win
    """
    newCount = count
    win_or_block(player,cpu,var,0) #check for win
    if newCount == count :
        var = 0 
        win_or_block(player,cpu,var,0) #try to block
    if newCount == count :
        if count == 3 and (game[5-1] == cpu or game[5-1] == player):###
            if(game[1-1] != " " and game[9-1] != " ") or (game[3-1] != " " and game[7-1] != " "): ###
                print("Reached special move!") #Special move! for diagonal elements!
                if game[5-1] == cpu:
                    r = random.choice(List_of_side_edges)
                    game[r-1] = cpu
                elif game[5-1] == player:
                    r = random.choice(List_of_corners)
                    while True:
                        if game[r-1] != " " :
                            r = random.choice(List_of_corners)
                        else :
                            game[r-1] = cpu
                            break
                count+=1
            else:  ###
                bestMove(player,cpu)
        else:
            bestMove(player,cpu)

def masterplayer(player,cpu):
    print("<======CPU SHOWING OFF!!======>")
    global count
    if count == 1:
        second_move(player,cpu)
    if  count >= 3:
        generic_move(player,cpu)
    

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
            #print("var : ",var)
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
press 2: for Player1 = 'O' and CPU = 'X'
press 3: CPU plays first =>""")
    tr = int(input("Enter option : "))
    if tr == 1:
        player1 = 'X'
        cpu = 'O'
    else:
        player1 = 'O'
        cpu = 'X'
        
    if tr == 3:
        cpu = 'X'
        player1 = 'O'
        CPU_FirstMove(player1,cpu)
        while True:
            print_game()
            checkresult(player1,cpu)
            
            player(player1)
            print_game()
            checkresult(player1,cpu)
              
    else:    
        while True:
            print("Player1's turn :")
            player(player1)
            print_game()
            checkresult(player1,cpu)

        
            masterplayer(player1,cpu)
            print_game()
            checkresult(player1,cpu)
         
def print_game():
    #os.system('clear')
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
