#Solves [http://usaco.org/index.php?page=viewproblem2&cpid=665]

#Safely read list of String lines from input file
with open("cowsignal.in", "r") as inFile:
    text = inFile.readlines()

ctrl = list(map(int, text[0].split()))

outString = ""
for m in range(1, ctrl[0]+1):
    tempString = ""
    for n in range(ctrl[1]):
        tempString += (text[m][n]*ctrl[2])
    outString += (tempString + "\n")*ctrl[2]

#Safely (create &) write to output file
with open("cowsignal.out", "w") as outFile:
    outFile.write(outString)