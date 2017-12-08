#Solves [http://usaco.org/index.php?page=viewproblem2&cpid=711]

#Safely read list of String lines from input file
with open("crossroad.in", "r") as inFile:
    text = inFile.readlines()

total = 0
pos = [-1]*10
for i in range(1, int(text[0])+1):
    entry = text[i].split()
    tag = int(entry[0])-1
    side = int(entry[1])
    if pos[tag] != side:
        if pos[tag] != -1:
            total += 1
        pos[tag] = side

#Safely (create &) write to output file
with open("crossroad.out", "w") as outFile:
    outFile.write(str(total))