import math
'''
This function takes 5 numbers and returns the area of the shape discribed (4 first numbers are the sides and 5th is the diametere)
If any of the the first 4 numbers are zero the 3 other numbers count as a triangle
'''
def AreaX(A,B,C,D,E):
    if any(A,B,C,D == 0):
        Values = [A,B,C,D]
        Values = sorted(Values, reverse=False) 
        X1 = Values[1]
        X2 = Values[2]
        X3 = Values[3]
        P = (X1 + X2 + X3) / 2
        AreaAmount = math.sqrt([P * (P - X1) * (P - X2) * (P - X3)])
    else:
        P1 = (A + B + E) / 2
        P2 = (E + D + C) / 2
        AreaAmount = math.sqrt(P1 * (P1 - A) * (P1 - B) * (P1 - E)) + math.sqrt(P2 * (P2 - C) * (P2 - D) * (P2 - E))
    return AreaAmount
