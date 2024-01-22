LINES = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}

white = "white"
black = "black"

def makeMove(currPos, move, color):
    posAfterMove = currPos.copy()
    # Move
    target = move[-2:]
    line = target[0]
    rank = 8 - int(target[1])
    print(target)
    piece = move.replace(target, "")
    print(piece)
        # Pawn move
    if piece == "":
        piece = (color == white) * "P" + (color == black) * "p"
        print(piece) 
    else:
        if color == white:
            piece = piece.upper()
        else:
            piece = piece.lower()   
    posAfterMove[rank] = currPos[rank][:LINES[line]] + piece + currPos[rank][LINES[line] + 1:]
    # Promotion
    return convertToFEN(posAfterMove)

def isValidMove(move):

    return True

def displayPosition(positionFEN):
    currPos = positionFEN.split(" ")[0]
    posArray = []
    for rank in currPos.split("/"):
        toPrint = ""
        for char in rank:
            if char.isnumeric():
                toPrint += "." * int(char)
            else:
                toPrint += char
        posArray.append(toPrint)
        print(toPrint)
    return posArray

def convertToFEN(currPos):
    fenPos = ""
    i = 0
    while i < len(currPos):
        j = 0
        while j < len(currPos[i]):
            if currPos[i][j] == ".":
                c = 1
                while j + c < len(currPos[i]) and currPos[i][j + c] == ".":
                    c += 1
                j += c - 1
                fenPos += str(c)
            else:
                fenPos += currPos[i][j]
            j += 1
        fenPos += "/"
        i += 1
    print(fenPos)
    return fenPos


startingPos = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
currentPosition = displayPosition(startingPos)

moves = []

isEnd = False
while isEnd == False:
    if len(moves) % 2 == 0:
        color = white
    else:
        color = black
    print(color)
    currMove = input(f"{color} to play: ")
    while not isValidMove(currMove):
        print(f"{currMove} is invalid.")
        currMove = input("Please input valid move: ")
    moves.append(currMove)
    currentPosition = makeMove(currentPosition, currMove, color)
    currentPosition = displayPosition(currentPosition)