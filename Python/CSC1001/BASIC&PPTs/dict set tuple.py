###most powerful data collection::::dictionary{}
dct = dict()
dct['age'] = 21
dct[21] = 24
print(dct)

##count how many times a word has been inputtted before
# wordDict = dict()
# while True:
#     word = input('Enter a word:')
#     if word == 'done':
#         break
#     elif word in wordDict:
#         wordDict[word]+=1
#     else:
#         wordDict[word]=1
# print('The result of the word count:',wordDict)

###   .get
counts = {'aaa':1,'bbb':2,'ccc':5}
print(counts.get('aaa',3))
print(counts.get('eee','s'))
for key, value in counts.items():
    print(key,value)

###times each word appears:
# wordDict={}
# text = input('Enter a line:')
# words = text.split()
# print('Counting...')
# for word in words:
#     wordDict[word] = wordDict.get(word,0)+1
# print('The result of the word count:',wordDict)


##open a file and count::
# #(C:\Users\王禹杭\Desktop\try.txt)

# filename = input("input the file name:")
# file1 = open(filename, "r")
# wordDict = dict()
# for item in file1:
#     words = item.split()
#     for word in words:
#         wordDict[word] = wordDict.get(word,0)+ 1
# print(wordDict)

purse = dict()
purse['money'] = 12
purse['candy']= 5
print(purse)
purse[3]= 3**3
purse['candy']= purse['candy']+2
print(purse)


##convert dic into list
print(list(purse.values()))
print(list(purse))
print(list(purse.items()))


print('\n#############################\n')          ##set
a = set('abrcdabrcd')  #集合set
b = set('alczaalcz')
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素

###tuple:temporary variables

