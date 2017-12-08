inFile = open('mowing.in','r')      #read in
outFile = open('mowing.out','w')    #write out

text = inFile.readlines()   #list of lines in input file

# setup move list (strings)
moves = []
for i in range(1, int(text[0])+1):
    moves.append(text[i].split())

#setup coordinate system & move
visited = 
pos = [0,0]
for i in range(moves):
    pos[0] += moves[i][1] if moves[i][0] = "E"
    pos[0] -= moves[i][1] if moves[i][0] = "W"
    pos[1] += moves[i][1] if moves[i][0] = "N"
    pos[1] -= moves[i][1] if moves[i][0] = "S"

    

outFile.write(str(moves))

inFile.close()
outFile.close()
