text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(" ")
snum = text[pos:].strip()
num = float(snum)
print(num)