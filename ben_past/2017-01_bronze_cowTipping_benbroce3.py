#Solves [http://usaco.org/index.php?page=viewproblem2&cpid=689]

#Safely read list of String lines from input file
with open("cowtip.in", "r") as inFile:
    text = inFile.readlines()

n = int(text[0][:1])

cows = []
for i in range(1, n+1):
    cows.append(list(map(int, text[i][:n])))

count = 0
def toggle(x,y):
    count += 1
    x -= 1
    y -= 1
    for i in range(0,y+1):
        for j in range(0,x+1):
            cows[i][j] = not(cows[i][j])

def diagonals(L): #http://stackoverflow.com/questions/23069388/listing-elements-in-a-nested-lists-diagonally/23069625#23069625
        """
            >>> L = array([[ 0,  1,  2],
                           [ 3,  4,  5],
                           [ 6,  7,  8],
                           [ 9, 10, 11]])
            >>> antidiagonals(L)
                    [[0], [3, 1], [6, 4, 2], [9, 7, 5], [10, 8], [11]]
        """
    return [[L[p - q][q] for q in range(max(p-n+1,0), min(p+1, n))]for p in range(2 * n - 1)]

dcows = diagonals(cows)

for i in range(2 * n - 1):
    for j in range(len(dcows[i])):
        if cows

####


#Safely (create &) write to output file
with open("cowtip.out", "w") as outFile:
    outFile.write("Test")