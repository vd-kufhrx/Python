def isValidPassword(password):
    if len(password)<8:
        print("A password must have at least eight characters.")
        return False
    if not password.isalnum():
        print('A password must consist of only letters and digits.')
        return False
    count = 0
    for ch in password:
        if ch.isdigit():
            count+=1
    if count<2:
        print('A pass world must contain at least two digits')
        return False 
    else:
        return True
def main():
    while True:
        password = input(('PLEASE input a password:'))
        if isValidPassword(password):
            print('Yes')
            break
main()