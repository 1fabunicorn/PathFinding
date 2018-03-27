# def findAndReplace(list, find, replace):
#     return [w.replace(find, replace) for w in list]
#
#
# print(findAndReplace(["bob", "fred"], "bob", "fred"))
maze = [['path', 'path', 'path', 'path', 'path', 'path', 'path'],
        ['end', 'wall', 'path', 'wall', 'wall', 'wall', 'path'],
        ['path', 'wall', 'path', 'wall', 'path', 'wall', 'path'],
        ['path', 'wall', 'path', 'wall', 'path', 'wall', 'path'],
        ['path', 'wall', 'path', 'wall', 'path', 'wall', 'path'],
        ['path', 'wall', 'wall', 'wall', 'path', 'wall', 'start'],
        ['path', 'path', 'path', 'path', 'path', 'path', 'path']]


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


def right(position, option=None):
    try:
        if len(maze[0]) < position[0] + 1:
            print("over")
            return False
        if option is 'maze':
            return maze[position[0] + 1][position[1]]
        else:
            return [position[0] + 1, position[1]]

    except IndexError:
        return False


current = [1, 2]
print(right(current, 'maze'))
print(right(current))
