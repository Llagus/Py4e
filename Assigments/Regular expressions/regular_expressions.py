import re

fname = input("Enter file name:")
if len(fname) < 1 : fname = "regex_sum_42.txt"

try :
    file = open(fname)
except :
    print("This file does not exist")
    quit()

nsum = 0
for line in file : 
    lst = re.findall("[0-9]+", line)
    for member in lst : 
        try:
            num = int(member)
        except: 
            num = 0 
        nsum += num

print(nsum)