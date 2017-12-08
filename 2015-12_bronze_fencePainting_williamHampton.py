#Solves [http://usaco.org/index.php?page=viewproblem2&cpid=567]

with open('paint.in') as infile:                                        #open infile
  read_data = infile.read()                                             #read from infile

read_data = list(map(int, read_data.replace("\n"," ").split()))         #map input to a list

fj = []                                                                 #initialize painted values list
for x in range(0,3,2):                                                  #loop over a,b and then c,d
  for y in range(read_data[x],read_data[x+1]):                          #loop for each value in the interval
    fj.append(y)                                                        #append painted values to list

fj = str(len(list(set(fj))))                                            #organize values and remove duplicates, count length of painted values 

with open('paint.out', 'w') as outfile:                                 #open outfile
  outfile.write(fj)                                                     #write to outfile
