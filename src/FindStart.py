# finds the start and end of the maze
"""
Possible maze start coordinates are as follows

00, len,0, 0,len len,len
00, 60, 06, 66

  10 20 30 40 50
01              61
02              62
03              63
04              64
05              65
  16 26 36 46 56


  0 1 2 3 4 5 6
0 n p p p p p n
1 o           p
2 p           p
3 p           p
4 p           p
5 p           o
6 n p p p p p n
"""


def findStart(mazeArray):
    edges = []
    startEnd = {"start": None, "end": None}
    nullStartOrEnds = [[0, 0], [len(mazeArray), 0],
                       [0, len(mazeArray)], [len(mazeArray), len(mazeArray)]]

    for x in range(len(mazeArray)):
        for y in range(len(mazeArray[0])):
            cords = [x, y]
            if cords not in nullStartOrEnds:
                edges.append(cords)

    for i in range(len(edges)):  # TODO: Make sense of this. they are backwards
        x, y = edges[i][0], edges[i][1]
        if mazeArray[x][y] is 'start':
            startEnd["end"] = [y, x]
        if mazeArray[x][y] is 'end':
            startEnd["start"] = [y, x]

    return startEnd


# findStart([['path', 'path', 'path', 'path', 'path', 'path', 'path'], ['end', 'wall', 'path', 'wall', 'wall', 'wall', 'path'], ['path', 'wall', 'path', 'wall', 'path', 'wall', 'path'], ['path', 'wall', 'path', 'wall', 'path', 'wall', 'path'], ['path', 'wall', 'path', 'wall', 'path', 'wall', 'path'], ['path', 'wall', 'wall', 'wall', 'path', 'wall', 'start'], ['path', 'path', 'path', 'path', 'path', 'path', 'path']])
