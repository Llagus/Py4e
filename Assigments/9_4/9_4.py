name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

lst = list()
dic = dict()

for sentence in handle :
    if  not sentence.startswith("From ") : continue
    lst = sentence.split()
    dic[lst[1]]= dic.get(lst[1],0) + 1

adress = None
count = None
for k,v in dic.items() : 
    if adress is None or v > count : 
        adress = k
        count = v
print(adress, count)    
