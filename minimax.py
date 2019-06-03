import validations as v
import copy
import random as r
import math as m

# maxVal = 100
# minVal = -100

weights = [
    120, -20,  20,   5,   5,  20, -20, 120,
    -20, -40,  -5,  -5,  -5,  -5, -40, -20, 
     20,  -5,  15,   3,   3,  15,  -5,  20, 
      5,  -5,   3,   3,   3,   3,  -5,   5, 
      5,  -5,   3,   3,   3,   3,  -5,   5,
     20,  -5,  15,   3,   3,  15,  -5,  20,
    -20, -40,  -5,  -5,  -5,  -5, -40, -20,
    120, -20,  20,   5,   5,  20, -20, 120
]


s = -10000

def getMoveScore(board, move, player):
    opp = 2
    if player == 2:
        opp = 1
    newBoard = v.applyMove (board, move, player)
    myScore = v.getScore(newBoard, player)
    oppScore = v.getScore(newBoard, opp)

    return [newBoard, move, myScore, oppScore]

def getMin(board, move, player):
    opp = 2
    if player == 2:
        opp = 1

    applied = getMoveScore(copy.deepcopy(board), move, player)
    newBoard = applied[0]
    
    oppMoves = v.getMoves(newBoard, opp)

    minScore = 100
    finalBoard = []
    for m in oppMoves:
        oppApl = getMoveScore(copy.deepcopy(newBoard), m[0], opp)
        #minScore = min(minScore, oppApl[3])
        if oppApl[3] < minScore:
            minScore = oppApl[3]
            finalBoard = oppApl[0]

    return [move, minScore, finalBoard]

def Minimax(board, player, moves, depth):
    movement = " "
    for m in moves:
        currMove = getMin(board, m[0], player)
        if currMove[1] * weights[currMove[0]]> s:
            movement = currMove[0]
    print(v.indexToHuman(movement))
    return movement

# def Minimax(player, board, depth, isMax):
    # opp = 2
    # if player == 2:
        # opp = 1

    # viable = v.getMoves(board, player)
    # if viable:
        # randMove = r.choice(viable)
        # bestMove = randMove[0]
    # else:
        # bestMove = " "
    
    
 
    # if isMax:
        # bestValue = minVal
        # moves = v.getMoves(board, player)
        # for m in moves:
            # applied = getMoveScore(copy.deepcopy(board), m[0], player)
            # val = Minimax(opp, applied[1], depth - 1, False)
            # if val[0] > bestValue:
                # bestValue = val[0]
                # bestMove = m[0]
    # else:
        # bestValue = maxVal
        # moves = v.getMoves(board, player)
        # for m in moves:
            # applied = getMoveScore(copy.deepcopy(board), m[0], player)
            # val = Minimax(opp, applied[1], depth - 1, True)
            # if val[0] < bestValue:
                # bestValue = val[0]
                # bestMove = m[0]
    # return [bestValue, bestMove]