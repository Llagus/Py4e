score = input("Enter Score: ")

try : 
    s = float(score)
except : 
    print("Score needs to be a numeric value")
    quit()

if s >= 1 or s < 0 : 
    print("Score is out of Range:(0-1)")
elif s >= 0.9 : 
    print("A")
elif s >= 0.8 : 
    print("B")
elif s >= 0.7 : 
    print("C")
elif s >= 0.6 : 
    print("D")
else : 
    print("F")

