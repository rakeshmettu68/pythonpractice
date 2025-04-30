
#check if the given string palindrom or not using recursion
def is_palindrom(string,len_string,r):
    if r>=len_string:
        return True
    elif string[r] != string[len_string]:
        return False
    else:
        return is_palindrom(string,len_string-1,r+1)

string = input("Enter a string: ")
len_string = len(string)-1
r = 0
check=(string,len_string,r)
if check:
    print("Given string is a palindrom")
else:
    print("Given a string is not a palindrom")