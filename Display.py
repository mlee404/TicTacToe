from TicTacToe import *;
## (FOR THE DISPLAY)
##Print current game.
##Print prompts ('Player X/O, your move')
##Print victory (X wins/O wins/ Cat's Game!)
def gameLoop():
    #Terminating Condition: X has not won, O has not won, and there are still spaces.
    while checkVictory(playerX) == False and checkVictory(playerO) == False and checkCatsGame() == False:
        printPlayerPrompt();
        printCurrentGameBoard();
    if(checkVictory(playerX) == True or checkVictory(playerO) == True):
        printVictoryMessage(playerTurn);
    else:    
        print("Cat Game.");

#Print the state of the game board.
def printCurrentGameBoard():
    for i in range(1,10):
        if i in playerX:
            print('X', end='');
        elif i in playerO:
            print('O', end='');
        else: print('- ',end='');
        if i%3 == 0:
            print("\n");

def printVictoryMessage(playerTurn):
    if(playerTurn):
        print("VICTORY TO PLAYER O!");
    else:
        print("VICTORY TO PLAYER X!");

    
def printPlayerPrompt():
    if(getActivePlayer()):
        print("It is Display O's Turn.");
    else:
        print("It is Display X's Turn.");
    space = input("Which space will you pick?  ");
    handlePlayerInput(space);
        

def handlePlayerInput(inputString):
    ##If the input is 1-9, then that is a valid space.
    ##If it is a string, then we can't do anything with it.
    try:
        x = True;
        if(int(inputString) in range(1,10) and checkSpace(int(inputString))):
            while x==True:
                if(getActivePlayer()):
                    if(playerSpaceAdded(playerO, int(inputString))==True):
                        x = False;
                        updateActivePlayer();
                    else:
                        print("FAILED.  TRY AGAIN.");
                else:
                    if(playerSpaceAdded(playerX, int(inputString))==True):
                        addSpace(playerX, int(inputString));
                        x = False;
                        updateActivePlayer();
                    else:
                        print("FAILED.  TRY AGAIN.");
                print(" IS A NUMBER.");

        else:
            print("IS NOT A VALID NUMBER.");
    except ValueError:
        print("That's not a valid space!");
        
    
    print("Handle it!");
