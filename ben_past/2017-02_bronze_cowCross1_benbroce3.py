inFile = open('crossroad.in','r')   #read in
outFile = open('crossroad.out','w') #write out

text = inFile.readlines()   #list of lines in input file

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
outFile.write(str(total))

inFile.close()
outFile.close()
