#Solves [http://usaco.org/index.php?page=viewproblem2&cpid=712]

#Safely read list of String lines from input file
with open("circlecross.in", "r") as inFile:
    text = inFile.readlines()

cows = list(text[0])   #list of cow IDs

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

#Safely (create &) write to output file
with open("circlecross.out", "w") as outFile:
    outFile.write(str(total))