from functools import partial 
def currencyConverter(inamount,intconversionRate):
    return inamount*intconversionRate
usd2Euro = partial(currencyConverter,intconversionRate=0.82)
usd2Gbp = partial(currencyConverter,intconversionRate=0.71)
usd2Jpy = partial(currencyConverter,intconversionRate=109.16)
usd2Inr = partial(currencyConverter,intconversionRate=81)


print("\nplease enter the choice of currency conversion....",end="\n")
print('\n1.USD To EURO\n2.USD To GBP\n3.USD to GPY\n4.USD To INR',end="\n")
conversionType = int(input("please enter the choice from the menu: "))
if conversionType ==1:
    inAmount= int(input("please enter the amount for the conversion in USD: "))
    print("\nThe given amount for %d coverted to EURO is :%d"%(inAmount,usd2Gbp(inAmount)))
elif conversionType==2:
    inAmount= int(input("please enter the amount for the conversion in USD: "))
    print("\nThe given amount for %d coverted to GBP is :%d"%(inAmount,usd2Jpy(inAmount)))
elif conversionType==3:
    inAmount= int(input("please enter the amount for the conversion in USD: "))
    print("\nThe given amount for %d coverted to JPY is :%d"%(inAmount,usd2Inr(inAmount)))
elif conversionType==4:
    inAmount= int(input("please enter the amount for the conversion in USD: "))
    print("\nThe given amount for %d coverted to INR is :%d"%(inAmount,usd2Euro(inAmount)))
else:
    print("please enter the correct choice for current conversion")