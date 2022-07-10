filename= input('Input a file:')   ###(C:\Users\王禹杭\Desktop\try.txt)
fhand = open(filename,"r")
counts = dict()
for item in fhand:
    words = item.split()
    for word in words:
        counts[word]=counts.get(word, 0)+1

str1 = list()
for keys, values in counts.items():
    str1.append((values, keys))

str1.sort(reverse = True)

for val,key in str1[:10]:
    print(key,val)


