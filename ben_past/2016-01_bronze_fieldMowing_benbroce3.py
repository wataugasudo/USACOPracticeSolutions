#Solves [http://usaco.org/index.php?page=viewproblem2&cpid=593]

#Safely read list of String lines from input file
with open("mowing.in", "r") as inFile:
    text = inFile.readlines()

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
    
###

#Safely (create &) write to output file
with open("mowing.out", "w") as outFile:
    outFile.write(str(moves))