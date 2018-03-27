"""
Nova Trauben
MazeToArray.py
Reads maze file into array to work with

from src import MazeToArray
maze = read("../Mazes/maze0.tif")
"""
import cv2


colorCodes = {"[ 66  66 244]": "start",
              "[255 255 255]": "wall",
              "[0 0 0]": "path",
              "[ 92 244  65]": "end"}


def toCode(rgbCode):
    try:
        return colorCodes[rgbCode]
    except KeyError:
        raise RuntimeError


def fileExists(file):
    try:
        open(file)
        return True
    except FileNotFoundError:
        return False


def read(file):
    # TODO: add exception if file path doesnt exist
    if fileExists(file):
        rawMazeArray = cv2.imread(file)
        x, y = len(rawMazeArray), len(rawMazeArray[0])
        mazeArray = [list([]) for _ in range(x)]

        for X in range(x):
            for Y in range(y):
                try:
                    current = str(rawMazeArray[X][Y])
                    mazeArray[X].append(toCode(current))
                except RuntimeError:
                    print("maze file does not follow color standards")
                    return
        return mazeArray
    else:
        return "maze file not found"
