import random
'''
This function takes 2 numbers and returns a rendom even number between them
'''
def Rand2(x,y):
    x = (x+1) / 2
    y = (y+1) / 2
    Rand = random.randrange(int(x)+1,int(y))
    return Rand * 2
