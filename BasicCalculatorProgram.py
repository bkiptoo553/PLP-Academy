def BasicCalc():
    #capturing user-input
    FNO = float(input("enter first number   "))
    SNO = float(input("enter second number  "))
    OP = input("enter the operator   ")

    # else-if statement for computation
    if OP == '+':
        ANS = FNO + SNO
    elif OP == '-':
        ANS = FNO - SNO
    elif OP == '*':
        ANS = FNO * SNO
    elif OP == '/':
        if SNO != 0:
            ANS = FNO / SNO
        else:
            print("No division by zero")
            return
    else:
        print("invalid operator")
        return

    print(f"Answer: {ANS}")   
BasicCalc() #calls the above function