def myCache(inFunction):
    cachememory ={}
    def excefactorial(inValue):
        if inValue in cachememory:
            return cachememory[inValue]
        else:
            finalResult = inFunction(inValue)
            cachememory[inValue]= finalResult
            return finalResult
    return excefactorial
def calcFibonacci(inValue):
    if inValue in[0,1]:
        return inValue
    else:
        return  myCache(calcFibonacci)(inValue-1) + myCache(calcFibonacci)(inValue-2)
def printFibonacciserices(inFibvalue):
    final_result = [calcFibonacci(fibindex) for fibindex in range (inFibvalue)] 
    return final_result  
if __name__== "__main__":
    n = int(input("Enter a number: "))
    out_result = printFibonacciserices(n)
    print("\nThe Fibonacci series for the first %d values is:"%(n))
    print(out_result)

