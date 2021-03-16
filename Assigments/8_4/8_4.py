fname = input("Enter file name: ")
try : 
    fh = open(fname)
except : 
    print("Error: file doesn't exist")

is_there = False
lst = list()
for line in fh:
    line.rstrip()
    words = line.split()
    for word in words :
        if word  not in lst : 
            lst.append(word)
lst.sort()
print(lst)

#print(line.rstrip())