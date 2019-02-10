from turtle import *
import random
import time
import os
global turnCount
turnCount = 1
global spot
num = 0
num2 = 0

veryFirstTurn = True
gameOn = True
spot = 0
past = True
compClose = False
oneTurn = True
userMoves = []
userClose = False
compMoves = []
usersTurn = False
userIsX = False
userIsO = False
xOrO = random.randint(1,2)
firstTurn = random.randint(1,2)
winningPossibilities = [[1,2,3],[1,4,7],[2,5,8],[3,6,9],[4,5,6],[7,8,9],[1,5,9],[3,5,7]]
listOfSpaces = [1,2,3,4,5,6,7,8,9]

def compDrawAlgorithmX(x1,y1,x2,y2):
    global spot
    if spot in listOfSpaces:
        bdrawer = Turtle()
        bdrawer.turtlesize(0.001)
        bdrawer.hideturtle()
        bdrawer.pensize(3)
        bdrawer.speed(0)
        bdrawer.penup()
        bdrawer.goto(x1 + 10, y2 + 10)
        bdrawer.pendown()
        bdrawer.goto(x2 - 10, y1 - 10)
        bdrawer.penup()
        bdrawer.goto(x1 + 10, y1 -10)
        bdrawer.pendown()
        bdrawer.goto(x2 - 10, y2 + 10)
        compMoves.append(spot)


def compDrawAlgorithmO(x1,y1,x2,y2):
    global spot
    if spot in listOfSpaces:
        bdrawer = Turtle()
        bdrawer.turtlesize(0.001)
        bdrawer.hideturtle()
        bdrawer.pensize(3)
        bdrawer.speed(0)
        bdrawer.penup()
        xMiddle = x1 + ((x2-x1) / 2)
        yMiddle = (y1 + ((y2-y1) / 2) + 40)
        bdrawer.goto(xMiddle, yMiddle)
        bdrawer.pendown()
        bdrawer.right(180)
        bdrawer.circle(50)
        compMoves.append(spot)


def userDrawX(x,y):
    global spot

    global oneTurn
    if x > -270 and x < -120 and y > 100 and y < 250: #spot 1
        spot = 1
        if spot in listOfSpaces:
            x1 = -270
            y1 = 250
            x2 = -120
            y2 = 100
        else:
            print("Could not put spot in " + str(spot))
            oneTurn = True
            spot = 0
    elif x > -120 and x < 120 and y > 100 and y < 250: #spot 2
        spot = 2
        if spot in listOfSpaces:
            x1 = -120
            y1 = 250
            x2 = 120
            y2 = 100
        else:
            oneTurn = True
            spot = 0
    elif x > 120 and x < 270 and y > 100 and y < 250: #spot 3
        spot = 3
        if spot in listOfSpaces:
            x1 = 120
            y1 = 250
            x2 = 270
            y2 = 100
        else:
            print("couldnt put in spot " + str(spot))
            oneTurn = True
            spot = 0
    elif x > -270 and x < -120 and y > -100 and y < 100: #spot 4
        spot = 4
        if spot in listOfSpaces:
            x1 = -270
            y1 = 100
            x2 = -120
            y2 = -100
        else:
            print("couldnt put in spot " + str(spot))
            oneTurn = True
            spot = 0
    elif x > -120 and x < 120 and y > -100 and y < 100: #spot 5
        spot = 5
        if spot in listOfSpaces:
            x1 = -120
            y1 = 100
            x2 = 120
            y2 = -100
        else:
            print("couldnt put in spot " + str(spot))
            oneTurn = True
            spot = 0
    elif x > 120 and x < 270 and y > -100 and y < 100: #spot 6
        spot = 6
        if spot in listOfSpaces:
            x1 = 120
            y1 = 100
            x2 = 270
            y2 = -100
        else:
            print("couldnt put in spot " + str(spot))
            oneTurn = True
            spot = 0
    elif x > -270 and x < -120 and y > -250 and y < -100: #spot 7
        spot = 7
        if spot in listOfSpaces:
            x1 = -270
            y1 = -100
            x2 = -120
            y2 = -250
        else:
            print("couldnt put in spot " + str(spot))
            oneTurn = True
            spot = 0
    elif x > -120 and x < 120 and y > -250 and y < -100: #spot 8
        spot = 8
        if spot in listOfSpaces:
            x1 = -120
            y1 = -100
            x2 = 120
            y2 = -250
        else:
            print("couldnt put in spot " + str(spot))
            oneTurn = True
            spot = 0
    elif x > 120 and x < 270 and y > -250 and y < -100: #spot 9
        spot = 9
        if spot in listOfSpaces:
            x1 = 120
            y1 = -100
            x2 = 270
            y2 = -250
        else:
            print("couldnt put in spot " + str(spot))
            oneTurn = True
            spot = 0


    if spot in listOfSpaces:
        bdrawer = Turtle()
        bdrawer.turtlesize(0.001)
        bdrawer.hideturtle()
        bdrawer.pensize(3)
        bdrawer.speed(0)
        bdrawer.penup()
        bdrawer.goto(x1 + 10, y2 + 10)
        bdrawer.pendown()
        bdrawer.goto(x2 - 10, y1 - 10)
        bdrawer.penup()
        bdrawer.goto(x1 + 10, y1 - 10)
        bdrawer.pendown()
        bdrawer.goto(x2 - 10, y2 + 10)
        oneTurn = False
        userMoves.append(spot)


def userDrawO(x,y):
    global spot

    global oneTurn
    if x > -270 and x < -120 and y > 100 and y < 250: #spot 1
        spot = 1
        if spot in listOfSpaces:
            x1 = -270
            y1 = 250
            x2 = -120
            y2 = 100
            print("User chose " + str(spot))
            print(listOfSpaces)
        else:
            print("couldnt put in spot " + str(spot))
            oneTurn = True
            spot = 0
    elif x > -120 and x < 120 and y > 100 and y < 250: #spot 2
        spot = 2
        if spot in listOfSpaces:
            x1 = -120
            y1 = 250
            x2 = 120
            y2 = 100
            print("User chose " + str(spot))
            print(listOfSpaces)
        else:
            print("couldnt put in spot " + str(spot))
            oneTurn = True
            spot = 0
    elif x > 120 and x < 270 and y > 100 and y < 250: #spot 3
        spot = 3
        if spot in listOfSpaces:
            x1 = 120
            y1 = 250
            x2 = 270
            y2 = 100
            print("User chose " + str(spot))
            print(listOfSpaces)
        else:
            print("couldnt put in spot " + str(spot))
            oneTurn = True
            spot = 0
    elif x > -270 and x < -120 and y > -100 and y < 100: #spot 4
        spot = 4
        if spot in listOfSpaces:
            x1 = -270
            y1 = 100
            x2 = -120
            y2 = -100
            print("User chose " + str(spot))
            print(listOfSpaces)
        else:
            print("couldnt put in spot " + str(spot))
            oneTurn = True
            spot = 0
    elif x > -120 and x < 120 and y > -100 and y < 100: #spot 5
        spot = 5
        if spot in listOfSpaces:
            x1 = -120
            y1 = 100
            x2 = 120
            y2 = -100
            print("User chose " + str(spot))
            print(listOfSpaces)
        else:
            print("couldnt put in spot " + str(spot))
            oneTurn = True
            spot = 0
    elif x > 120 and x < 270 and y > -100 and y < 100: #spot 6
        spot = 6
        if spot in listOfSpaces:
            x1 = 120
            y1 = 100
            x2 = 270
            y2 = -100
            print("User chose " + str(spot))
            print(listOfSpaces)
        else:
            print("couldnt put in spot " + str(spot))
            oneTurn = True
            spot = 0
    elif x > -270 and x < -120 and y > -250 and y < -100: #spot 7
        spot = 7
        if spot in listOfSpaces:
            x1 = -270
            y1 = -100
            x2 = -120
            y2 = -250
            print("User chose " + str(spot))
            print(listOfSpaces)
        else:
            print("couldnt put in spot " + str(spot))
            oneTurn = True
            spot = 0
    elif x > -120 and x < 120 and y > -250 and y < -100: #spot 8
        spot = 8
        if spot in listOfSpaces:
            x1 = -120
            y1 = -100
            x2 = 120
            y2 = -250
            print("User chose " + str(spot))
            print(listOfSpaces)
        else:
            print("couldnt put in spot " + str(spot))
            oneTurn = True
            spot = 0
    elif x > 120 and x < 270 and y > -250 and y < -100: #spot 9
        spot = 9
        if spot in listOfSpaces:
            x1 = 120
            y1 = -100
            x2 = 270
            y2 = -250
            print("User chose " + str(spot))
            print(listOfSpaces)
        else:
            print("couldnt put in spot " + str(spot))
            oneTurn = True
            spot = 0


    if spot in listOfSpaces:
        bdrawer = Turtle()
        bdrawer.turtlesize(0.001)
        bdrawer.hideturtle()
        bdrawer.pensize(3)
        bdrawer.speed(0)
        bdrawer.penup()
        xMiddle = x1 + ((x2 - x1) / 2)
        yMiddle = (y1 + ((y2 - y1) / 2) + 40)
        bdrawer.goto(xMiddle, yMiddle)
        bdrawer.pendown()
        bdrawer.right(180)
        bdrawer.circle(50)
        oneTurn = False
        userMoves.append(spot)


def drawBoard():
    bdrawer = Turtle()
    bdrawer.hideturtle()
    bdrawer.turtlesize(0.001)
    bdrawer.speed(0)

    bdrawer.penup()
    bdrawer.goto(-120,250)
    bdrawer.pendown()
    bdrawer.right(90)
    bdrawer.forward(500)

    bdrawer.penup()
    bdrawer.goto(120, 250)
    bdrawer.pendown()
    bdrawer.forward(500)

    bdrawer.penup()
    bdrawer.goto(270, 100)
    bdrawer.pendown()
    bdrawer.right(90)
    bdrawer.forward(540)

    bdrawer.penup()
    bdrawer.goto(270, -100)
    bdrawer.pendown()
    bdrawer.forward(540)
    bdrawer.penup()


    if xOrO == 1:
        global userIsX
        userIsX = True
        bdrawer.goto(300,300)
        bdrawer.write("You are an X", font=("Arial", 20, "normal"), align="center")
    elif xOrO == 2:
        global userIsO
        userIsO = True
        bdrawer.goto(300, 300)
        bdrawer.write("You are an O", font=("Arial", 20, "normal"), align="center")

def drawWhosTurn():
    bdrawer = Turtle()
    bdrawer.hideturtle()
    bdrawer.turtlesize(0.001)
    bdrawer.speed(0)
    bdrawer.penup()
    if firstTurn == 1:
        bdrawer.goto(-300, 300)
        bdrawer.write("Your Turn", font=("Arial", 20, "normal"), align="center")
    elif firstTurn == 2:
        bdrawer.goto(-300, 300)
        bdrawer.write("Computer Turn", font=("Arial", 20, "normal"), align="center")

screen = Screen()
screen.screensize(700,700)
screen.title("Tic Tac Toe")
screen.delay(0)


drawBoard()

drawWhosTurn()



mode = "insane"


def main():
    global spot
    global veryFirstTurn
    global userClose, compClose
    global turnCount
    global compWentFirst
    global compFirstTurn
    compFirstTurn = 0
    bdrawer = Turtle()
    bdrawer.hideturtle()
    bdrawer.turtlesize(0.001)
    bdrawer.penup()
    bdrawer.speed(0)

    bdrawer.pensize(3)


    def on_screen_click(x, y):
        global veryFirstTurn
        global oneTurn

        if firstTurn == 1:
            veryFirstTurn = False

            while(oneTurn):
                if userIsX:


                    userDrawX(x,y)
                    if spot not in listOfSpaces:
                        break
                        print("error: line 449")


                elif userIsO:
                    userDrawO(x, y)
                    if spot not in listOfSpaces:
                        break
                        print("error: line 456")

    if firstTurn == 2:
        time.sleep(1)

        if mode == "insane":
            print(turnCount)

            if turnCount == 1:
                if userMoves == []:
                    compWentFirst = True
                else:
                    compWentFirst = False

            jumanji = 0



            if turnCount == 1:
                if compWentFirst == True:

                    jumanji = 5
                    print("going in space 5")
                    compFirstTurn = jumanji

                else:

                    print("user went first")
                    if userMoves[0] != 5:
                        print("going in space 5")
                        jumanji = 5
                        compFirstTurn = jumanji

                    else:

                        jumanji = 7
                        compFirstTurn = jumanji













            elif turnCount == 2:
                if compWentFirst == True:
                    print(userMoves)
                    print("made it to line 482")
                    if userMoves[0] == 1:
                        jumanji = 9

                    elif userMoves[0] == 2:
                        jumanji = 3

                    elif userMoves[0] == 3:
                        jumanji = 7

                    elif userMoves[0] == 4:
                        jumanji = 1

                    elif userMoves[0] == 6:
                        jumanji = 3

                    elif userMoves[0] == 7:
                        jumanji = 3

                    elif userMoves[0] == 8:
                        jumanji = 7

                    elif userMoves[0] == 9:
                        jumanji = 1

                    compFirstTurn = jumanji

                elif compWentFirst == False:

                    '''
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

                    compFirstTurn = jumanji
                    if compFirstTurn == 0:
                        compFirstTurn = random.choice(listOfSpaces)
                    '''
                    import TicTacToeUserFirst
                    compFirstTurn = TicTacToeUserFirst.turnTwoNeverLose(compWentFirst, userMoves, compMoves)






            elif turnCount == 3:



                import TicTacToeTurn3
                compFirstTurn = TicTacToeTurn3.thirdTurn(compWentFirst,userMoves,compMoves)


            elif turnCount > 3:

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










            turnCount = turnCount + 1










        if userIsX:
            if compFirstTurn == 1:
                spot = 1
                compDrawAlgorithmO(-270, 250, -120, 100)
            elif compFirstTurn == 2:
                spot = 2
                compDrawAlgorithmO(-120,250,120,100)
            elif compFirstTurn == 3:
                spot = 3
                compDrawAlgorithmO(120, 250, 270, 100)
            elif compFirstTurn == 4:
                spot = 4
                compDrawAlgorithmO(-270,100,-120,-100)
            elif compFirstTurn == 5:
                spot = 5
                compDrawAlgorithmO(-120,100,120,-100)
            elif compFirstTurn == 6:
                spot = 6
                compDrawAlgorithmO(120,100,270,-100)
            elif compFirstTurn == 7:
                spot = 7
                compDrawAlgorithmO(-270,-100,-120,-250)
            elif compFirstTurn == 8:
                spot = 8
                compDrawAlgorithmO(-120,-100,120,-250)
            elif compFirstTurn == 9:
                spot = 9
                compDrawAlgorithmO(120, -100, 270, -250)
        elif userIsO:
            if compFirstTurn == 1:
                spot = 1
                compDrawAlgorithmX(-270, 250, -120, 100)
            elif compFirstTurn == 2:
                spot = 2
                compDrawAlgorithmX(-120,250,120,100)
            elif compFirstTurn == 3:
                spot = 3
                compDrawAlgorithmX(120, 250, 270, 100)
            elif compFirstTurn == 4:
                spot = 4
                compDrawAlgorithmX(-270,100,-120,-100)
            elif compFirstTurn == 5:
                spot = 5
                compDrawAlgorithmX(-120,100,120,-100)
            elif compFirstTurn == 6:
                spot = 6
                compDrawAlgorithmX(120,100,270,-100)
            elif compFirstTurn == 7:
                spot = 7
                compDrawAlgorithmX(-270,-100,-120,-250)
            elif compFirstTurn == 8:
                spot = 8
                compDrawAlgorithmX(-120,-100,120,-250)
            elif compFirstTurn == 9:
                spot = 9
                compDrawAlgorithmX(120, -100, 270, -250)


    screen.onclick(on_screen_click)




while gameOn:
    for rnd in winningPossibilities:
        num = 0
        #winningPossibilities = [[1, 2, 3], [1, 4, 7], [2, 5, 8], [3, 6, 9], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]

        for w in rnd:
            if str(w) in str(userMoves):
                 num = num + 1
            if num == 3:
                bdrawer = Turtle()
                bdrawer.hideturtle()
                bdrawer.turtlesize(0.001)
                bdrawer.speed(0)
                bdrawer.pencolor("blue")
                bdrawer.penup()
                bdrawer.pensize(4)

                if rnd == [1, 2, 3]:
                    time.sleep(0.5)
                    bdrawer.goto(-240, 175)
                    bdrawer.pendown()
                    bdrawer.forward(480)
                elif rnd == [1, 4, 7]:
                    time.sleep(0.5)
                    bdrawer.goto(-200, 235)
                    bdrawer.right(90)
                    bdrawer.pendown()
                    bdrawer.forward(480)
                elif rnd == [2, 5, 8]:
                    time.sleep(0.5)
                    bdrawer.goto(0, 235)
                    bdrawer.right(90)
                    bdrawer.pendown()
                    bdrawer.forward(480)
                elif rnd == [3, 6, 9]:
                    time.sleep(0.5)
                    bdrawer.goto(195, 235)
                    bdrawer.right(90)
                    bdrawer.pendown()
                    bdrawer.forward(480)
                elif rnd == [4, 5, 6]:
                    time.sleep(0.5)
                    bdrawer.goto(-240, 10)
                    bdrawer.pendown()
                    bdrawer.forward(480)
                elif rnd == [7, 8, 9]:
                    time.sleep(0.5)
                    bdrawer.goto(-240, -175)
                    bdrawer.pendown()
                    bdrawer.forward(480)
                elif rnd == [1, 5, 9]:
                    time.sleep(0.5)
                    bdrawer.goto(-195, 175)
                    bdrawer.pendown()
                    bdrawer.right(43)
                    bdrawer.forward(550)
                elif rnd == [3, 5, 7]:
                    time.sleep(0.5)
                    bdrawer.goto(195, 175)
                    bdrawer.pendown()
                    bdrawer.left(223)
                    bdrawer.forward(550)
                time.sleep(2)
                screen.clear()



                bdrawer.goto(0, 0)
                bdrawer.write("You Win!", font=("Arial", 36, "normal"),
                                   align="center")
                time.sleep(2)
                quit()


    for rnd2 in winningPossibilities:
        num2 = 0

        for w2 in rnd2:
            if str(w2) in str(compMoves):
                num2 = num2 + 1
            if num2 == 3:

                bdrawer = Turtle()
                bdrawer.hideturtle()
                bdrawer.turtlesize(0.001)
                bdrawer.pensize(4)
                bdrawer.pencolor("red")
                bdrawer.speed(0)

                bdrawer.penup()
                bdrawer.goto(0, 0)



                if rnd2 == [1, 2, 3]:
                    time.sleep(0.5)
                    bdrawer.goto(-240, 175)
                    bdrawer.pendown()
                    bdrawer.forward(480)
                elif rnd2 == [1, 4, 7]:
                    time.sleep(0.5)
                    bdrawer.goto(-200, 235)
                    bdrawer.right(90)
                    bdrawer.pendown()
                    bdrawer.forward(480)
                elif rnd2 == [2, 5, 8]:
                    time.sleep(0.5)
                    bdrawer.goto(0, 235)
                    bdrawer.right(90)
                    bdrawer.pendown()
                    bdrawer.forward(480)
                elif rnd2 == [3, 6, 9]:
                    time.sleep(0.5)
                    bdrawer.goto(195, 235)
                    bdrawer.right(90)
                    bdrawer.pendown()
                    bdrawer.forward(480)
                elif rnd2 == [4, 5, 6]:
                    time.sleep(0.5)
                    bdrawer.goto(-240, 10)
                    bdrawer.pendown()
                    bdrawer.forward(480)
                elif rnd2 == [7, 8, 9]:
                    time.sleep(0.5)
                    bdrawer.goto(-240, -175)
                    bdrawer.pendown()
                    bdrawer.forward(480)
                elif rnd2 == [1, 5, 9]:
                    time.sleep(0.5)
                    bdrawer.goto(-195, 175)
                    bdrawer.pendown()
                    bdrawer.right(43)
                    bdrawer.forward(550)
                elif rnd2 == [3, 5, 7]:
                    time.sleep(0.5)
                    bdrawer.goto(195, 175)
                    bdrawer.pendown()
                    bdrawer.left(223)
                    bdrawer.forward(550)

                time.sleep(2)
                screen.clear()
                bdrawer.goto(0, 0)
                bdrawer.write("Computer Won!", font=("Arial", 36, "normal"),
                              align="center")
                time.sleep(2)
                quit()



    if listOfSpaces == []:
        time.sleep(0.5)
        screen.clear()
        bdrawer = Turtle()
        bdrawer.hideturtle()
        bdrawer.speed(0)

        bdrawer.penup()
        bdrawer.goto(0, 0)
        bdrawer.write("It was a draw!", font=("Arial", 36, "normal"),
                      align="center")
        time.sleep(1)
        quit()


    main()
    try:
        listOfSpaces.remove(spot)

    except:
        pass
    if firstTurn == 1:
        if oneTurn == False:
            firstTurn = firstTurn + 1

    else:
        firstTurn = 1
        oneTurn = True






screen.mainloop()

