from src import MazeToArray as Mta
from src import FindStart as Fs


def _(mazeArr):  # lookup
    return maze[mazeArr[0]][mazeArr[1]]


def isPath(mazeArr):
    return _(mazeArr) is 'path'


def isEnd(mazeArr):
    return _(mazeArr) is 'end'


# TODO: Make into one function?
def right(position, option=None):
    try:
        if len(maze[0]) < position[0] + 1:
            print("over")
            return False
        if option is 'maze':
            return [position[0] + 1][position[1]]
        else:
            return [position[0] + 1, position[1]]

    except IndexError:
        return False


def left(position, option=None):
    try:
        if position[0] - 1 < 0:
            return False
        if option is 'maze':
            return maze[position[0] - 1][position[1]]
        else:
            return [position[0] - 1, position[1]]
    except IndexError:
        return False


def up(position, option=None):
    try:
        if position[1] - 1 < 0 or len(maze[0]) > position[1] - 1:
            return False
        if option is 'maze':
            return maze[position[0]][position[1] - 1]
        else:
            return [position[0], position[1] - 1]
    except IndexError:
        return False


def down(position, option=None):
    try:
        if position[1] + 1 < 0 or len(maze[0]) > position[1] + 1:
            return False
        if option is 'maze':
            return maze[position[0]][position[1] + 1]
        else:
            return [position[0], position[1] + 1]
    except IndexError:
        return False


def solveMaze(maze):
    traveledToo = []
    reps = 0
    # right, left, up, down, = 1, -1, -1, 1
    startEnd = Fs.findStart(maze)
    start, end = startEnd["start"], startEnd["end"]
    current = start
    print(current)
    print(maze)

    while True:
        # check right
        print(current)
        if isPath(right(current, 'maze')):
            print("right")
            if right(current) not in traveledToo:
                print("going right")
                current = right(current)
                traveledToo.append(current)
        # check left
        if isPath(left(current, 'maze')):
            print("left")
            if left(current) not in traveledToo:
                print("going left")
                current = left(current)
                traveledToo.append(current)
        # check up
        if isPath(up(current, 'maze')) is 'path':
            print("up")
            if up(current) not in traveledToo:
                print("going up")
                current = up(current)
                traveledToo.append(current)
        # check down
        if isPath(down(current, 'maze')):
            print("down")
            if down(current) not in traveledToo:
                print("going down")
                current = down(current)
                traveledToo.append(current)
        if isEnd(current):
            print("end")
        reps += 1
        if reps > 20:
            return


maze = Mta.read("Mazes/maze0.tif")
print(Fs.findStart(maze))
# print(maze[2][2])
# print(isPath(right([0, 1])))
# print(right([0, 1]))

# print(Fs.findStart(maze))
# print(solveMaze(maze))
