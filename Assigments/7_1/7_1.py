fname = input("Enter file name: ")

try :
    fh = open(fname)
except : 
    print("Error: name file incorrect")
    quit()

file = fh.read().upper().rstrip()
print(file)