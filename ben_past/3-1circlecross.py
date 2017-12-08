inFile = open('circlecross.in','r')     #read in
outFile = open('circlecross.out','w')   #write out

cows = list(inFile.readlines()[0])   #list of cow IDs

def scan(start, end):
    for m in range(start+1, end):
        if tempcows[m] == tempcows[start]:
            tempcows[m] = 0
            print(start, m)
            return False    #cows don't cross
        tempcows[start] = 0
    return True             #cows cross

total = 0
for i in range(0, len(cows)-1):
    first = cows[i]
    if first != 0:
        for j in range(1, (len(cows))-i):
            current = cows[i+j]
            if first == current:
                break
        tempcows = cows
        for x in range(i+1, i+j):
            total += scan(x,j) & bool(cows[x])
            tempcows[x]
        cows[i] = 0
        cows[j] = 0

outFile.write(str(total))

inFile.close()
outFile.close()
