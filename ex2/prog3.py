def prog3(x):
    s=int(x/2)
    for i in range(2,s+1):
        if x % i ==0:
            return(False)
            break
    return(True)