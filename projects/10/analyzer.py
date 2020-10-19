import sys
import os

from parser import *


def analyze():
    if len(sys.argv) == 1:
        raise IOError("Expected an argument for passing the file path!!!")

    file_path = sys.argv[1]

    if os.path.isdir(file_path):
        f = os.listdir(file_path)
        files = []
        for file in f:
            if '.jack' in file:
                files.append(os.path.join(file_path, file))
    else:
        files = [file_path]

    for f in files:
        p = Parser(f)
        p.write()


if __name__ == '__main__':
    analyze()