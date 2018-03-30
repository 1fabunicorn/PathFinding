from src import ArrayToMaze
from src import MazeToArray as Mta
from src import FindStart as Fs

maze = Mta.read("Mazes/maze0.tif")
startEnd = Fs.findStart(maze)
start, end = startEnd['start'], startEnd['end']


def search(x, y):
    if maze[x][y] == 'end':
        print 'found at %d,%d' % (x, y)
        return True
    elif maze[x][y] == 'wall':
        print 'wall at %d,%d' % (x, y)
        return False
    elif maze[x][y] == 'visited':
        print 'visited at %d,%d' % (x, y)
        return False

    print 'visited %d,%d' % (x, y)

    # mark as visited
    maze[x][y] = 'visited'

    # explore neighbors clockwise starting by the one on the right
    if ((x < len(maze)-1 and search(x+1, y))
        or (y > 0 and search(x, y-1))
        or (x > 0 and search(x-1, y))
        or (y < len(maze)-1 and search(x, y+1))):
        return True

    return False


search(start[0], start[1])
