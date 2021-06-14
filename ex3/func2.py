def func2(x):
    HelperList = ['0','1','2','3','4','5','6','7','8','9']
    i = 0
    Value = 0
    HelperVal = 0
    FloatHelper = 0
    while i < len(x):
        if(x[i] != "."):
            Value = Value +  (HelperList.index(x[i]) * (10 ** ((len(x) -2 - i) + HelperVal))) 
        else:    
            FloatHelper = i
            HelperVal = 1   
        i += 1
    return Value/ (10 ** (len(x) - (FloatHelper + 1)))
