

def thirdTurn(cWF, uM,cM):
    listOfSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    winningPossibilities = [[1, 2, 3], [1, 4, 7], [2, 5, 8], [3, 6, 9], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]
    import random
    jumanji = 0
    compWentFirst = cWF
    userMoves = uM
    compMoves = cM

    if compWentFirst == True:
        print(userMoves)
        print("made it to line 482")


        if userMoves[0] == 1:
            if userMoves[1] == 2:
                jumanji = 3
            elif userMoves[1] == 3:
                jumanji = 2
            elif userMoves[1] == 4:
                jumanji = 7
            elif userMoves[1] == 6:
                jumanji = 7
            elif userMoves[1] == 7:
                jumanji = 4
            elif userMoves[1] == 8:
                jumanji = 3
        elif userMoves[0] == 2:
            if userMoves[1]!= 7:
                jumanji = 7
            else:
                jumanji = 9
        elif userMoves[0] == 3:
            if userMoves[1]== 1:
                jumanji = 2
            elif userMoves[1] == 2:
                jumanji = 1
            elif userMoves[1] == 4:
                jumanji = 9
            elif userMoves[1] == 6:
                jumanji = 9
            elif userMoves[1] == 8:
                jumanji = 1
            elif userMoves[1] == 9:
                jumanji = 6
        elif userMoves[0] == 4:
            if userMoves[1]!= 9:
                jumanji = 9
            else:
                jumanji = 3
        elif userMoves[0] == 6:
            if userMoves[1]!= 7:
                jumanji = 7
            else:
                jumanji = 1
        elif userMoves[0] == 7:
            if userMoves[1]== 1:
                jumanji = 4
            elif userMoves[1] == 2:
                jumanji = 9
            elif userMoves[1] == 4:
                jumanji = 1
            elif userMoves[1] == 6:
                jumanji = 1
            elif userMoves[1] == 8:
                jumanji = 9
            elif userMoves[1] == 9:
                jumanji = 8
        elif userMoves[0] == 8:
            if userMoves[1]!= 3:
                jumanji = 3
            else:
                jumanji = 1
        elif userMoves[0] == 9:
            if userMoves[1] == 2:
                jumanji = 7
            elif userMoves[1] == 3:
                jumanji = 6
            elif userMoves[1] == 4:
                jumanji = 3
            elif userMoves[1] == 6:
                jumanji = 3
            elif userMoves[1] == 7:
                jumanji = 8
            elif userMoves[1] == 8:
                jumanji = 7

        compFirstTurn = jumanji

    elif compWentFirst == False:
        compFirstTurn = jumanji
        for rnd3 in winningPossibilities:
            num3 = 0
            x123 = 0
            compFirstTurn = 0

            for w3 in rnd3:
                if str(w3) in str(userMoves):
                    num3 = num3 + 1
                    if num3 == 2:
                        for w3 in rnd3:
                            if str(w3) not in str(compMoves) and str(w3) not in str(userMoves):
                                jumanji = int(w3)
                                x123 = 1
                                break
                        if x123 == 1:
                            break
        for rnd4 in winningPossibilities:
            num4 = 0
            compFirstTurn = 0
            x123 = 0
            for w5 in rnd4:
                if str(w5) in str(compMoves):
                    num4 = num4 + 1
                    if num4 == 2:
                        for w5 in rnd4:
                            if str(w5) not in str(compMoves) and str(w5) not in str(userMoves):
                                jumanji = int(w5)
                                x123 = 1
                                break
                        if x123 == 1:
                            break
        compFirstTurn = jumanji

        if compFirstTurn == 0:
            compFirstTurn = random.choice(listOfSpaces)
            print("Made it to Random Choice " + str(compFirstTurn))

        compFirstTurn = jumanji




    return compFirstTurn












