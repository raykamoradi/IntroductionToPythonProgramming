def prog4(x):
    Divisors = []
    for i in range(1,x+1):
            if(x % i == 0):
                Divisors.append(i)          
    return Divisors
