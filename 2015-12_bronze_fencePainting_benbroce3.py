#Solves [http://usaco.org/index.php?page=viewproblem2&cpid=567]

#Safely read list of String lines from input file
with open("paint.in", "r") as inFile:
    text = inFile.readlines()

#read farmer & cow's variables as integer list elements
#(split 1st & 2nd text[] lines at the space,
# cast/"map" each variable to an integer,
# convert back to a list from a map() element)
f = list(map(int, text[0].split()))
c = list(map(int, text[1].split()))

fence = [0]*101 #create a list of 101 zeros

#step through a..b & c..d index ranges in the fence list,
#changing each value in the range to a 1
for i in range(f[0], f[1]):
    fence[i] = 1
for i in range(c[0], c[1]):
    fence[i] = 1
    
#sum all #s in fence list
total = sum(fence)

#Safely (create &) write to output file
with open("paint.out", "w") as outFile:
    outFile.write(str(total))
