def debug_check(inlist):
    total = sum(inlist)
    percentagevalue = []
    for qun in inlist:
        try:
            result = (total/qun)*100
            percentagevalue.append(result)
        except ZeroDivisionError as Obj:
            print("something went worng in this prigramm")
            print("the abnormility is found ",Obj)
            percentagevalue.append(None)
    return percentagevalue    

inpurchase=[50,45,30,62,75,0,25,35,0,46,26]
purchasequn=debug_check(inpurchase)
if purchasequn is not None:
    print("the values is ",purchasequn)