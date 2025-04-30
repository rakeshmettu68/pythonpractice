n = int(input("Enter a number "))
for i in range (1,n+1):
    spaces = (n-i)*" "
    stars = "* "*i
    print(spaces+stars)
# if you have to print the left triangle just add  one space
    