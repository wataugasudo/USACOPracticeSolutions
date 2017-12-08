inFile = open('square.in','r')     #read in
outFile = open('square.out','w')  #write out

text = inFile.readlines()   #list of lines in input file
rect1 = list(map(int, text[0].split()))
rect2 = list(map(int, text[1].split()))

dX = max(rect1[2], rect2[2]) - min(rect1[0], rect2[0])
dY = max(rect1[3], rect2[3]) - min(rect1[1], rect2[1])

outFile.write(str(max(dX, dY)**2))

inFile.close()
outFile.close()
