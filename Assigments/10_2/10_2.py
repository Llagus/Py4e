name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = None
dic = dict()
for line in handle : 
    if  not line.startswith("From ") : continue
    lst = line.split()
    lst = lst[5].split(":")
    word = lst[0]
    dic[lst[0]] = dic.get(lst[0], 0) + 1

lst = sorted([ (k,v) for k,v in  dic.items()])

for k,v in lst : 
    print(k, v)
