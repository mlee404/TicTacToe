##TicTacToe requires the following:

##(FOR THE GAME)

##Player X
##Player O
##Numbers 1 - 9 (Correspond to spaces).  Can be modified for 2D array too
##or Tuples.

## (FOR INPUT/OUTPUT)
##Read Input
##Handle Input


## (FOR THE DISPLAY)
##Print game state.


##This is the Game Controller.  The controller will keep track of
##both active players, add spaces which they have chosen, determine the victor,
##and reset the game.

playerX = [];
playerO = [];
playerTurn = False; ##False = X, True = O

##Who's turn is it?
def getActivePlayer():
    return playerTurn;

##Switch who is next.  This is called after the "active player" has moved.
def updateActivePlayer():
    global playerTurn;
    if playerTurn is True:
        playerTurn = False;
    else:
        playerTurn = True;
    
def playerSpaceAdded(playerList, space):
    if(checkSpace(space)):
        addSpace(playerList, space);
        return True;
    else:
        return False;

def addSpace(playerList, space):
    if(checkSpace(space)):
        playerList.append(space);

##CHECK IF SPACE IS VALID!
def checkSpace(space):
    if(space in playerX or space in playerO):
        return False;
    else:
        return True;
    
##At most, a player can occupy 5 spaces.
##Must have three in a row for victory condition.
def checkVictory(playerList):
    if(len(playerList) >=3):
        if(checkHorizontalVictory(playerList) or checkVerticalVictory(playerList) or checkDiagonalVictory(playerList)):
            return True;
        else:
            return False;
    else:
        return False;
#Horizontal = [1,2,3], [4,5,6], [7,8,9]
def checkHorizontalVictory(playerList):
    if((1 in playerList and 2 in playerList and 3 in playerList)
       or
       (4 in playerList and 5 in playerList and 6 in playerList)
       or
       (7 in playerList and 8 in playerList and 9 in playerList)):
        print("Horizontal Victory");
        return True;
    else:
        return False;

#Vertical = [1,4,7], [2,5,8], [3,6,9]
def checkVerticalVictory(playerList):
    if((1 in playerList and 4 in playerList and 7 in playerList)
       or
       (2 in playerList and 5 in playerList and 8 in playerList)
       or
       (3 in playerList and 6 in playerList and 9 in playerList)):
        print("Vertical Victory");
        return True;
    else:
        return False;
        
#Diagonal = [1,5,9], [3,5,7]
def checkDiagonalVictory(playerList):
    if((1 in playerList and 5 in playerList and 9 in playerList)
       or
       (3 in playerList and 5 in playerList and 7 in playerList)):
        print("Diagonal Victory");
        return True;
    else:
        return False;

#Cat's Game is all spaces are taken and there is no clear victor.
def checkCatsGame():
    if(len(playerX) + len(playerO) >=9):
        print("Cat's Game.");
        return True;
    return False;
