def func3(x):
    Mult = 1
    Value = 0
    while x > Mult:
        Mult = Mult * 10
    while x > 1:
        while x > Mult:  
            Value += Mult          
            x -= Mult
        Mult = Mult // 10
    return Value