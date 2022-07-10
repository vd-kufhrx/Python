##longest prefix of s1 and s2:

def prefix(s1,s2):
    i = 0 
    s = s1[i]
    while i<len(s1) and s2.startswith(s):
        ##Enlarge the prefix until it is not common；
        i+=1
        s=s1[:i+1]
    s=s1[:i]
    return s
def main():
    s1 = input("Enter the first string:")
    s2 = input("Enter the second string:")
    print("the longest common prefix of the teo strings is / ",prefix(s1,s2),"/")
main()
    
    