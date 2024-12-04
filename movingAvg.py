def calAverage():
    out_list = []
    def inner(invalue = None):
        if invalue is not None:
            out_list.append(invalue)
            return sum(out_list)/len(out_list)
    return inner
def total_avg(inList):
    a=calAverage()
    my_list = []
    for num in inList:
        my_list.append(a(num))
    return my_list
        
if __name__=="__main__":
    b = [2,4,6,8,10]
    result = total_avg(b)
    print(result)