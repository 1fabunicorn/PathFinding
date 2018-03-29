from src import MazeToArray as Mta
from src import FindStart as Fs

maze = Mta.read("Mazes/maze0.tif")
startEnd = Fs.findStart(maze)
start, end = startEnd['start'], startEnd['end']


def _(array):  # Lookup
    x, y = array[0], array[1]
    try:
        return maze[x][y]
    except IndexError:
        return False


def isPath(array):
    return _(array) is "path"


def isEnd(array):
    return _(array) is "end"


def move(move, currentX, currentY):
    if move is 'right':
        return [currentX + 1, currentY]
    if move is 'left':
        return [currentX - 1, currentY]
    if move is 'up':
        return [currentX, currentY - 1]
    if move is 'down':
        return [currentX, currentY + 1]


print("start is " + str(start))
xCurrent, yCurrent = start[0], start[1]

for x in range(3):

    if _(move('right', xCurrent, yCurrent)) is 'path':
        xOldCurrent, yOldCurrent = xCurrent, yCurrent
        xCurrent, yCurrent = move('right', xOldCurrent, yOldCurrent)[0], move('right', xOldCurrent, yOldCurrent)[1]
        print("xOldCurrent: " + str(xOldCurrent) + " yOldCurrent: " + str(yOldCurrent))
        print("xCurrent: " + str(xCurrent) + " yCurrent: " + str(yCurrent) + "\n")

    elif _(move('left', xCurrent, yCurrent)) is 'path':
        xOldCurrent, yOldCurrent = xCurrent, yCurrent
        xCurrent, yCurrent = move('left', xOldCurrent, yOldCurrent)[0], move('left', xOldCurrent, yOldCurrent)[1]
        print("xOldCurrent: " + str(xOldCurrent) + " yOldCurrent: " + str(yOldCurrent))
        print("xCurrent: " + str(xCurrent) + " yCurrent: " + str(yCurrent) + "\n")

    elif _(move('up', xCurrent, yCurrent)) is 'path':
        xOldCurrent, yOldCurrent = xCurrent, yCurrent
        xCurrent, yCurrent = move('up', xOldCurrent, yOldCurrent)[0], move('up', xOldCurrent, yOldCurrent)[1]
        print("xOldCurrent: " + str(xOldCurrent) + " yOldCurrent: " + str(yOldCurrent))
        print("xCurrent: " + str(xCurrent) + " yCurrent: " + str(yCurrent) + "\n")

    elif _(move('down', xCurrent, yCurrent)) is 'path':
        xOldCurrent, yOldCurrent = xCurrent, yCurrent
        xCurrent, yCurrent = move('down', xOldCurrent, yOldCurrent)[0], move('down', xOldCurrent, yOldCurrent)[1]
        print("xOldCurrent: " + str(xOldCurrent) + " yOldCurrent: " + str(yOldCurrent))
        print("xCurrent: " + str(xCurrent) + " yCurrent: " + str(yCurrent) + "\n")

    elif maze[xCurrent][yCurrent] is 'end':
        print("end!!!")
