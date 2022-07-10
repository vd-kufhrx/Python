# x=[1,2,'joe',99]
# print(len(x))

# num=[3,4,5,6,7]
# print(max(num))
# print(sum(num)/len(num))
# print(9 in num)
# if 9 not in num:
#     print('oh yeah ')
# else:
#     print('  oooops')

# for i in num:
#     print('HAPPY',i)
    
# for i in range(len(num)):
#     if i%2==1:
#         fri = num[i]
#         print('HAPPY',fri)


###copy and change elements
friends = ['Tom','Jerry']
for friend in friends:
    friend = 'David'

# for i in range(len(friends)):
    # friends[i] = 'David'

Newfriends = friends.copy()
Newfriends[0]='David'
print(friends)
print(Newfriends)

####  add elements:::
stuff = list()
stuff.append(99)
stuff.append('my love')
print(stuff)

###find average by list
# numlist = list()
# while True:
#     try:
#         inp = input('Enter a number:')
#         if inp == 'done': break
#         value=float(inp)
#         numlist.append(value)
#     except:
#         print('invalid input')
# average = sum (numlist)/len(numlist)
# print('The average value is:',average)

##split()  to:list
myStr = 'i love      you,f for  my love'
words = myStr.split()
for i in words:
    print(i)

words1= myStr.split(',')
print(words1)

print('\n#########################\n')
###sort  v.s. sorted
list1 = [1, 6, 4, 15, 3]
list_new = list1.sort()

print(list1)
print(list_new)

list2 = sorted(list1)
print(list2)

list1.sort(reverse=True)
print(list1)

print('\n#########################\n')

header = 'From professor.xman@uct.edu Sat Jan 5 09:14:16 2008'
words = header.split()
address = words[1].split('@')
print('The email domain is:', address[1])
print('the month when the email is sent:',words[3])


##delete::s=s[:i]+s[i+1:]

