def prog1(x,y):
    EvenNos = []
    for i in range(x+1,y):
        if(i % 2 == 0):
            EvenNos.append(i)
    return EvenNos