#Solves [http://usaco.org/index.php?page=viewproblem2&cpid=713]

inFile = open('cowqueue.in','r')    #read in
outFile = open('cowqueue.out','w')  #write out

text = inFile.readlines()   #list of lines in input file

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
outFile.write(str(total))

inFile.close()
outFile.close()
