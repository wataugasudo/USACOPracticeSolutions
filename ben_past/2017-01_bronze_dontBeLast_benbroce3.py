#Solves [http://usaco.org/index.php?page=viewproblem2&cpid=687]

#Safely read list of String lines from input file
with open("notlast.in", "r") as inFile:
    text = inFile.readlines()

log = []
logdict = {"Bessie":0, "Elsie":0, "Daisy":0, "Gertie":0, "Annabelle":0,
           "Maggie":0, "Henrietta":0}

for i in range(1, int(text[0])+1):
    entry = text[i].split()
    logdict[entry[0]] += int(entry[1])

#https://docs.python.org/2/library/functions.html
log = sorted(list(logdict.items()), key=lambda x: x[1])

m = log[0][1]
slast = 0
while log[slast][1] <= m:
    slast += 1

if slast != 6:
    if log[slast][1] == log[slast + 1][1]:
        outFile.write("tie\n")

#Safely (create &) write to output file
with open("notlast.out", "w") as outFile:
    outFile.write(log[slast][0] + "\n")