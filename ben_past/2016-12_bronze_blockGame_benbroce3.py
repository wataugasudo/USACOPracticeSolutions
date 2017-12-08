import itertools

inFile = open('blocks.in','r') #read in
outFile = open('blocks.out','w') #write out

text = inFile.readlines() #list of lines in input file
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

outFile.write("\n".join(map(str, result)))

inFile.close()
outFile.close()
