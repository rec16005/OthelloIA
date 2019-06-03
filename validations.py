import math as m
import copy

tileRep = ["_", "X", "O"]

N = 8

letters = "abcdefgh"

def indexToHuman(index):
    div = index / 8
    frac, whole = m.modf(div)
    row = str(whole + 1)
    col = str((frac/0.125))
    return row[0] + 'ABCDEFGH'[int(col[0])]

def humanBoard(board):
    result = '   A  B  C  D  E  F  G  H'
    for i in range(0, len(board)):
        if i % N == 0:
            result += '\n\n ' + str(int(m.floor(i / N) + 1)) + ' '
        
        result += " " + tileRep[board[i]] + " "

    return result

def checkNextPos(board, currentPos, dir):
    RightBorder = [7, 15, 23, 31, 39, 47, 55, 63]
    if dir.lower() == "u":
        nextPos = currentPos - 8
        if nextPos >= 0:
            return board[nextPos]
        else:
            return -1

    elif dir.lower() == "d":
        nextPos = currentPos + 8
        if nextPos <= 63:
            return board[nextPos]
        else:
            return -1

    elif dir.lower() == "r":
        nextPos = currentPos + 1
        if nextPos <= 63 and nextPos%8 != 0:
            return board[nextPos]
        else:
            return -1

    elif dir.lower() == "l":
        nextPos = currentPos - 1
        if nextPos >= 0 and nextPos not in RightBorder:
            return board[nextPos]
        else:
            return -1
    elif dir.lower() == "ur":
        nextPos = currentPos -7
        if nextPos >= 0 and nextPos%8 != 0:
            return board[nextPos]
        else:
            return -1
    elif dir.lower() == "dr":
        nextPos = currentPos + 9
        if nextPos <= 63 and nextPos%8 != 0:
            return board[nextPos]
        else:
            return -1
    elif dir.lower() == "ul":
        nextPos = currentPos - 9
        if nextPos >= 0 and nextPos not in RightBorder:
            return board[nextPos]
        else:
            return -1
    elif dir.lower() == "dl":
        nextPos = currentPos + 7
        if nextPos <= 63 and nextPos not in RightBorder:
            return board[nextPos]
        else:
            return -1

def getEmptys(board):
    emptys = []
    i = 0
    for pos in board:
        if pos == 0:
            emptys.append(i)
            i += 1
        else:
            i += 1
    return emptys

def getAdys(board, emptys, pID):
    if pID == 1:
        oID = 2
    else:
        oID = 1

    withAdy = []

    for e in emptys:
        up = checkNextPos(board, e, "u")
        down = checkNextPos(board, e, "d")
        right = checkNextPos(board, e, "r")
        left = checkNextPos(board, e, "l")
        upright = checkNextPos(board, e, "ur")
        upleft = checkNextPos(board, e, "ul")
        downright = checkNextPos(board, e, "dr")
        downleft = checkNextPos(board, e, "dl")

        if up == oID:
            withAdy.append([e, "u"])
        if down == oID:
            withAdy.append([e, "d"])
        if right == oID:
            withAdy.append([e, "r"])
        if left == oID:
            withAdy.append([e, "l"])
        if upright == oID:
            withAdy.append([e, "ur"])
        if upleft == oID:
            withAdy.append([e, "ul"])
        if downright == oID:
            withAdy.append([e, "dr"])
        if downleft == oID:
            withAdy.append([e, "dl"])

    return withAdy

def getNextPos(board, currentPos, dir):
    if checkNextPos(board, currentPos, dir) != -1:
        if dir == "u":
            return currentPos - 8
        elif dir == "d":
            return currentPos + 8
        elif dir == "r":
            return currentPos + 1
        elif dir == "l":
            return currentPos - 1
        elif dir == "ur":
            return currentPos - 7
        elif dir == "dr":
            return currentPos + 9
        elif dir == "ul":
            return currentPos - 9
        elif dir == "dl":
            return currentPos + 7
        else:
            return -1

def getFlanks(board, adys, pID):
    if pID == 1:
        oID = 2
    else:
        oID = 1

    flanks = []

    for a in adys:
        nextPos = checkNextPos(board, a[0], a[1])
        #if nextPos == pID:
        #    flanks.append(a)
        if nextPos == oID:
            pos = getNextPos(board, a[0], a[1])
            flag = "opp"
            while flag == "opp":
                if checkNextPos(board, pos, a[1]) == pID:
                    flanks.append(a)
                    flag = "end"
                elif checkNextPos(board, pos, a[1]) == oID:
                    pos = getNextPos(board, pos, a[1])
                else:
                    flag = "end"
    return flanks

def getMoves(board, pID):
    emptys = getEmptys(board)
    adys = getAdys(board, emptys, pID)
    flanks = getFlanks(board, adys, pID)

    return flanks

def getScore (board, player):
    score = 0
    for b in board:
        if b == player:
            score += 1

    return score

def getDif (board, pID):
    oID = 2
    if pID == 2:
        oID = 1

    myScore = getScore(board, pID)
    oppScore = getScore(board, oID)

    return myScore - oppScore

def applyMove (board, move, pID):
    newBoard = copy.deepcopy(board)
    
    if pID == 1:
        oID = 2
    else:
        oID = 1

    ady = []
    
    flipU = []
    flipD = []
    flipR = []
    flipL = []
    flipUR = []
    flipUL = []
    flipDR = []
    flipDL = []
    
    up = checkNextPos(board, move, "u")
    down = checkNextPos(board, move, "d")
    right = checkNextPos(board, move, "r")
    left = checkNextPos(board, move, "l")
    upright = checkNextPos(board, move, "ur")
    upleft = checkNextPos(board, move, "ul")
    downright = checkNextPos(board, move, "dr")
    downleft = checkNextPos(board, move, "dl")

    if up == oID:
        ady.append("u")
        flipU.append(getNextPos(board, move, "u"))
    if down == oID:
        ady.append("d")
        flipD.append(getNextPos(board, move, "d"))
    if right == oID:
        ady.append("r")
        flipR.append(getNextPos(board, move, "r"))
    if left == oID:
        ady.append("l")
        flipL.append(getNextPos(board, move, "l"))
    if upright == oID:
        ady.append("ur")
        flipUR.append(getNextPos(board, move, "ur"))
    if upleft == oID:
        ady.append("ul")
        flipUL.append(getNextPos(board, move, "ul"))
    if downright == oID:
        ady.append("dr")
        flipDR.append(getNextPos(board, move, "dr"))
    if downleft == oID:
        ady.append("dl")
        flipDL.append(getNextPos(board, move, "dl"))

    if flipU:
        if checkNextPos(board, flipU[0], "u") == pID:
            newBoard[move] = pID
            newBoard[flipU[0]] = pID
        elif checkNextPos(board, flipU[0], "u") == oID:
            pos = getNextPos(board, flipU[0], "u")
            flipU.append(pos)
            flag = "opp"
            while flag == "opp":
                if checkNextPos(board, pos, "u") == pID:
                    newBoard[move] = pID
                    for i in flipU:
                        newBoard[i] = pID
                    flag = "end"
                elif checkNextPos(board, pos, "u") == oID:
                    pos = getNextPos(board, pos, "u")
                    flipU.append(pos)
                else:
                    flag = "end"            

    if flipD:
        if checkNextPos(board, flipD[0], "d") == pID:
            newBoard[move] = pID
            newBoard[flipD[0]] = pID
        elif checkNextPos(board, flipD[0], "d") == oID:
            pos = getNextPos(board, flipD[0], "d")
            flipD.append(pos)
            flag = "opp"
            while flag == "opp":
                if checkNextPos(board, pos, "d") == pID:
                    newBoard[move] = pID
                    for i in flipD:
                        newBoard[i] = pID
                    flag = "end"
                elif checkNextPos(board, pos, "d") == oID:
                    pos = getNextPos(board, pos, "d")
                    flipD.append(pos)
                else:
                    flag = "end"

    if flipR:
        if checkNextPos(board, flipR[0], "r") == pID:
            newBoard[move] = pID
            newBoard[flipR[0]] = pID
        elif checkNextPos(board, flipR[0], "r") == oID:
            pos = getNextPos(board, flipR[0], "r")
            flipR.append(pos)
            flag = "opp"
            while flag == "opp":
                if checkNextPos(board, pos, "r") == pID:
                    newBoard[move] = pID
                    for i in flipR:
                        newBoard[i] = pID
                    flag = "end"
                elif checkNextPos(board, pos, "r") == oID:
                    pos = getNextPos(board, pos, "r")
                    flipR.append(pos)
                else:
                    flag = "end"  

    if flipL:
        if checkNextPos(board, flipL[0], "l") == pID:
            newBoard[move] = pID
            newBoard[flipL[0]] = pID
        elif checkNextPos(board, flipL[0], "l") == oID:
            pos = getNextPos(board, flipL[0], "l")
            flipL.append(pos)
            flag = "opp"
            while flag == "opp":
                if checkNextPos(board, pos, "l") == pID:
                    newBoard[move] = pID
                    for i in flipL:
                        newBoard[i] = pID
                    flag = "end"
                elif checkNextPos(board, pos, "l") == oID:
                    pos = getNextPos(board, pos, "l")
                    flipL.append(pos)
                else:
                    flag = "end"	

    if flipUR:
        if checkNextPos(board, flipUR[0], "ur") == pID:
            newBoard[move] = pID
            newBoard[flipUR[0]] = pID
        elif checkNextPos(board, flipUR[0], "ur") == oID:
            pos = getNextPos(board, flipUR[0], "ur")
            flipUR.append(pos)
            flag = "opp"
            while flag == "opp":
                if checkNextPos(board, pos, "ur") == pID:
                    newBoard[move] = pID
                    for i in flipUR:
                        newBoard[i] = pID
                    flag = "end"
                elif checkNextPos(board, pos, "ur") == oID:
                    pos = getNextPos(board, pos, "ur")
                    flipUR.append(pos)
                else:
                    flag = "end"

    if flipDR:
        if checkNextPos(board, flipDR[0], "dr") == pID:
            newBoard[move] = pID
            newBoard[flipDR[0]] = pID
        elif checkNextPos(board, flipDR[0], "dr") == oID:
            pos = getNextPos(board, flipDR[0], "dr")
            flipDR.append(pos)
            flag = "opp"
            while flag == "opp":
                if checkNextPos(board, pos, "dr") == pID:
                    newBoard[move] = pID
                    for i in flipDR:
                        newBoard[i] = pID
                    flag = "end"
                elif checkNextPos(board, pos, "dr") == oID:
                    pos = getNextPos(board, pos, "dr")
                    flipDR.append(pos)
                else:
                    flag = "end"

    if flipUL:
        if checkNextPos(board, flipUL[0], "ul") == pID:
            newBoard[move] = pID
            newBoard[flipUL[0]] = pID
        elif checkNextPos(board, flipUL[0], "ul") == oID:
            pos = getNextPos(board, flipUL[0], "ul")
            flipUL.append(pos)
            flag = "opp"
            while flag == "opp":
                if checkNextPos(board, pos, "ul") == pID:
                    newBoard[move] = pID
                    for i in flipUL:
                        newBoard[i] = pID
                    flag = "end"
                elif checkNextPos(board, pos, "ul") == oID:
                    pos = getNextPos(board, pos, "ul")
                    flipUL.append(pos)
                else:
                    flag = "end"	

    if flipDL:
        if checkNextPos(board, flipDL[0], "dl") == pID:
            newBoard[move] = pID
            newBoard[flipDL[0]] = pID
        elif checkNextPos(board, flipDL[0], "dl") == oID:
            pos = getNextPos(board, flipDL[0], "dl")
            flipDL.append(pos)
            flag = "opp"
            while flag == "opp":
                if checkNextPos(board, pos, "dl") == pID:
                    newBoard[move] = pID
                    for i in flipDL:
                        newBoard[i] = pID
                    flag = "end"
                elif checkNextPos(board, pos, "dl") == oID:
                    pos = getNextPos(board, pos, "dl")
                    flipDL.append(pos)
                else:
                    flag = "end"

    return newBoard