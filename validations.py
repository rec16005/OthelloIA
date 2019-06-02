import math as m

def indexToHuman(index):
    div = index / 8
    frac, whole = m.modf(div)
    row = str(whole + 1)
    col = str((frac/0.125))
    return row[0] + 'ABCDEFGH'[int(col[0])]

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
        if nextPos == pID:
            flanks.append(a[0])
        elif nextPos == oID:
            pos = getNextPos(board, a[0], a[1])
            flag = "opp"
            while flag == "opp":
                if checkNextPos(board, pos, a[1]) == pID:
                    flanks.append(a[0])
                    flag = "end"
                elif checkNextPos(board, pos, a[1]) == oID:
                    pos = getNextPos(board, pos, a[1])
                else:
                    flag = "end"
    return flanks