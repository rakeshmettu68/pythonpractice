a = int(input("Enter a year: "))
if a%4==0 and a%100 !=0:
    print("Given year is a leap year")
elif a%400==0:
    print("Given year is a leap year")
else:
    print("Given year is not  a leap year")
    
if a%4==0:
    if a%100==0:
        if a%400==0:
            print("YES Given year is leap year %d"%(a))   
        else:
            print("Sorry Given year %d is not leap year "%(a))
    else:
        print("Sorry Given year %d is not leap year "%(a))
else:
    print("Sorry Given year %d is not leap year "%(a))
    
