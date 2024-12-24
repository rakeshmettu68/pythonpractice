try:
    try:
        a = int(input("please enter the Numenator: "))
        b = int(input("please enter the Denaminator: "))
        result = a/b
        print("The result is: ", result)
    except ZeroDivisionError as zerodivisionObj:
        print("zerodivision error is occured as Denaminator is suppiled as \"zero\"",end="\n")
        try:
            value3 = ("\nplease enter denamiantor: ")
            c = int(value3)
        except ValueError as valueErrorObj:
            print("\nHey string to integer consvestion is failed...")
            raise RuntimeError("an error is occured while proccesing input data.....") 
        except BaseException as base:
            print("Encounter un_kown abnormality...",end="\n")
            print("The message from the interpreter is : ", base)
    except BaseException as base:
        print("Encounter unkown abnormality...",end="\n")
        print("The message from the interpreter is : ", base)
except RuntimeError as runtimeObj:
    print("Runtime error is occured: ")
    print("The message from the interpreter is",runtimeObj)
    

except BaseException as base:
    print("Encounter unkown abnormality...",end="\n")
    print("The message from the interpreter is : ", base)