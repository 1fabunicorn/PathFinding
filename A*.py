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

print(maze)
print(_([5,4]))

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
# for x in range(20):
#     xCurrent, yCurrent = start[0], start[1]
#
#     if _(move('right', xCurrent, yCurrent)) is 'path':
#         xCurrent, yCurrent = move('right', xCurrent, yCurrent)[0], move('right', xCurrent, yCurrent)[1]
#         print("x: " + str(xCurrent) + " y: " + str(yCurrent))
#
#     if _(move('left', xCurrent, yCurrent)) is 'path':
#         xCurrent, yCurrent = move('left', xCurrent, yCurrent)[0], move('left', xCurrent, yCurrent)[1]
#         print("x: " + str(xCurrent) + " y: " + str(yCurrent))
#
#     if _(move('up', xCurrent, yCurrent)) is 'path':
#         xCurrent, yCurrent = move('up', xCurrent, yCurrent)[0], move('up', xCurrent, yCurrent)[1]
#         print("x: " + str(xCurrent) + " y: " + str(yCurrent))
#
#     if _(move('down', xCurrent, yCurrent)) is 'path':
#         xCurrent, yCurrent = move('up', xCurrent, yCurrent)[0], move('up', xCurrent, yCurrent)[1]
#         print("x: " + str(xCurrent) + " y: " + str(yCurrent))
#
#     if maze[xCurrent][yCurrent] is 'end':
#         print("end!!!")
xCurrent, yCurrent = start[0], start[1]
print(_(move('up', xCurrent, yCurrent)))
