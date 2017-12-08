#Solves [http://usaco.org/index.php?page=viewproblem2&cpid=688]

#Safely read list of String lines from input file
with open("hps.in", "r") as inFile:
    text = inFile.readlines()

h = {"s":1, "p":2, "h":"T"}
p = {"s":2, "p":"T", "h":1}
s = {"s":"T", "p":1, "h":2}

games = []
for i in range(1,int(text[0])+1):
    games.append(list(map(int, text[i].split())))

vict = [0]*6
combos = ["hps","hsp","psh","phs","shp","sph"]
for i in range(0, 6):
    result = 0
    for j in range(0, int(text[0])):
        if locals()[combos[i][games[j][0]-1]][combos[i][games[j][1]-1]] == 1:
            result += 1
    vict[i] = result

#Safely (create &) write to output file
with open("hps.out", "w") as outFile:
    outFile.write(str(max(vict)) + "\n")