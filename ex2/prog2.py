def prog2(x,y):
    EvenNos = []
    if x < y:
        for i in range(x+1,y):
            if(i % 2 == 0):
                EvenNos.append(i)
    else:
        for i in range(y+1,x):
            if(i % 2 == 0):
                EvenNos.append(i)
    return EvenNos