numberMapping = {
    0: "0️⃣",
    1: "1️⃣",
    2: "2️⃣",
    3: "3️⃣",
    4: "4️⃣",
    5: "5️⃣",
    6: "6️⃣",
    7: "7️⃣",
    8: "8️⃣",
    9: "9️⃣",
    "X": "💣",
    "O": "◼"
}

2
4
total = 2
4 - 2 = 2

print(numberMapping)

def printBoard(board):
    for outerElement in board:
        for innerElement in outerElement:
            print(innerElement, end=" ")

def takeCoordinateInput() -> list[int]:
    inp = input("Where is the bomb: ")
    coordinatesRaw = inp.split(",")
    coordinates = list(map(int, coordinatesRaw))
    return coordinates

def createBombBoard(size):
    bombBoard = []
    for i in range(size):
        for j in range(size):
            bombBoard.append("💣")


def scanBombs(bombBoard,coordinate):
    x,y = coordinate
    bombsFound = 0
    startXFrom = max(x-1, 0)
    startXTo = min(x+1, len(bombBoard) - 1)
    for i in range(startXFrom, startXTo):
        startYFrom = max(y-1, 0)
        startYTo = min(y+1, len(bombBoard) - 1)
        for j in range(startYFrom, startYTo):
            if (bombBoard[i][j] == "o"):
                bombsFound += 1
            print(i)
    return bombsFound

# arr = takeCoordinateInput()
# arr = [10,10,5]
x, y = takeCoordinateInput()

print(x, y)

# xCoordinate = res[0]
# yCoordinate = res[1]

# array[1][2]
# print(array[xCoordinate][yCoordinate]) #

# # user input = [1,2,_]
# []
