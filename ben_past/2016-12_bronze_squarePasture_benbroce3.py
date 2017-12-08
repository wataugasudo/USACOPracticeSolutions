#Solves [http://usaco.org/index.php?page=viewproblem2&cpid=663]

#Safely read list of String lines from input file
with open("square.in", "r") as inFile:
    text = inFile.readlines()

rect1 = list(map(int, text[0].split()))
rect2 = list(map(int, text[1].split()))

dX = max(rect1[2], rect2[2]) - min(rect1[0], rect2[0])
dY = max(rect1[3], rect2[3]) - min(rect1[1], rect2[1])

#Safely (create &) write to output file
with open("square.out", "w") as outFile:
    outFile.write(str(max(dX, dY)**2))