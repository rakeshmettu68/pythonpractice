temparature = input("Enter a temp: ")
unit = temparature[-1]
value= float(temparature[:-1])
degress = (round(value,2))
if unit =="c" or unit =="C":
   print(str(degress)+"C")
   F = round((9/5*degress)+32,2) #formula for celsius to fahrenhit f = (c*9/5)+32

   print(str(F)+"F")
   K = round(degress+273,2) # formula for celsius to kelvin  k = 273+c 
   print(str(K)+"K")
elif unit=="F" or unit=="f":
   print(str(degress)+"F")
   C = round((degress-32)*5/9,2)#formula for fahernhit to celsius c = (F-32)*5/9
   print(str(C)+"C")
   K = round(C+273,2)#ormula for fahernhit to kelvin k = c+273k
   print(str(K)+"K")
elif unit=="k" or unit=="k":
   C = round((degress-273),2)#ormula for kelvin to celsius = c-273k
   print(str(C)+"C")
   F = round((9/5*c)+32,2)#formula for kelvin to fahernhit f = (c*9/5)+32
   print(str(F)+"F")
   print(str(degress)+"K")