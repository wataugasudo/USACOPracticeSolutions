#Solves [http://usaco.org/index.php?page=viewproblem2&cpid=713]

#Safely read list of String lines from input file
with open("cowqueue.in", "r") as inFile:
    text = inFile.readlines()

queue = []
for i in range(1, int(text[0])+1):
    queue.append(list(map(int, text[i].split())))
queue = sorted(queue)

total = 0
for i in range(0, len(queue)):
    if queue[i][0] > total:
        total = queue[i][0] + queue[i][1]
    else:
        total += queue[i][1]

#Safely (create &) write to output file
with open("cowqueue.out", "w") as outFile:
    outFile.write(str(total))