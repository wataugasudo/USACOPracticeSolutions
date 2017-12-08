#Solves [http://usaco.org/index.php?page=viewproblem2&cpid=665]

inFile = open('cowsignal.in','r')     #read in
outFile = open('cowsignal.out','w')  #write out

text = inFile.readlines()   #list of lines in input file

ctrl = list(map(int, text[0].split()))

outString = ""
for m in range(1, ctrl[0]+1):
    tempString = ""
    for n in range(ctrl[1]):
        tempString += (text[m][n]*ctrl[2])
    outString += (tempString + "\n")*ctrl[2]
outFile.write(outString)

inFile.close()
outFile.close()
