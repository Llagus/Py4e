# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try : 
    fh = open(fname)
except : 
    print("Error: file name")
    quit()
s = 0.0
count = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    num = float(line[line.find(" "):].strip())
    count = count + 1 
    s = s + num 
print("Average spam confidence:", s/count)
