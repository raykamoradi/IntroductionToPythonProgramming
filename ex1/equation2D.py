import math
'''
This function takes 3 numbers and calculates if they where the a, b and c values of a 2d equation what would the results be
'''
def equation2D(a,b,c):
    delta = b**2 - (4*a*c)
    if(delta < 0):
        return "There is no answeres for it"
    elif(delta == 0):
        return "There is one result: " + str((-b) / (2*a))
    else:
        return (-b + math.sqrt(delta)) / (2*a), (-b - math.sqrt(delta)) / (2*a)
