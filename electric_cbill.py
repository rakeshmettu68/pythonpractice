#electric Charge and their rates
# 1 to 100 units : 1.5 rs extra_charge :25
#101 to 200 units :2.5 rs extra_charge :50
#201 to 300 units :4 rs   extra_charge :75
#300 to 350 units :5 rs   extra_charhge =;100
# above 350 _fixed charge 1500 rs
def current_bill(units):
    if units <=100:
        amount = units*1.5
        extra_charge = 25
        total_amount = amount+extra_charge
        print(total_amount)
    elif units <=200:
        amount = (100*1.5)+(units-100)*2.5
        extra_charge = 50
        total_amount = amount+extra_charge
        print(total_amount)
    elif units <=300:
        amount = (100*1.5)+(100)*2.5+(units-200)*4
        extra_charge = 75
        total_amount = amount+extra_charge
        print(f"the total charge for your units : {units}={total_amount}")
    elif units <=350:
        amount = (100*1.5)+(100)*2.5+(100)*4+(units-300)*5
        extra_charge= 100
        total_amount = amount+extra_charge
        print(total_amount)
    else:
        amount = 0
        extra_charge = 1500
        total_amount = amount+total_amount
        print(total_amount)
units = int(input("Enter a units: "))
if units>0:
    current_bill(units)
else:
    print("Please enter the valid units")