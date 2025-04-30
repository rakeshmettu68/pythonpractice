#A number is said to be  an Armstrong number, if the sum of the power  of all the digits of N is equal to Number 
#is the numer itself 

'''number =int(input("Enter a number "))
str_num = str(number)
len_num = len(str_num)
a = 0
for i in range(len_num):
    b = int(str_num[i]) ** len_num
    a = a+b
if a == number:
    print("yes given nuber is ARMSTRONG number ")
else:
    print("no")'''
"-----------------------------------------------------------"
n = int(input("Enter a number : "))
sum_of_digits =0
len_n = len(str(n))
int_n = int(n)
while n !=0:
    rem = n%10
    num = rem**len_n
    sum_of_digits +=num
    n = n//10
if sum_of_digits==int_n:
    print("Given number is Armstrong number ")
else:
    print("Given number ids not a Armstrong number")
    


