def turnTwoNeverLose(cWF, uM, cM):
    listOfSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    winningPossibilities = [[1, 2, 3], [1, 4, 7], [2, 5, 8], [3, 6, 9], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]
    import random
    jumanji = 0
    compWentFirst = cWF
    userMoves = uM
    compMoves = cM

    if compWentFirst == False:
        print("Made it to TicTacToeUserFirst")

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
            elif userMoves[1] == 9:
                jumanji = 8
        elif userMoves[0] == 2:
            if userMoves[1] == 1:
                jumanji = 3
            elif userMoves[1] == 3:
                jumanji = 1
            elif userMoves[1] == 4:
                jumanji = 1
            elif userMoves[1] == 6:
                jumanji = 3
            elif userMoves[1] == 7:
                jumanji = 1
            elif userMoves[1] == 8:
                jumanji = 9
            elif userMoves[1] == 9:
                jumanji = 3
        elif userMoves[0] == 3:
            if userMoves[1] == 1:
                jumanji = 2
            elif userMoves[1] == 2:
                jumanji = 1
            elif userMoves[1] == 4:
                jumanji = 1
            elif userMoves[1] == 6:
                jumanji = 9
            elif userMoves[1] == 7:
                jumanji = 4
            elif userMoves[1] == 8:
                jumanji = 9
            elif userMoves[1] == 9:
                jumanji = 6
        elif userMoves[0] == 4:
            if userMoves[1] == 1:
                jumanji = 7
            elif userMoves[1] == 2:
                jumanji = 1
            elif userMoves[1] == 3:
                jumanji = 1
            elif userMoves[1] == 6:
                jumanji = 9
            elif userMoves[1] == 7:
                jumanji = 1
            elif userMoves[1] == 8:
                jumanji = 7
            elif userMoves[1] == 9:
                jumanji = 7
        elif userMoves[0] == 6:
            if userMoves[1] == 1:
                jumanji = 3
            elif userMoves[1] == 2:
                jumanji = 3
            elif userMoves[1] == 4:
                jumanji = 1
            elif userMoves[1] == 3:
                jumanji = 9
            elif userMoves[1] == 7:
                jumanji = 9
            elif userMoves[1] == 8:
                jumanji = 9
            elif userMoves[1] == 9:
                jumanji = 3
        elif userMoves[0] == 7:
            if userMoves[1]== 1:
                jumanji = 4
            elif userMoves[1] == 2:
                jumanji = 1
            elif userMoves[1] == 3:
                jumanji = 2
            elif userMoves[1] == 4:
                jumanji = 1
            elif userMoves[1] == 6:
                jumanji = 9
            elif userMoves[1] == 8:
                jumanji = 9
            elif userMoves[1] == 9:
                jumanji = 8
        elif userMoves[0] == 8:
            if userMoves[1] == 1:
                jumanji = 7
            elif userMoves[1] == 2:
                jumanji = 1
            elif userMoves[1] == 3:
                jumanji = 9
            elif userMoves[1] == 4:
                jumanji = 7
            elif userMoves[1] == 6:
                jumanji = 9
            elif userMoves[1] == 7:
                jumanji = 9
            elif userMoves[1] == 9:
                jumanji = 7
        elif userMoves[0] == 9:
            if userMoves[1] == 1:
                jumanji = 8
            elif userMoves[1] == 2:
                jumanji = 3
            elif userMoves[1] == 3:
                jumanji = 6
            elif userMoves[1] == 4:
                jumanji = 7
            elif userMoves[1] == 6:
                jumanji = 3
            elif userMoves[1] == 7:
                jumanji = 8
            elif userMoves[1] == 8:
                jumanji = 7
        elif userMoves[0] == 5:
            if userMoves[1] == 1:
                jumanji = 9
            elif userMoves[1] == 2:
                jumanji = 8
            elif userMoves[1] == 3:
                jumanji = 9
            elif userMoves[1] == 4:
                jumanji = 6
            elif userMoves[1] == 6:
                jumanji = 4
            elif userMoves[1] == 8:
                jumanji = 2
            elif userMoves[1] == 9:
                jumanji = 1


    compFirstTurn = jumanji

    return compFirstTurn