#Solves [http://usaco.org/index.php?page=viewproblem2&cpid=687]

inFile = open('notlast.in','r')     #read in
outFile = open('notlast.out','w')   #write out

text = inFile.readlines()   #list of lines in input file

log = []
logdict = {"Bessie":0, "Elsie":0, "Daisy":0, "Gertie":0, "Annabelle":0, "Maggie":0, "Henrietta":0}

for i in range(1, int(text[0])+1):
    entry = text[i].split()
    logdict[entry[0]] += int(entry[1])

log = sorted(list(logdict.items()), key=lambda x: x[1]) #https://docs.python.org/2/library/functions.html

m = log[0][1]
slast = 0
while log[slast][1] <= m:
    slast += 1

if slast != 6:
    if log[slast][1] == log[slast + 1][1]:
        outFile.write("tie\n")
outFile.write(log[slast][0] + "\n")

inFile.close()
outFile.close()
