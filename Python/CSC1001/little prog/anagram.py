s1 = input('Please enter the first word:')
s2 = input('Please enter the second word:')
if s1 == s2:  # Check if the two strings are the same
    print('Two words are the same.')
else:
    s1_list, s2_list = list(s1), list(s2)  # Convert strings into lists
    s1_list.sort()
    s2_list.sort()
    if s1_list == s2_list:  # Check if the two lists are the same after sorting
        # Capitalize the first letter
        print(s2.capitalize(), 'is an anagram of', s1 + '.')
    else:
        print(s2.capitalize(), 'is not an anagram of', s1 + '.')
