#Solves [http://usaco.org/index.php?page=viewproblem2&cpid=664]

import itertools

#Safely read list of String lines from input file
with open("blocks.in", "r") as inFile:
    text = inFile.readlines()

N = int(text[0])

def getBoardSide(boardNum, case):
    return text[boardNum+1].split()[case]

result = [0]*26

#https://docs.python.org/3/library/itertools.html
combos = ["".join(c) for c in itertools.product("01", repeat=N)]

for c in range(len(combos)):
    comboChars = ""
    for i in range(N):
        comboChars += getBoardSide(i, int(combos[c][i]))

    tempResult = [0]*26
    for i in range(len(comboChars)):
        tempResult[ord(comboChars[i])-97] += 1

    for i in range(len(tempResult)):
        if tempResult[i] > result[i]:
            result[i] = tempResult[i]

#Safely (create &) write to output file
with open("blocks.out", "w") as outFile:
    outFile.write("\n".join(map(str, result)))